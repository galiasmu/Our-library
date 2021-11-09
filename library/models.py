from django.db import models


class Category(models.Model):
    category = models.TextField(max_length=255)


class Availability(models.Model):
    availability = models.BooleanField(default=True)


class StateBook(models.Model):
    stateBook = models.TextField(max_length=50)


class Author(models.Model):
    name = models.TextField(max_length=100)
    lastName = models.TextField(max_length=100)
    pseudonym = models.TextField(max_length=100)
    nationality = models.TextField(max_length=255)


class Rol(models.Model):
    rol = models.TextField(max_length=100)


class Person(models.Model):
    name = models.TextField(max_length=100)
    lastName = models.TextField(max_length=100)
    birthDate = models.TextField(max_length=100)
    dni = models.BigIntegerField()
    phone = models.BigIntegerField()
    email = models.TextField(max_length=255)


class User(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name='Person')
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, verbose_name='Rol')
