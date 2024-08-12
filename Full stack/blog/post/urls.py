from django.urls import path

from .views import show_post, set_post

urlpatterns = [
    path("", view=show_post, name="show_post"),
    path("create", view=set_post, name="set_post"),
]
