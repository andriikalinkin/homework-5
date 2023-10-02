from django.shortcuts import render
from django.http import HttpResponse
from faker import Faker


fake = Faker()


def index(request):
    return HttpResponse("<h1>Homework-5 index page</h1>")


def generate_teachers(request):
    return HttpResponse("<h1>`generate_teachers` page</h1>")
