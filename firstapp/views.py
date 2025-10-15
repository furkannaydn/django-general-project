from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


course_dictonary = {
    'python': 'This is Python Course',
    'java': 'This is Java Course',
    'kotlin': 'This is Kotlin Course',
    'swift': 'This is Swift Course'


}



def index(request):
    return HttpResponse("Hello, world. You're at the firstapp index.")

def course(request, item):
    return HttpResponse(course_dictonary.get(item, "This course is not available"))

def multiply_view(request, a, b):
    return HttpResponse(f"The product is {a * b}")