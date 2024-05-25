from flask import Flask, request
from threading import Thread
from base64 import b64encode
from aiohttp import ClientSession
from .device import Device
from .scenario import Scenario
from .group import Group
from .room import Room
from .household import Household
from typing import Any
import webbrowser

class ClientDataInvalid(BaseException): pass
class YandexHomeError(BaseException): pass

app = Flask(__name__)
server = Thread(target=app.run, args=('localhost', 5030))
pclient_id = None
pclient_secret = None

class YandexHome:
    def __init__(self, token: str = None, *, client_id: str = None, client_secret: str = None) -> None:
        if not token and client_id and client_secret:
            global pclient_id
            global pclient_secret
            pclient_id = client_id
            pclient_secret = client_secret
            self.get_token()
        elif (not token and not client_id and client_secret) or (not token and client_id and not client_secret) or (not token and not client_id and not client_secret):
            raise ClientDataInvalid("Отсутствуют client_id и client_secret для получения токена!")
        self.token = token
        self.headers = {'Authorization': f'Bearer {self.token}'}

    def get_token(self):
        webbrowser.open('https://oauth.yandex.ru/authorize?response_type=code&client_id=d347a18dfe8d40e6ba4ffa3eb1026415')
        server.start()
        server.join()

    async def __get_user(self):
        async with ClientSession() as session:
            async with session.get('https://api.iot.yandex.net/v1.0/user/info', headers=self.headers) as req:
                json = await req.json()
                if json['status'] == 'ok':
                    return json
                else:
                    raise YandexHomeError(json['message'])
                
    async def get_user(self):
        json = await self.__get_user()
        if json['status'] == 'ok':
            rooms = []
            groups = []
            devices = []
            scenarios = []
            households = []

            for household in json['households']:
                households.append(Household(household['id'], household['name'], household['type']))
            groups = await self.get_groups(json)
            devices = await self.get_devices(json)
            for room in json['rooms']:
                room_devices = []
                for device in room['devices']:
                    room_devices.append(await self.get_device(device, cached_devices=devices))
                for house in households:
                    if house.id == room['household_id']:
                        room = Room(room['id'], room['name'], room_devices, house)
                        break
                rooms.append(room)
            scenarios = await self.get_scenarios(json)
            
            json['rooms'] = rooms
            json['groups'] = groups
            json['devices'] = devices
            json['scenarios'] = scenarios
            json['households'] = households
            return json
        else:
            raise YandexHomeError(json['message'])

    async def get_devices(self, cached_user: dict = None):
        if cached_user:
            user_data = cached_user
        else:
            user_data = await self.__get_user()
        devices = []
        for device_ud in user_data['devices']:
            groups = []
            device_household = None
            for group in device_ud['groups']:
                groups.append(await self.get_group(group))
            for household in user_data['households']:
                if household['id'] == device_ud['household_id']:
                    device_household = Household(household['id'], household['name'], household['type'])
            device = Device(device_ud['id'], device_ud['name'], device_ud['aliases'], device_ud['room'], device_ud['external_id'], device_ud['skill_id'], device_ud['type'], groups, device_ud['capabilities'], device_ud['properties'], device_household, self.token)
            devices.append(device)
        return devices
                
    async def get_groups(self, cached_user: dict = None):
        if cached_user:
            user_data = cached_user
        else:
            user_data = await self.__get_user()
        groups = []
        for group_ud in user_data['groups']:
            async with ClientSession() as session:
                async with session.get(f'https://api.iot.yandex.net/v1.0/groups/{group_ud["id"]}', headers=self.headers) as req:
                    group = await req.json()
                    for household in user_data['households']:
                        if household['id'] == group_ud['household_id']:
                            group = Group(group['id'], group['name'], group['aliases'], group['type'], group['state'], group['devices'], Household(household['id'], household['name'], household['type']), self.token)
                            groups.append(group)
                            break
        return groups
    
    async def get_group(self, id: str = None, *, name: str = None):
        if name or id:
            if id != None:
                async with ClientSession() as session:
                    async with session.get(f'https://api.iot.yandex.net/v1.0/groups/{id}', headers=self.headers) as req:
                        group = await req.json()
                        group = Group(group['id'], group['name'], group['aliases'], group['type'], group['state'], group['devices'], None, self.token)
                        return group
            if name != None:
                groups = []
                user_data = await self.get_groups()
                for group in user_data:
                    if group.name.lower() == name.lower() or name.lower() in [alias.lower() for alias in group.aliases]:
                        groups.append(group)
            if len(groups) > 0:
                if len(groups) == 1:
                    return groups[0]
                else:
                    return groups
            else:
                raise YandexHomeError("Группы с таким именем не найдены!")
        else:
            raise YandexHomeError('Не указан ни id, ни name.')

    async def get_scenarios(self, cached_user: dict = None):
        if cached_user:
            user_data = cached_user
        else:
            user_data = await self.__get_user()
        scenarios = []
        for scenario in user_data['scenarios']:
            scenarios.append(Scenario(scenario['id'], scenario['name'], scenario['is_active'], self.token))
        return scenarios
    
    async def get_scenario(self, id: str = None, *, name: str = None):
        user_data = await self.get_scenarios()
        if name or id:
            scenarios = []
            for scenario in user_data:
                if id != None:
                    if scenario.id == id:
                        return scenario
                if name != None:
                    if scenario.name.lower() == name.lower():
                        scenarios.append(scenario)
            if len(scenarios) > 0:
                if len(scenarios) == 1:
                    return scenarios[0]
                else:
                    return scenarios
            else:
                raise YandexHomeError("Сценарии с таким именем не найдены!")
        else:
            raise YandexHomeError('Не указан ни id, ни name.')
                
    async def get_device(self, id: str = None, *, name: str = None, cached_devices: list = None):
        if cached_devices:
            devices = cached_devices
        else:
            devices = await self.get_devices()
        if id:
            for device in devices:
                device: Device
                if device.id == id:
                    return device
        if name:
            founded_devices = []
            for device in devices:
                device: Device
                if name.lower() == device.name.lower() or name.lower() in [x.lower() for x in device.aliases]:
                    founded_devices.append(await self.get_device(device.id))
            if len(founded_devices) > 0:
                if len(founded_devices) == 1:
                    return founded_devices[0]
                else:
                    return founded_devices
            else:
                raise YandexHomeError("Устройства с таким именем не найдены!")
        raise YandexHomeError('Не указан ни id, ни name.')


            
    async def action(self, device: Device, actionType: str, instance: str, value: Any):
        async with ClientSession() as session:
            async with session.post(f'https://api.iot.yandex.net/v1.0/devices/actions', headers=self.headers, json={'devices': [{'id': device.id, 'actions': [{'type': actionType, 'state': {'instance': instance, 'value': value}}]}]}) as req:
                json = await req.json()
                if json['status'] == 'ok':
                    return json
                else:
                    raise YandexHomeError(json['message'])

@app.route('/')
async def yandex_callback():
    if pclient_id and pclient_secret:
        code = request.args.get('code')
        auth = f"{pclient_id}:{pclient_secret}"
        auth_bytes = auth.encode('ascii')
        base64_bytes = b64encode(auth_bytes)
        base64_auth = base64_bytes.decode('ascii')
        async with ClientSession() as session:
            async with session.post('https://oauth.yandex.ru/token', headers={'Authorization': f'Basic {base64_auth}'}, data={'grant_type': 'authorization_code', 'code': code}) as req:
                json = await req.json()
                token = json['access_token']
                return f'Твой токен: {token}'
            