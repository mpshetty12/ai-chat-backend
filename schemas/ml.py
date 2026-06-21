from pydantic import BaseModel

class churnpredict(BaseModel):
    age: int
    usage: int
    support_calls: int
