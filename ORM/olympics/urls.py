from django.urls import path

from olympics import views

urlpatterns = [
    path("sport/create", view=views.create_sport, name="create_sport"),
    path("sport/set/details", view=views.sport_image_upload, name="sport_image_upload"),
    path("convert", view=views.add_image_to_database, name="add_image_to_database"),
    path(
        "get/image", view=views.get_image_from_database, name="get_image_from_database"
    ),
]
