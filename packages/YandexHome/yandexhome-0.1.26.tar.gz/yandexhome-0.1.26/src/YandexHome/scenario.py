from aiohttp import ClientSession

class YandexHomeError(BaseException): pass

class Scenario:
    def __init__(self, id: str, name: str, is_active: bool, token: str) -> None:
        self.id = id
        self.name = name
        self.is_active = is_active
        self.__token = token

    async def start(self):
        if self.is_active:
            async with ClientSession() as session:
                async with session.post(f'https://api.iot.yandex.net/v1.0/scenarios/{self.id}/actions', headers={'Authorization': f'Bearer {self.__token}'}) as req:
                    json = await req.json()
                    if json['status'] == 'error':
                        raise YandexHomeError(json['message'])
                    
    def __str__(self) -> str:
        return f'<Scenario id={self.id} name={self.name} is_active={self.is_active}>'
    
    def __repr__(self) -> str:
        return self.__str__()