from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from .model import Record

class CreateUserForm(UserCreationForm):

    class Meta:
        model=User
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


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='hotel_bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_booking_date', models.DateTimeField()),
                ('hotel_date_arrive', models.DateTimeField()),
                ('hotel_date_leave', models.DateTimeField()),
                ('hotel_adults', models.IntegerField(default=0)),
                ('hotel_children', models.IntegerField(default=0)),
                ('hotel_total_cost', models.FloatField(default=0)),
            ],
        ),
    ]
