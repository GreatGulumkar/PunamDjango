from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError

from .models import Books

# from django.core.serializers import serialize

from .serializer import Books_serializer


@api_view(["GET"])
def all_books(request):
    if request.method == "GET":

        try:
            queryset = Books.objects.all()

            serializer = Books_serializer(queryset, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            print(ex)
            return Response("Something went worng", status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def create_books(request):
    if request.method == "POST":

        try:

            name = request.data["name"]
            Auther = request.data["Auther"]
            publication_date = request.data["publication_date"]
            edition = request.data["edition"]

            queryset = Books.objects.create(
                name=name,
                Auther=Auther,
                publication_date=publication_date,
                edition=edition,
            )

            temp = Books_serializer(queryset)
            temp.validate_edition(edition)

            return Response(f"Book {name} created", status=status.HTTP_200_OK)

        except ValidationError:
            queryset.delete()
            return Response(
                "Edition cannot be less on 1", status=status.HTTP_406_NOT_ACCEPTABLE
            )

        except Exception as ex:
            print(ex)
            return Response("Something went worng", status=status.HTTP_400_BAD_REQUEST)
