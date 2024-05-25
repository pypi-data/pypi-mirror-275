from .household import Household
from datetime import datetime
from typing import Any
from aiohttp import ClientSession
from asyncio import run

async def post(url, headers, json):
    async with ClientSession() as session:
        async with session.post(url, headers=headers, json=json) as req:
            return await req.json()

class YandexHomeError(BaseException): pass

class Property:
    def __init__(self, retrievable: bool, property_type: str, parameters: dict, state: dict, last_updated: datetime, reportable: bool = None):
        self.retrievable = retrievable
        self.property_type = property_type
        self.parameters = parameters
        self.state = state
        self.last_updated = last_updated
        self.instance=self.parameters['instance']
        self.reportable = reportable
        if state != None:
            self.__setattr__(self.parameters['instance'], self.state['value'])
        if 'unit' in self.parameters:
            self.__setattr__(f'{self.parameters["instance"]}_unit', self.parameters['unit'])

    def __str__(self):
        inst = 'instance'
        if self.state != None:
            return f'<Property retrievable={self.retrievable} type={self.property_type} instance={self.instance} {self.parameters["instance"]}={self.__getattribute__(self.parameters["instance"])} {self.parameters["instance"]}_unit={self.__getattribute__(f"{self.parameters[inst]}_unit")} last_updated={self.last_updated} reportable={self.reportable}>'
        else:
            return f'<Property retrievable={self.retrievable} type={self.property_type} instance={self.instance} last_updated={self.last_updated} reportable={self.reportable}>'
        
    def __repr__(self) -> str:
        return self.__str__()
    
class Capability:
    def __init__(self, retrievable: bool, capability_type: str, parameters: dict, state: dict, last_updated: datetime, reportable: bool = None):
        self.retrievable = retrievable
        self.type = capability_type
        self.parameters = parameters
        self.state = state
        self.last_updated = last_updated
        self.reportable = reportable
        self.instance = self.state['instance']
        self.__setattr__(self.state['instance'], self.state['value'])

    def __str__(self):
        return f'<Capability retrievable={self.retrievable} type={self.type} parameters={self.parameters} {self.state["instance"]}={self.state["value"]} last_updated={self.last_updated} reportable={self.reportable}>'
    
    def __repr__(self) -> str:
        return self.__str__()

class Device:
    def __init__(self, id: str, name: str, aliases: list[str], room: str, external_id: str, skill_id: str, device_type: str, groups: list, capabilities: list[dict], properties: list[dict], household: Household, token: str):
        self.__attr = ['id', 'name', 'aliases', 'room', 'external_id', 'skill_id', 'type', 'groups', 'household', '_Device__token', 'avaible_properties', '_Device__capabilities', '_Device__properties']
        self.id = id
        self.name = name
        self.aliases = aliases
        self.room = room
        self.external_id = external_id
        self.skill_id = skill_id
        self.type = device_type
        self.groups = groups
        self.__token = token
        self.__capabilities = capabilities
        self.__properties = properties
        self.household = household
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
            req = run(post(f'https://api.iot.yandex.net/v1.0/devices/actions', headers={'Authorization': f'Bearer {self.__token}'}, json={'devices': [{'id': self.id, 'actions': [{'type': action_type, 'state': {'instance': __name, 'value': __value}}]}]}))
            if req['status'] == 'error':
                raise YandexHomeError(req['message'])
            if req['devices'][0]['capabilities'][0]['state']['action_result']['status'].lower() == 'error':
                raise YandexHomeError(req['devices'][0]['capabilities'][0]['state']['action_result']['error_code'])

    def __str__(self) -> str:
        try:
            if self.groups != None:
                return f'<Device id={self.id} name={self.name} avaible_properties={self.avaible_properties} aliases={self.aliases} room={self.room} external_id={self.external_id} skill_id={self.skill_id} type={self.type} groups={self.groups} capabilities={self.capabilities} properties={self.properties} household={self.household}>'
        except:
            return f'<Device id={self.id} name={self.name} avaible_properties={self.avaible_properties} aliases={self.aliases} room={self.room} external_id={self.external_id} skill_id={self.skill_id} type={self.type} capabilities={self.capabilities} properties={self.properties} household={self.household}>'
    
    def __repr__(self) -> str:
        return self.__str__()
    
    @property
    def properties(self):
        return [Property(property_dict['retrievable'], property_dict['type'], property_dict['parameters'], property_dict['state'], datetime.fromtimestamp(property_dict['last_updated']), property_dict.get('reportable', None)) for property_dict in self.__properties]
    
    @property
    def capabilities(self):
        return [Capability(capability_dict['retrievable'], capability_dict['type'], capability_dict['parameters'], capability_dict['state'], datetime.fromtimestamp(capability_dict['last_updated']), capability_dict.get('reportable', None)) for capability_dict in self.__capabilities]

    async def delete(self):
        async with ClientSession() as session:
            async with session.delete(f'https://api.iot.yandex.net/v1.0/devices/{self.id}', headers={'Authorization': f'Bearer {self.__token}'}) as req:
                json = await req.json()
                if json['status'] == 'error':
                    raise YandexHomeError(json['message'])