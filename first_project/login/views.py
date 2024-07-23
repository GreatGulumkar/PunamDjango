from django.shortcuts import render, redirect

# Create your views here.


from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponse

# models
from database.models import UserProfile
from django.contrib.auth.models import User

# authenticate, logout and login
from django.contrib.auth import authenticate, login, logout


@csrf_exempt
def user_register(request):
    return render(request, "register.html")


@csrf_exempt
def user_login(request):
    return render(request, "login.html")


@csrf_exempt
def user_create(request):
    if request.method == "POST":
        # UserProfile.objects.create = {
        #     "username": request.POST["email"],
        #     "email": request.POST["email"],
        #     "password": request.POST["password"],
        # }

        User.objects.create_user(
            username=request.POST["email"],
            email=request.POST["email"],
            password=request.POST["password"],
        )

    print("User created successfully")
    return render(request, "login.html")


@csrf_exempt
def check_user_login(request):
    if request.method == "POST":

        user = authenticate(
            username=request.POST["email"], password=request.POST["password"]
        )
        if user is None:
            # Display an error message if authentication fails (invalid password)
            print("invalid password")
            return redirect("/login/")
        else:
            # Log in the user and redirect to the home page upon successful login
            print("User logged in")
            login(request, user)
            data = {"user": request.POST["email"]}

            # return render(request, "index.html", data)
            return JsonResponse(data)


def user_logout(request):
    logout(request)
    print("user logged out")
    return redirect("/", {"logout": True})
