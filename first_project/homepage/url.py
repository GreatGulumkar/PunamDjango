from django.urls import path

from homepage import views


urlpatterns = [
    path("", view=views.show_homepage, name="show_homepage"),
]
