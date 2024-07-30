from django.shortcuts import render

from database.models import product

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.


@api_view(["POST"])  # we specify which REST method this api will use.
def create_session(request):
    if request.method == "POST":

        try:
            name = request.data["name"]
            description = request.data["description"]
            product.objects.create(
                name=name,
                description=description,
                price=request.data["price"],
            )
            request.session["last_created"] = name
            return Response(
                "Data recieved by backend successfully", status=status.HTTP_200_OK
            )
        except Exception as ex:
            print(ex)
            return Response("Something went worng", status=status.HTTP_400_BAD_REQUEST)


@api_view(["GEt"])
def last_created(request):
    if request.method == "GET":

        try:
            name = request.session["last_created"]
            return Response(name, status=status.HTTP_200_OK)
        except Exception as ex:
            print(ex)
            return Response("Something went worng", status=status.HTTP_400_BAD_REQUEST)
