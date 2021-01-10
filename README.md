# CRUD_Operations_Django-API

urlpatterns = [
    path("",views.home,name="home"), <b>//HOME<b>
    path('all-cars/',views.all_cars,name="all_cars"), <b>//GET<b>
    path("create-car/",views.post_car,name="post_car"), <b>//PUT<b>
    path('retrive-car/<str:car_name>/',views.get_car,name="get_car"), <b>//GET<b>
    path('update-car/<str:car_name>/',views.put_car,name="update_car"), <b>//UPDATE<b>
    path('delete-car/<str:car_name>/',views.delete_car,name="delete_car"), <b>//DELETE<b>
]
