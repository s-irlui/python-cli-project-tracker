class BaseModel:
    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return str(self.__dict__)