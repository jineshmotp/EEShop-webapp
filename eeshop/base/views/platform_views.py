from django.shortcuts import render
# import datetime
from datetime import datetime

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import  IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from base.models import Product,Platform_data
from base.serializers import PlatformsSerializer


from rest_framework import status

from datetime import datetime

now = datetime.now() # current date and time

year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")

date_time = now.strftime("%m/%d/%Y")
	

@api_view(['GET'])
def getPlatformdatas(request):
    platforms = Platform_data.objects.all()
    serializer_platforms = PlatformsSerializer(platforms, many=True)
    return Response(serializer_platforms.data)

@api_view(['GET'])
def getPlatformdata(request,platk):
    platform = Platform_data.objects.all().filter(product_id=platk)
    serializer_platform = PlatformsSerializer(platform, many=True)
    return Response(serializer_platform.data)

## Platform data get request from Admin

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getPlatformDetails(request,pk):
    platform = Platform_data.objects.get(_id=pk)
    serializer = PlatformsSerializer(platform, many=False)
    return Response(serializer.data)  



###  Platform Created by admin

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createPlatform(request,pk):
    user = request.user
    product = Product.objects.get(_id=pk)
    platform = Platform_data.objects.create(
        user= user,
        product_id = product,
        platform_name='Amazon',        
        price=0,
        countInStock=0,
        rating=0.0,
        numReviews=0,
        expected_date='',
        website_link='',

    )    
    serializer = PlatformsSerializer(platform, many=False)
    return Response(serializer.data)  

## Update Platform 

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updatePlatform(request,pk):
    data = request.data
    platform = Platform_data.objects.get(_id=pk)

    platform.platform_name = data['platform_name']
    platform.price = data['price']
    platform.countInStock = data['countInStock']
    platform.rating = data['rating']
    platform.numReviews = data['numReviews']
    platform.expected_date = data['expected_date'],
    platform.website_link = data['website_link']


    platform.save()    

    serializer = PlatformsSerializer(platform, many=False)
    return Response(serializer.data)


### Product Delete by admin 

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deletePlatform(request,pk):
    platform = Platform_data.objects.get(_id=pk)
    platform.delete()
    return Response('Platform Deleted')