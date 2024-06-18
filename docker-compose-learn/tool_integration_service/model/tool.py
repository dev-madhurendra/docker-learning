from pydantic import BaseModel


from pydantic import BaseModel
from typing import Optional

class Tool(BaseModel):
    id: int
    name: str