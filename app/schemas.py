from datetime import datetime

from pydantic import BaseModel, Extra, validator

from core.utils import check_cadastr_number


class CadastrBD(BaseModel):
    cadastr_number: str
    latitude: float
    longitude: float

    @validator('cadastr_number')
    def cadastr_number_valid(cls, value):
        check_cadastr_number(value)
        return value

    @validator('latitude')
    def check_latitude(cls, value):
        if value < -180 or value > 180:
            raise ValueError(
                f'Значение {value} не попадает в диапазон (-180:180)')
        return value

    @validator('longitude')
    def check_longitude(cls, value):
        if value < -90 or value > 90:
            raise ValueError(
                f'Значение {value} не попадает в диапазон (-90:90)')
        return value


class CadastrCreate(CadastrBD):

    class Config:
        schema_extra = {
            'example': {
                'cadastr_number': '47:14:1203001:814',
                'latitude': 112.5,
                'longitude': 63.8,
            }
        }
        extra = Extra.forbid
        orm_mode = True


class CadastrGet(CadastrBD):
    id: int
    result: bool

    class Config:
        orm_mode = True


class HistoryDB(BaseModel):
    id: int
    endpoint: str
    type: str
    data: str
    date: datetime

    class Config:
        orm_mode = True
