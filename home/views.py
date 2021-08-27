from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    #return HttpResponse("This is my homepage(/)")
    context = {'name': 'Manish', 'course': 'Django'}
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def intro(request):
    return render(request, 'intro.html')

def edu(request):
    return render(request, 'education.html')

def exp(request):
    return render(request, 'experience.html')

def contact(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        #print(name, email, phone, desc)
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        print("The data has been written to the DB")

    return render(request, 'contact.html')