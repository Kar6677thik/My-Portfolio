from django.shortcuts import render

def home(request):
    return render(request, "portApp/main.html")

def about(request):
    return render(request, 'portApp/about.html')

def projects(request):
    return render(request, 'portApp/projects.html')

def contact(request):
    return render(request, 'portApp/contact.html')



