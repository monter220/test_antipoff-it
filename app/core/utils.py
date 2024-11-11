from rosreestr2coord import Area


def check_cadastr_number(value):
    area = Area(value)
    if area.get_coord() == []:
        raise ValueError(f'Номер {value} does not exist')
