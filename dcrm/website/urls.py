from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=""),

    path('register', views.register, name="register"),

    path('my-login', views.my_login, name="my-login"),

    path('user-logout', views.user_logout, name="user-logout"),

    #View a single record

    path('record/<int:pk>', views.singular_record,name="record"),

    ################### C R U D ###################

    #Create
    path('create-record', views.create_record ,name="create-record"),

    #Read
    path('dashboard', views.dashboard, name="dashboard"),

    #Update
    path('update-record/<int:pk>', views.update_record, name="update-record"),

    #Delete
    path('delete-record/<int:pk>', views.delete_record, name="delete-record"),

    ################### MY URLS ########################


    path('history', views.history ,name="history"),

    path('booking', views.hotel,name="booking"),



  
    
   


]


