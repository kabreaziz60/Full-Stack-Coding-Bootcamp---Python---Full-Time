# Create your views here.
from unicodedata import name
from django.shortcuts import render # this line is added automatically
from django.http import HttpResponse # pass view information into the browser


from .models import Person, Post    # import the models from polls/models.py

person = Person.objects.filter(first_name="Maria", last_name = "Fez").first() 
# get the first object because Person.objects.filter returns a QuerSet (ie. a list)



def index(request):
    context = {
        'page_title' : "Homepage",
        'user' : person
    }
    return render(request, 'posts/homepage.html', context)


def posts(request):
    context = {
        'user' : person,
# we retrieve the person variable (created outside of the function)
        'page_title' : "Posts",
        'posts' : Post.objects.filter(
            author__first_name=person.first_name, 
            author__last_name=person.last_name)
    }

    return render(request, 'posts/posts.html', context)


# from .forms import ContactForm

# def index(request):
#     context = {
#         'page_title' : "Homepage",
#         'user' : person,
#         'form' : ContactForm()
#     }
#     return render(request, 'posts/homepage.html', context)


from .forms import ContactForm

person = Person.objects.filter(first_name="Maria", last_name = "Fez").first()

def index(request):
    context = {
        'page_title' : "Homepage",
        'user' : person,
    }
    # if the submit button was clicked
    if request.method == 'POST':
        # POST, generate form with data from the request
        form = ContactForm(request.POST)
        # check if it's valid:
        if form.is_valid():
            # get the value of the fields
            form_name = form['name'].value
            form_email = form['email'].value
            form_comment = form['comment'].value
            context['formInfo'] = [form_name,form_email,form_comment]
            # render to a the same url, but with new data:
            return render(request, 'posts/homepage.html', context)
    else:
        # GET, generate blank form
        context['form'] = ContactForm()
    return render(request, 'posts/homepage.html', context)




from .models import Person, Post
from .forms import ContactForm

person = Person.objects.filter(first_name="Maria", last_name = "Fez").first()

def index(request):
    context = {
        'page_title' : "Homepage",
        'user' : person,
    }

    if request.method == 'POST':

        # POST, generate form with data from the request
        form = ContactForm(request.POST)
        # check if we get data
        print("data", form.data)
        # check if it's valid:
        if form.is_valid():
            form_name = form.cleaned_data['name']
            form_email = form.cleaned_data['email']
            form_comment = form.cleaned_data['comment']
            context['formInfo'] = {
                    'name' : form_name,
                    'email': form_email,
                    'comment': form_comment
                }
            context['btnFormHidden'] = True # To hide the button is the form is successfully submitted
            # print the values to make sure their are correct
            print(context['formInfo'])
            return render(request, 'posts/homepage.html', context)
        else:
             # print the errors, just in case
            print("---ERRORS---", form.errors)
            context['form'] = form
            return render(request, 'posts/homepage.html', context)

    else:
        # GET, generate blank form
        context['form'] = ContactForm()
    return render(request, 'posts/homepage.html', context)
