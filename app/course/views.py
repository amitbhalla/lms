from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser

from .models import Category
from .serializers import CategorySerializer


class CategoryListView(views.APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        json = JSONParser().parse(request)
        serializer = CategorySerializer(data=json)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
