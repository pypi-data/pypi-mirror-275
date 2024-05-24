# epik8spydev/tml_motor.py

import epics
import asyncio
from .motor import Motor

# Constants for motor commands and states
NOSTATE = -1
PROCESSING = 4
ERROR = 6
FAULT = 8
HOMED = 0x4000
MOVING = 0x0200
CMD_HOME = 3
CMD_ABS_POS = 2
CMD_REL_POS = 1
CMD_JOGF = 4
CMD_JOGR = 5

RUN = 1
STOP = 2
POS_TOLERANCE = 10

class TmlMotor(Motor):
    def __init__(self, name, pv_base, poi):
        self.name = name
        self.pv_names = {
            "mot_msgs": f"{pv_base}:MSGS",
            "mot_stat": f"{pv_base}:STAT",
            "mot_msta": f"{pv_base}:MSTA",
            "mot_act_sp": f"{pv_base}:ACT",
            "mot_act_rb": f"{pv_base}:ACT_RB",
            "mot_actx_sp": f"{pv_base}:ACTX_SP",
            "mot_cur_pos": f"{pv_base}:RBV",
            "mot_val_sp": f"{pv_base}:VAL_SP",
            "mot_val_rb": f"{pv_base}:VAL_RB",
            "desired_position_name": "DESIRED_POS_NAME"
        }
        self.mot_stat = NOSTATE
        self.state = "NOSTATE"
        self.mot_val_sp = -1
        self.cmd = "NONE"
        self.poi = poi
        self.current_position = None
        
        # Create monitors for the PVs
        self.monitors = {
            "mot_stat": epics.PV(self.pv_names["mot_stat"], callback=self.on_mot_stat_change),
            "mot_msta": epics.PV(self.pv_names["mot_msta"], callback=self.on_mot_msta_change),
            "mot_cur_pos": epics.PV(self.pv_names["mot_cur_pos"], callback=self.on_mot_cur_pos_change)
        }

        # Initial connection check
        if not self.monitors["mot_stat"].connected:
            raise Exception(f"{name} Cannot connect to {self.pv_names['mot_stat']}")
        
        task = asyncio.create_task(self.update())
        task.set_name(f"{name} update")

    def poi2pos(self, poi_name):
        for k in self.poi:
            if poi_name == k['name']:
                return k['pos']
        return -1000

    def pos2poi(self, position):
        for k in self.poi:
            if k['pos'] - POS_TOLERANCE <= position <= k['pos'] + POS_TOLERANCE:
                return k['name']
        return ""

    async def update(self):
        self.state = "INIT"
        while True:
            if self.state == "INIT":
                self.state = "CONNECT"

            elif self.state == "CONNECT":
                print("CONNECTING")
                mot_stat = self.mot_stat
                if mot_stat == PROCESSING:
                    self.state = "CHKHOMED"
                elif mot_stat not in (PROCESSING, ERROR, FAULT):
                    epics.caput(self.pv_names["mot_msgs"], "START")
                    self.state = "WAITCONNECT"
                else:
                    await asyncio.sleep(5)

            elif self.state == "WAITCONNECT":
                print("WAIT CONNECT")
                mot_stat = self.mot_stat
                if mot_stat == PROCESSING:
                    self.state = "CHKHOMED"
                elif mot_stat in (ERROR, FAULT):
                    self.state = "CONNECT"
                else:
                    await asyncio.sleep(1.5)

            elif self.state == "CHKHOMED":
                print("CHECK HOMED")
                if self.mot_msta & HOMED:
                    self.state = "READY"
                else:
                    self.state = "STARTHOME"

            elif self.state == "STARTHOME":
                print("START HOMING")
                mot_stat = self.mot_stat
                if mot_stat != PROCESSING:
                    self.state = "CONNECT"
                elif self.mot_act_rb == CMD_HOME:
                    epics.caput(self.pv_names["mot_actx_sp"], RUN)
                    self.state = "WAITHOME"
                else:
                    await asyncio.sleep(0.5)

            elif self.state == "WAITHOME":
                print("WAIT HOME")
                if self.mot_msta & HOMED:
                    self.state = "READY"
                elif self.mot_stat != PROCESSING:
                    self.state = "CONNECT"
                else:
                    await asyncio.sleep(1.0)

            elif self.state == "READY":
                await asyncio.sleep(0.1)

            elif self.state == "WAITEND":
                mot_stat = self.mot_stat
                if mot_stat != PROCESSING:
                    self.state = "CONNECT"
                    continue
                
                if not self.ismoving():
                    self.state = "READY"
                    continue

            await asyncio.sleep(0.5)

    def home(self):
        epics.caput(self.pv_names["mot_act_sp"], CMD_HOME)
        epics.caput(self.pv_names["mot_actx_sp"], RUN)
        self.cmd = "HOME"
        self.state = "WAITEND"

    def jogf(self):
        epics.caput(self.pv_names["mot_act_sp"], CMD_JOGF)
        epics.caput(self.pv_names["mot_actx_sp"], RUN)
        self.cmd = "JOGF"
        self.state = "WAITEND"

    def jogr(self):
        epics.caput(self.pv_names["mot_act_sp"], CMD_JOGR)
        epics.caput(self.pv_names["mot_actx_sp"], RUN)
        self.cmd = "JOGR"
        self.state = "WAITEND"

    def set(self, position):
        if isinstance(position, str):
            position = self.poi2pos(position)
        
        epics.caput(self.pv_names["mot_val_sp"], position)
        epics.caput(self.pv_names["mot_act_sp"], CMD_ABS_POS)
        epics.caput(self.pv_names["mot_actx_sp"], RUN)
        self.mot_val_sp = position
        self.cmd = "ABS"
        self.state = "WAITEND"

    def set_rel(self, position):
        epics.caput(self.pv_names["mot_val_sp"], position)
        epics.caput(self.pv_names["mot_act_sp"], CMD_REL_POS)
        epics.caput(self.pv_names["mot_actx_sp"], RUN)
        self.mot_val_sp = position
        self.cmd = "REL"
        self.state = "WAITEND"

    def get_setpoint(self):
        return epics.caget(self.pv_names["mot_val_sp"])

    def get_pos(self):
        return self.current_position

    def ismoving(self):
        return epics.caget(self.pv_names["mot_msta"] + ".BA")

    def iserror(self):
        return epics.caget(self.pv_names["mot_msta"] + ".B9")

    def ishomed(self):
        return epics.caget(self.pv_names["mot_msta"] + ".BE")

    def dir(self):
        return epics.caget(self.pv_names["mot_msta"] + ".B0")

    def limit(self):
        lsn = epics.caget(self.pv_names["mot_msta"] + ".BD")
        lsp = epics.caget(self.pv_names["mot_msta"] + ".B2")
        if lsn:
            return -1
        if lsp:
            return 1
        if lsn and lsp:
            return -1000
        return 0

    def on_mot_stat_change(self, pvname=None, value=None, **kwargs):
        self.mot_stat = value
        print(f"Mot stat changed: {value}")

    def on_mot_msta_change(self, pvname=None, value=None, **kwargs):
        self.mot_msta = value
        print(f"Mot msta changed: {value}")

    def on_mot_cur_pos_change(self, pvname=None, value=None, **kwargs):
        self.current_position = value
        #print(f"Current position changed: {value}")
