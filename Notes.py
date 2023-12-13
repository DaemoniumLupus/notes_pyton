import datetime

class Notes():
    heading: str
    text: str
    date: datetime
    id: int

    def __init__(self, count:int) -> None:
        self.date = datetime.datetime.today()
        self.id = count
        
