from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from .models import Record, ZooUser
from .models import hotel_bookings
class CreateUserForm(UserCreationForm):

    class Meta:
        model=ZooUser
        fields=['username','password1','password2']

class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=TextInput())
    password=forms.CharField(widget=PasswordInput())

class CreateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name','last_name','email','phone','address','city']

class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name','last_name','email','phone','address','city']



from django.db import migrations, models

class Hotel_Booking_Form(forms.ModelForm):

    class Meta:
        model = hotel_bookings 

        fields = {'hotel_date_arrive', 'hotel_date_leave','hotel_adults','hotel_children',
                  'hotel_total_cost','hotel_points'}
        
        labels ={
            "hotel_booking_date_arrive": 'What Day do you wish to arrive',
        }

        widgets = {
            'hotel_date_arrive': forms.DateInput(attrs={'type':'date'}),
            'hotel_date_leave': forms.DateInput(attrs={'type':'date'}),
            'hotel_total_cost': forms.HiddenInput(),
            'hotel_points': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)


    

