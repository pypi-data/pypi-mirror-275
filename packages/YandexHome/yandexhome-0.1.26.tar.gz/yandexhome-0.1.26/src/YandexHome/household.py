class Household:
    def __init__(self, id: str, name: str, house_type: str) -> None:
        self.id = id
        self.name = name
        self.type = house_type

    def __str__(self) -> str:
        return f'<Household id={self.id} name={self.name} type={self.type}>'
    
    def __repr__(self) -> str:
        return self.__str__()