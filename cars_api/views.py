from django.http import HttpResponse
import json
from .models import Car
from django.core import serializers

# Create your views here.
def home(request):
    response = json.dumps([{}])
    return HttpResponse(response,content_type = 'text/json')

def all_cars(request):
    if request.method == "GET":
        try:
            cars = Car.objects.all()
            allCars = []
            for car in cars:
                allCars.append({"name" : car.name,"speed" : car.speed})
            response = json.dumps(allCars)
        except:
            response = json.dumps([{"Error":"No cars found"}])
        return HttpResponse(response,content_type="text/json")    

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

def put_car(request,car_name):
    if request.method == "PUT":
        payload = json.loads(request.body)
        speed = payload["speed"]
        try:
            car = Car.objects.get(name=car_name)
            car.speed = speed
            car.save()
            response = json.dumps([{"Success":"Car Updated"}])
        except:
             response = json.dumps([{"Error":"Car NOT Updated/Found"}])
        return HttpResponse(response,content_type="json/text")

def delete_car(request,car_name):
    if request.method == "DELETE":
        try:
            car = Car.objects.get(name=car_name)
            car.delete()
            response = json.dumps([{"Error":"Car Deleted"}])
        except:
            response = json.dumps([{"Error":"No car Deleted/Found"}])
        return HttpResponse(response,content_type="text/json")