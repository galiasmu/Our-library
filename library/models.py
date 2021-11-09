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

class Book(models.Model):
    tittle = models.TextField(null=False, max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Author')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category')
    description = models.TextField(null=False, max_length=1000)
    stock = models.BigIntegerField()
    availability = models.ForeignKey(Availability, on_delete=models.CASCADE, verbose_name='Availability')
    stateBook = models.ForeignKey(StateBook, on_delete=models.CASCADE, verbose_name='StateBook')
    dateOfPublication = models.DateField('DateOfPublication', auto_now=False, auto_now_add=True)
    editorial = models.TextField(null=False, max_length=255)
    codeBook = models.BigIntegerField()


class Donation(models.Model):
    donor = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name='donor')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Book donor')
    state = models.ForeignKey(StateBook, on_delete=models.CASCADE, verbose_name='StateBook')


class Client(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name='Person')
    id = models.TextField(null=False, max_length=6)


class Loan(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Client')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Book')
    dateLoan = models.DateField('DateLoan', auto_now=False, auto_now_add=True)
    returnDate = models.DateField('ReturnLoan', auto_now=False, auto_now_add=False, null=True, blank=True)
    observation = models.ForeignKey(StateBook, on_delete=models.CASCADE, verbose_name='StateBook')

