from pydantic import BaseModel

from pydantic import BaseModel

class Employee(BaseModel):
    id: int
    name: str
    position: str
    company: str