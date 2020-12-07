# import pyowm
# from pyowm import OWM
#
# owm: OWM = pyowm.OWM('2ec5f7334b3ea215e38aaa2252e9e107')
#
# gorod = input ("Укажите город: ")
# owm = pyowm.OWM('a99967bc9ee70d5b4bd387902982f400')
# observation = owm.weather_at_place(city)
# w = observation.get_weather()
#
# print("В городе " + gorod+ " сейчас : " + w.get_detailed_status())
# print("Температура в городе " + gorod + " "  +str(temp))

from pyowm import OWM
from pyowm.utils.config import get_default_config

place = input(" Введите город/страну: ")

config_dict = get_default_config()
config_dict['language'] = 'ru'

owm = OWM( 'a99967bc9ee70d5b4bd387902982f400', config_dict  )

mgr = owm.weather_manager()
observation = mgr.weather_at_place(place)
w = observation.weather

print(w)