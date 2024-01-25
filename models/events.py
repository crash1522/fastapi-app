from pydantic import BaseModel
from  typing import List

class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        scheme_extra = {
            "example" : {
                "title": "FastAPI sample",
                "image": "image",
                "description": "this is sample",
                "tags": ["python", "fastAPI"],
                "location": "Google",
            }
        }