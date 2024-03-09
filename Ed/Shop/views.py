from django.shortcuts import render, redirect, HttpResponse
from .models import Users
from .forms import LoginForms

# Create your views here.
def index(req):
    return render(req, "Shop/index.html")

def login(req):
    forms = LoginForms()
    if req.POST:
        forms = LoginForms(req.POST)
        if forms.is_valid():
            email = forms.cleaned_data["email"]
            password = forms.cleaned_data["password"]
            users = Users.objects.values()
            for user in range(len([a for a in users])):
                if email == users[user]['email'] and password == users[user]['password']:
                    return HttpResponse("FOIIIIIIIIIIIII CARALHOOOOOOO")
            return HttpResponse("Login não autorizado")
        
    return render(req, "Shop/login.html", {
        "Forms": forms
    })

def singup(req):
    forms = LoginForms()
    if req.POST:
        forms = LoginForms(req.POST)
        if forms.is_valid():
            forms.save()
            return redirect(index)
    return render(req, "Shop/singup.html", {
        "Forms": forms
    })