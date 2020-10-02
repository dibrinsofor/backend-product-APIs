from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import LocationSerializer
from .models import Locations
from .forms import ImageForm

# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def apiOverview(request):
    api_urls = {
        'List':'/locations-list/',
	'Detail View':'/locations-detail/<str:pk>/',
	'Create':'/locations-create/',
	'Update':'/locations-update/<str:pk>/',
	'Delete':'/locations-delete/<str:pk>/',
    }

    return Response(api_urls)
    
@api_view(['GET'])
def locationList(request):
    locations = Locations.objects.all()
    serializer = LocationSerializer(locations, many=True)
    return Response(serializer.data)

    
@api_view(['GET'])
def locationDetail(request, pk):
    locations = Locations.objects.get(id=pk)
    serializer = LocationSerializer(locations, many=False)
    return Response(serializer.data)

    
@api_view(['POST'])
def locationCreate(request):
    serializer = LocationSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def locationUpdate(request, pk):
    locationn = Locations.objects.get(id=pk)
    serializer = LocationSerializer(instance = locationn, data = request.data)

    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)

@api_view(['DELETE'])
def locationDelete(request, pk):
    locationn = Locations.objects.get(id=pk)
    locationn.delete()

    return Response("Alaye! the location has been deleted")

@api_view(['GET'])
def detailView(request):
    locationn =location.objects.get.all()
    return location

# def showimage(request):

#     lastimage= Image.objects.last()

#     imagefile= lastimage.imagefile


#     form= ImageForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         form.save()

    
#     context= {'imagefile': imagefile,
#               'form': form
#               }
    
      
#     return render(request, 'Blog/images.html', context)

