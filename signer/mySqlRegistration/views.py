from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url="/login")
def home(request):
    user = request.user

    return render(
        request,
        "mySqlRegistration/home.html",
        {
            "user": user,
            "full_name": user.get_full_name(),
            "creation_date": user.date_joined,
        },
    )


def signup(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("up")
        try:
            user = User.objects.create_user(
                username,
                email,
                password,
            )
            user.first_name = firstname
            user.last_name = lastname
            user.save()

            login(request, user=user)
            return HttpResponseRedirect("/")
        except Exception:
            print(Exception)
            return render(
                request,
                "mySqlRegistration/signup.html",
                {"message": "Signup failed, try another username."},
            )

    return render(request, "mySqlRegistration/signup.html", {})


def login_me(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user=user)
            return HttpResponseRedirect("/")
        else:
            return render(
                request, "mySqlRegistration/login.html", {"message": "Login failed!"}
            )
    return render(request, "mySqlRegistration/login.html", {})


def logut(request):
    logout(request)
    return render(request, "mySqlRegistration/logout.html", {})
