from pydantic import BaseModel


from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: int
    name: str
    position: Optional[str]
    company: str
