from django.urls import path

from homepage import views

urlpatterns = [
    path("", view=views.create_session, name="create_session"),
    path("last", view=views.last_created, name="last_created"),
]
