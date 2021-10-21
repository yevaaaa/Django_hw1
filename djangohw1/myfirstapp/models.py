from django.db import models

# Create your models here.

"""
DJANGO HW 1
Deadline: OCT 18, 20:00
"""


"""
Problem 1

What option should I add in a field if I want to allow null values in that column?
Bring an example.
"""
# class Car(models.Model):
#     brand = models.CharField(max_length=15, null=True)
#     model = models.CharField(max_length=10, null=True)

"""
Problem 2

What options should I add in a field if I want to allow the user not to insert anything but I dont want that field to be null so I give it a default value.
Bring an example.
"""
# class Car(models.Model):
    # brand = models.CharField(max_length=15, blank=True, default='kia')
    # model = models.CharField(max_length=10, blank=True, default='sportage')

"""
Problem 3

If I created two new apps (user and car) what should I add in INSTALLED_APPS list of settings.py?
"""

'user.apps.UserConfig'
'car.apps.CarConfig'

"""
Problem 4

After changes were made in the models.py what commands I should run to syncronize the db with the new changes?
"""
# python manage.py migrate myfirstapp

"""
Problem 5

Imagine you have to create a table for university students. The field 'student_year' should be either Freshman, Sophomore, Junior or Senior. 
Make the model class. (Student can also have name, surname and major).
"""
# my_choices = [
#     ('one', 'Freshman'),
#     ('two', 'Sophomore'),
#     ('three', 'Junior'),
#     ('four', 'Senior')
# ]
#
#
# class Students(models.Model):
#     student_year = models.CharField(max_length=10, choices=my_choices)
#     name = models.CharField(max_length=15)
#     surname = models.CharField(max_length=20)
#     major = models.CharField(max_length=100)

"""
Problem 6

Create a Person and Address classes. Each person can have only one address but there can be more than one person who can have the same address.
Address has fields street, house, city and person. Person has fields first_name and last_name.
Create 2 person objects. Then create 2 address objects for those 2 person objects where the street, house, city are the same. (Do this in shell and paste your commands here.)
"""

class Person(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=20)


class Address(models.Model):
    street = models.CharField(max_length=89)
    house = models.IntegerField(max_length=4)
    city = models.CharField(max_length=30)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)


# >>> p1 = Person.objects.create(first_name='bob', last_name='bobyan')
# >>> p2 = Person.objects.create(first_name='bobuhi', last_name='bobyan')
# >>> from myfirstapp.models import Address
# >>> Address.objects.create(street='abcdef', house=1, city='milan', person=p1)
# <Address: Address object (1)>
# >>> Address.objects.create(street='abcdef', house=1, city='milan', person=p2)
# <Address: Address object (2)>
