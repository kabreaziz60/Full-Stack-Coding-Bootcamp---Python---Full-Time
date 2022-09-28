# Create your views here.
from unicodedata import name
from django.shortcuts import render # this line is added automatically
from django.http import HttpResponse # pass view information into the browser

# takes a request, returns a response

# Modifier 
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
# def liste(request) :
#     return HttpResponse("<h1>Ceci est la liste </h1><br><ul><li>Poll 1</li><li>Poll 2</li><li>Poll 3</li></ul> ")

# def index(request):

#     user = {
#         'first_name' : "John",
#         'last_name' : "Doe",
#         'site': "Developper Institut"
#     } 

#     subjects = [
#         {
#             'title' : "How to setup Django",
#             'author': "Maria"
#         },
#         {
#             'title' : "How to cake an amazing pie",
#             'author' : "Chef Mark"
#         },
#         {
#             'title' : "To day we learnent flask framwork",
#             'author' : "Mr LENGANI"
#         }
#     ]

#     context = {
#         'user' : user,
#         'subjects': subjects,
#     }
#     return render(request, 'posts/homepage.html', context)


# suite 


# from django.shortcuts import render

user = {
    'first_name' : "John",
    'last_name' : "Doe"
} 

# index function renders homepage.html template
def index(request):
    context = {
        'page_title' : "Homepage",
        'user' : user,
    }
    return render(request, 'posts/homepage.html', context)

# posts function renders posts.html template
def posts(request):
    subjects = [
        {
            'title' : "How to setup Django",
            'author': "Maria"
        },
        {
            'title' : "How to cake an amazing pie",
            'author' : "Chef Mark"
        }
    ]

    context = {
        'page_title' : "Posts",
        'user' : user,
        'subjects': subjects
    }

    return render(request, 'posts/posts.html', context)