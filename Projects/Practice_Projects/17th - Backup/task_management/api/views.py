from rest_framework.response import Response
from rest_framework.views import APIView
from .models import YourModel
from .serializers import YourModelSerializer

class YourModelListView(APIView):
    def get(self, request):
        queryset = YourModel.objects.all()
        serializer = YourModelSerializer(queryset, many=True)
        return Response(serializer.data)
