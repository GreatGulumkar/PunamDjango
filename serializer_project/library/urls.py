from django.urls import path

from library import views

urlpatterns = [
    path("", view=views.all_books, name="all_books"),
    path("create", view=views.create_books, name="create_books"),
]
