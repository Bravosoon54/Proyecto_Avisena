from pydantic import BaseModel, Field
from typing import Optional

class LandBase(BaseModel):
    nombre: str = Field(min_length=3, max_length=30)
    longitud: float
    latitud: float
    estado: bool

class LandCreate(LandBase):
    pass

class LandUpdate(BaseModel):    
    nombre: Optional [str] = Field(default=None, min_length=3, max_length=30)
    longitud: Optional [float] = None
    latitud: Optional [float] = None
    estado: Optional [bool] = None

class LandEstado(BaseModel):
    estado: Optional[bool] = None

class LandOut(LandBase):
    id_finca: int
    # nombre_usuario: str
