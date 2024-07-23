from django.urls import path

from login import views


urlpatterns = [
    path("register", view=views.user_register, name="user_register"),
    path("", view=views.user_login, name="user_login"),
    path("createuser", view=views.user_create, name="user_create"),
    path("checkuser", view=views.check_user_login, name="check_user_login"),
    path("logout", view=views.user_logout, name="user_logout"),
]
