from rest_framework import views
from rest_framework.response import Response

from .models import Category
from .serializers import CategorySerializer


class CategoryListView(views.APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
