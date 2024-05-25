from .device import Device
from .household import Household

class Room:
    def __init__(self, id: str, name: str, devices: list[Device], household: Household):
        self.id = id
        self.name = name
        self.devices = devices
        self.household = household

    def __str__(self) -> str:
        return f'<Room id={self.id} name={self.name} devices={self.devices} household={self.household}>'
    
    def __repr__(self) -> str:
        return self.__str__()