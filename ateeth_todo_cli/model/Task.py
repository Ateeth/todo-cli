class Task:
    description: str
    status: str
    id: int
    
    def __init__(self, desc, id):
        self.description = desc
        self.id = id
        self.status = "Todo"

    def to_dict(self):
        return {
            "description": self.description,
            "id": self.id,
            "status": self.status
        }
