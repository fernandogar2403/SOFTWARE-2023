from car import car
from account import account
from uberX import uberX
from user import user

if _name_   == "_main_":
    print("Inicializando las info de los carros" )
    print("Car")
    car = car("AMS256", Account("Andres Herrera", "ADS12365", "andres@platzi.com", "2563"))
    print(vars(car))
    print(vars(car.driver))

    print(UberX)
    uberX = uberX("KLO365", Account("Marco Lois", "SGHJ1236", "marco@platzi.com", "7856"), "Toyota", "Corolla")
    print(vars(uberX))
    print(vars(uberX.driver))

    print("User")
    user = User("Mariana Valle", "SDFG125F", "mariana@platzi.com", "7856")
    print(vars(user))