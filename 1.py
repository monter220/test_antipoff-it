from rosreestr2coord import Area

# Создание объекта Area с кадастровым номером участка
area = Area("47:14:1203001:814")
b = area.get_coord()
print(b)
# Преобразование данных в формат GeoJSON
# print(area.to_geojson())

# Получение геометрии в виде многоугольника
# print(area.to_geojson_poly())

# Получение координат
if area.get_coord() == []:
    print(f'Номер {area} does not exist')  # Возвращает список координат в формате [[[area1_xy], [hole1_xy], [hole2_xy]], [[area2_xyl]]]

# Получение дополнительных атрибутов участка
attributes = area.get_attrs()