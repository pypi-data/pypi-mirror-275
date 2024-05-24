# epik8spydev

A package for controlling motors with EPICS and asyncio.

## Installation

```bash
pip install epik8spydev
```
## Usage

```
from epik8spydev import TmlMotor

# Example usage
pv_base = "PV:BASE"
poi = [{"name": "home", "pos": 0}, {"name": "position1", "pos": 100}]
motor = TmlMotor(name="Motor1", pv_base=pv_base, poi=poi)

# Perform motor actions
motor.home()
motor.set(100)
```

### Package
python setup.py sdist bdist_wheel
pip install twine
twine upload dist/*


