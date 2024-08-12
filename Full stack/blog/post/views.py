from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

# from django.http import HttpResponse

from django.core.serializers import serialize

from database.models import BlogPost


@api_view(["GET"])
def show_post(request):
    if request.method == "GET":
        queryset = BlogPost.objects.all()

        serialized = serialize("json", queryset=queryset)

        return Response({"msg": serialized})


@api_view(["POST"])
def set_post(request):
    if request.method == "POST":

        try:
            BlogPost.objects.create(
                name=request.data["name"],
                content=request.data["content"],
            )

            return Response({"message": "Created"})
        except:
            return Response({"message": "Something went worng"})
