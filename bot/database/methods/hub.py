from bot.database.methods import InsertDataBase, UpdateDataBase, GetDataBase, DelDataBase


class OperationHub:
    __operation: str

    def __init__(self, operation):
        self.operation = operation

    async def select(self):
        match self.operation:
            case "add":
                return InsertDataBase()
            case "update":
                return UpdateDataBase()
            case "delete":
                return DelDataBase()
            case "get":
                return GetDataBase()
