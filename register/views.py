from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    return render(request, "register/register.html") 

def login(request):
    return render(request, "register/mine.html")

def myform(request):
    if request.method == "POST":
        user = UserCreationForm(request.POST)
        if user.is_valid():
            user.save()
            return redirect("/homepage/")
        else:
            print("not done")
    mylist = {
        "mine": UserCreationForm()
    }
    return render(request, "register/mine.html", mylist)

def logout(request):
    if request.method == "POST":
        user = UserCreationForm(request.POST)
        if user.is_valid():
            user.save()
            return redirect("/homepage/")
        else:
            print("not valid")

    list = {"myform": UserCreationForm()}
    return render(request, "register/logout.html", list)
