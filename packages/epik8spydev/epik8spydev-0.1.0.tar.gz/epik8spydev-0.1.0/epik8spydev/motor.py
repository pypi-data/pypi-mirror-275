# epik8spydev/motor.py

from abc import ABC, abstractmethod

class Motor(ABC):
    @abstractmethod
    def home(self):
        pass

    @abstractmethod
    def jogf(self):
        pass

    @abstractmethod
    def jogr(self):
        pass

    @abstractmethod
    def set(self, position):
        pass

    @abstractmethod
    def set_rel(self, position):
        pass

    @abstractmethod
    def get_setpoint(self):
        pass

    @abstractmethod
    def get_pos(self):
        pass

    @abstractmethod
    def ismoving(self):
        pass

    @abstractmethod
    def iserror(self):
        pass

    @abstractmethod
    def ishomed(self):
        pass

    @abstractmethod
    def dir(self):
        pass

    @abstractmethod
    def limit(self):
        pass
