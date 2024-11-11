import random

from datetime import datetime
from sqlalchemy.orm import validates
from sqlalchemy import (
    Column,
    String,
    Float,
    DateTime,
    CheckConstraint,
    Boolean,
    Text,
)

from app.core.db import Base
from app.core.utils import check_cadastr_number



class Cadaster(Base):
    cadastr_number = Column(String(17), unique=False, nullable=False)
    latitude = Column(Float, unique=False, nullable=False)
    longitude = Column(Float, unique=False, nullable=False)
    result = Column(Boolean, default=bool(random.getrandbits(1)))

    __table_args__ = (
        CheckConstraint(
            'latitude <= 180.0 AND latitude >= -180.0',
            name='can be between -180 and 180'
        ),
        CheckConstraint(
            'longitude <= 90.0 AND longitude >= -90.0',
            name='can be between -90 and 90'
        )
    )

    @validates('cadastr_number')
    def validate_cadastr_number(self, key, cadastr_number):
        check_cadastr_number(cadastr_number)
        return cadastr_number


class History(Base):
    endpoint = Column(String(100))
    type = Column(String(100))
    data = Column(Text)
    date = Column(DateTime, default=datetime.now)
