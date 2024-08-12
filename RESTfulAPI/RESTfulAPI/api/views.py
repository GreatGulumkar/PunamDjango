# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# models

from database.models import product

# serializers

from django.core.serializers import serialize


@api_view(["POST"])  # we specify which REST method this api will use.
def create_product(request):
    if request.method == "POST":

        # if price and description and name:
        #     return Response("Data recieved by backend successfully",status=status.HTTP_200_OK)
        #     # return HttpResponse/JSONresponse/render/redirct

        try:
            name = request.data["name"]
            description = request.data["description"]
            product.objects.create(
                name=name,
                description=description,
                price=request.data["price"],
            )

            return Response(
                "Data recieved by backend successfully", status=status.HTTP_200_OK
            )
        except:
            return Response("Something went worng", status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])  # we specify which REST method this api will use.
def get_all_product(request):
    if request.method == "GET":

        queryset = product.objects.all()

        serial = serialize("json", queryset)
        return HttpResponse(serial)


@api_view(["GET"])
def count_products(request):
    if request.method == "GET":
        count = product.objects.count()

        return HttpResponse(count)


@api_view(["POST"])
def delete_products(request):
    """
    body = {
    "name": "Gaming Keyboard"
    }
    """
    if request.method == "POST":
        try:
            product.objects.filter(name=request.data["name"]).delete()

            return Response("Product delete successfully", status=status.HTTP_200_OK)
        except:
            return Response("Something went worng", status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])  # we specify which REST method this api will use.
def get_product(request, pk):
    if request.method == "GET":

        queryset = product.objects.filter(pk=pk)

        serial = serialize("json", queryset)
        return HttpResponse(serial)
