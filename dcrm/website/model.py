from django.db import models

# Create your models here.
class Record(models.Model):

    creation_data = models.DateTimeField(auto_now_add= True)

    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 255)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)


    def __str__(self):
        return self.first_name + " " + self.last_name

class hotel_bookings(models.Model):

    hotel_booking_date = models.DateTimeField()
    hotel_date_arrive = models.DateTimeField()
    hotel_date_leave = models.DateTimeField()
    hotel_adults = models.IntegerField(default=0)
    hotel_children = models.IntegerField(default=0)
    hotel_total_cost = models.FloatField(default=0)
    
