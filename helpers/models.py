
from pydantic import BaseModel

class InputData(BaseModel):
    Id: int
    SepalLengthCm: float 
    SepalWidthCm: float
    PetalLengthCm: float
    PetalWidthCm: float
