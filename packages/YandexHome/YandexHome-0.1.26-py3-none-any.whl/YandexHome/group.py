from typing import Literal
from .device import Device
from .household import Household
from aiohttp import ClientSession
from asyncio import run
from typing import Any

class YandexHomeError(BaseException): pass

async def post(url, headers, json):
    async with ClientSession() as session:
        async with session.post(url, headers=headers, json=json) as req:
            return await req.json()

async def get_device(deviceId: str, token: str):
    async with ClientSession() as session:
        async with session.get(f'https://api.iot.yandex.net/v1.0/devices/{deviceId}', headers={'Authorization': f'Bearer {token}'}) as req:
            json = await req.json()
            if json['status'] == 'ok':
                device = Device(json['id'], json['name'], json['aliases'], json['room'], json['external_id'], json['skill_id'], json['type'], json['groups'], json['capabilities'], json['properties'], json.get('household_id', '0'), token)
                return device
            else:
                raise YandexHomeError(json['message'])

class Group:
    def __init__(self, id: str, name: str, aliases: list[str], group_type: str, state: Literal['online', 'offline', 'split'], devices: list, household: Household, token: str) -> None:
        self.__attr = ['id', 'name', 'aliases', 'type', 'state', 'devices', '_Group__token', 'capabilities', 'avaible_properties', 'household']
        self.id = id
        self.name = name
        self.aliases = aliases
        self.type = group_type
        self.state = state
        self.household = household
        self.devices: list[Device] = []
        self.__token = token
        for __device in devices:
            self.devices.append(run(get_device(__device['id'], self.__token)))
        for device in self.devices:
            device: Device
            device.__delattr__('groups')
        self.capabilities = []
        for device in self.devices:
            for capability in device.capabilities:
                self.capabilities.append(capability)
        self.avaible_properties = []
        for capability in self.capabilities:
            self.avaible_properties.append(capability.instance)
            self.__setattr__(capability.instance, capability.__getattribute__(capability.instance))
            
    def __setattr__(self, __name: str, __value: Any) -> None:
        first = False
        try: self.__getattribute__(__name)
        except: first = True
        object.__setattr__(self, __name, __value)
        if __name not in self.__attr and __name != '_Device__attr' and not first:
            action_type = ''
            for capability in self.capabilities:
                if capability.instance == __name:
                    action_type = capability.type
            req = run(post(f'https://api.iot.yandex.net/v1.0/groups/{self.id}/actions', headers={'Authorization': f'Bearer {self.__token}'}, json={'actions': [{'type': action_type, 'state': {'instance': __name, 'value': __value}}]}))
            if req['status'] == 'error':
                raise YandexHomeError(req['message'])
            if req['devices'][0]['capabilities'][0]['state']['action_result']['status'].lower() == 'error':
                raise YandexHomeError(req['devices'][0]['capabilities'][0]['state']['action_result']['error_code'])
            
    def __str__(self):
        return f'<Group avaible_properties={self.avaible_properties} id={self.id} name={self.name} household={self.household} aliases={self.aliases} type={self.type} state={self.state} devices={self.devices} capabilities={self.capabilities}>'
    
    def __repr__(self) -> str:
        return self.__str__()