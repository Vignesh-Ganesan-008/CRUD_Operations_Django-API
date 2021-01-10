from django.http import HttpResponse
import json
from .models import Car

# Create your views here.
def home(request):
    response = json.dumps([{}])
    return HttpResponse(response,content_type = 'text/json')

def get_car(request,car_name):
    if request.method == "GET":
        try:
            car = Car.objects.get(name=car_name)
            response = json.dumps([{"Name":car.name, "Speed":car.speed}])
        except:
            response = json.dumps([{"Error":"No car found"}])
        return HttpResponse(response,content_type="text/json")

def post_car(request):
    if request.method == "POST":
        payload = json.loads(request.body)
        car_name = payload["car_name"]
        speed = payload["speed"]
        car = Car(name=car_name,speed=speed)
        try:
            car.save()
            response = json.dumps([{"Success":"Car added"}])
        except:
             response = json.dumps([{"Error":"Car NOT added"}])
        return HttpResponse(response,content_type="json/text")