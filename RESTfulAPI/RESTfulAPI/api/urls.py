from django.urls import path

from api import views

urlpatterns = [
    path("create/", view=views.create_product, name="create_product"),
    path("products/", view=views.get_all_product, name="get_all_product"),
    path("count/", view=views.count_products, name="count_products"),
    path("delete/", view=views.delete_products, name="delete_products"),
    

]

