from datetime import datetime, timezone, timedelta

start_message = '''Я расскажу о текущей погоде для населенного пункта.

Я могу ответить на:
- Текстовое сообщение с названием населенного пункта.
- Голосовое сообщение с названием населенного пункта.
- Сообщение с геопозицией.'''


error_text = '''Я не могу ответить на такой тип сообщения.
Но могу ответить на:
- Текстовое сообщение с названием населенного пункта.
- Голосовое сообщение с названием населенного пункта.
- Сообщение с геопозицией.'''


def not_found_place(message: str):
    return f'Я не нашел населенный пункт "{message}".'


def result_message_text(weather):
    return f'''{weather["weather"][0]["description"]}.
Температура {(weather["main"]["temp"])} ℃, ощущается как {(weather["main"]["feels_like"])} ℃.
Атмосферное давление {(weather["main"]["pressure"])} мм рт. ст.
Влажность {(weather["main"]["humidity"])} %.
Видимость {(weather["visibility"])} метров.
Ветер {(weather["wind"]["speed"])} м/с {__wind_direction(weather["wind"]["deg"])}.
Восход солнца {__format_time(weather['sys']['sunrise'], weather['timezone'])} МСК. Закат {__format_time(weather['sys']['sunset'], weather['timezone'])} МСК.'''


def result_message_voice(weather):
    return f'''Населенный пункт {weather["name"]}.
{weather["weather"][0]["description"]}.
Температура {round(weather["main"]["temp"])} градусов цельсия.
Ощущается как {round(weather["main"]["feels_like"])} градусов цельсия.
Давление {round(weather["main"]["pressure"])} миллиметров ртутного столба.
Влажность {round(weather["main"]["humidity"])} процентов.'''


def __wind_direction(deg):
    if deg is None:
        return None
    directions = ["С", "СВ", "В", "ЮВ", "Ю", "ЮЗ", "З", "СЗ"]
    idx = round(deg / 45) % 8
    return directions[idx]


def __format_time(unix_time, tz_offset):
    utc_time = datetime.fromtimestamp(unix_time, timezone.utc)
    local_time = utc_time + timedelta(seconds=tz_offset)
    return local_time.strftime("%H:%M")
