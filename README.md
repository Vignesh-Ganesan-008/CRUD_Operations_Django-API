# CRUD_Operations_Django-API

<h3>A simple RESTful API using django to demonstrate CRUD operations.</h3> 

urlpatterns = [<br>
    path("",views.home,name="home"), <b>//HOME</b><br>
    path('all-cars/',views.all_cars,name="all_cars"), <b>//GET</b><br>
    path("create-car/",views.post_car,name="post_car"), <b>//PUT</b><br>
    path('retrive-car/<str:car_name>/',views.get_car,name="get_car"), <b>//GET</b><br>
    path('update-car/<str:car_name>/',views.put_car,name="update_car"), <b>//UPDATE</b><br>
    path('delete-car/<str:car_name>/',views.delete_car,name="delete_car"), <b>//DELETE</b><br>
]<br>
