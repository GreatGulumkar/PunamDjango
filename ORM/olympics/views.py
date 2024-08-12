from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from django.core.serializers import serialize

from database.models import Sport, images

from .forms import ImageForm

from .serializers import SportSerializer


@api_view(["POST"])
def create_sport(request):
    if request.method == "POST":
        print(request.data["Name"])
        print(request.data["category"])


@api_view(["POST"])
def sport_image_upload(request):
    if request.method == "POST":

        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return Response({"message": "Image uploaded successfully"}, status=201)

        return Response(form.errors, status=400)


@api_view(["GET"])
def add_image_to_database(request):
    if request.method == "GET":

        image = open("media\cycling.png", "rb")

        image_data = image.read()

        images.objects.create(picture=image_data)

        return Response("All good")


@api_view(["GET"])
def get_image_from_database(request):
    if request.method == "GET":

        try:
            # Query the database for parking images based on the parking_id
            print(request.data["sport_id"])
            queryset = Sport.objects.filter(sport_id=request.data["sport_id"])

            # Serialize the data
            serializer = SportSerializer(queryset, many=True)

            # Return the serialized data as JSON response
            return Response(serializer.data, status=status.HTTP_200_OK)
        except queryset.DoesNotExist:
            # Handle the case where the parking ID does not exist
            return Response(
                {"message": "Parking ID does not exist"},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            # Handle other exceptions
            return Response(
                {"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
