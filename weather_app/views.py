from django.shortcuts import render 
# import json to load json data to python dictionary 
import json 
# urllib.request to make a request to api 
import urllib.request 
from .models import weather
from django.utils import timezone

  
def index(request): 
    if request.method == 'POST': 
        city = request.POST['city'] 
        ''' api key might be expired use your own api_key 
            place api_key in place of appid ="your_api_key_here "  '''
  
        # source contain JSON data from API 
  
        source = urllib.request.urlopen( 
            'http://api.openweathermap.org/data/2.5/weather?q='+city+ '&appid=a15bc10703f28b89ebe4e66776851d8b').read() 
  
        # converting JSON data to a dictionary 
        list_of_data = json.loads(source) 
  
        # data for variable list_of_data 
        data = { 
            "name": str(list_of_data['name']),
            "country_code": str(list_of_data['sys']['country']), 
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']), 
            "temp": str(round(float(list_of_data['main']['temp'])-273.15)) + '°C', 
            "pressure": str(list_of_data['main']['pressure']), 
            "humidity": str(list_of_data['main']['humidity']), 
            
        } 
        weatherdata = weather.objects.create(
            city=str(list_of_data['name']),
            country_code=str(list_of_data['sys']['country']), 
            coordinate=str(list_of_data['coord']['lon']) + ' '
                       + str(list_of_data['coord']['lat']), 
            temp=round(float(list_of_data['main']['temp'])-273.15), 
            pressure=list_of_data['main']['pressure'], 
            humidity=list_of_data['main']['humidity'],
            
        )
        
    else: 
        data={} 
    weather_data = weather.objects.all().order_by('-timestamp')
    return render(request, "index.html", {"data":data,"weather_data": weather_data}) 