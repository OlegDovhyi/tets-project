from pyowm import OWM
 # ustanovka pip install pyowm
def pogoda_in_city():
        
    city = input('enter the name of the city, where you want to know the weather : ')
    owm = OWM('376128bcc10048c02162617c67d8bbfe') 
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place(city)
    w = observation.weather
    temperature = w.temperature('celsius')['temp']
    wind =  w.wind()['speed']
    status = w.detailed_status

    print (f'in the {city}, temperature is {temperature} *C, speed of  wind {wind} m/s, and now is "{status}" ')

