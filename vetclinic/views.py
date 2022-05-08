from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import vet
from .serializers import vetSerializers
from django.core.exceptions import ObjectDoesNotExist

class ItemCollection(APIView):

    def get(self,request):
        model=vet.objects.all()
        serializer=vetSerializers(model,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = vetSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ItemDetail(APIView):

    def get(self,request,vetID):
        try:
            model=vet.objects.get(vetID=vetID)
        except ObjectDoesNotExist:
            return Response({"Message":"Item does not exist"},status.HTTP_404_NOT_FOUND)
        serializer = vetSerializers(model)
        return Response(serializer.data)

    def delete(self,request,vetID):
        try:
            model=vet.objects.get(vetID=vetID)
        except ObjectDoesNotExist:
            return Response({"Message":"Item does not exist"},status.HTTP_404_NOT_FOUND)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self,request,vetID):
        try:
            model = vet.objects.get(vetID=vetID)
        except ObjectDoesNotExist:
            return Response({"Message":"Item does not exist"}, status.HTTP_404_NOT_FOUND)
        serializer = vetSerializers(model,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

def home(request):
    # Home page
    return HttpResponse('<h2>This is vet & clinic service home page</h2>')
