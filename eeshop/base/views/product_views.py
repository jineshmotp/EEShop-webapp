from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import  IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger

from base.models import Product,Platform_data
from base.serializers import ProductSerializer


from rest_framework import status



## Product Serializer

@api_view(['GET'])
def getProducts(request):
    query = request.query_params.get('keyword')
    print('query:',query)
    if query == None:
        query = ''

    products = Product.objects.filter(name__icontains=query)
    
    paginator = Paginator(products, 2)
    page = request.query_params.get('page')
  
  

    # try:
    #     products = paginator.get_page(page)
    # except PageNotAnInteger:
    #     products = Paginator.get_page(1)
    # except EmptyPage:
    #     products = Paginator.get_page(paginator.num_pages)

    # if page == None:
    #     page = 1
    
    # page = int(page)


    serializers = ProductSerializer(products, many=True)
    # return Response({'products:':serializers.data,'page':page,'pages':paginator.num_pages})
    return Response(serializers.data)

@api_view(['GET'])
def getTopProducts(request):
    products = Product.objects.all().order_by('name')[0:3]
    serializers = ProductSerializer(products, many=True)    
    return Response(serializers.data)



@api_view(['GET'])
def getProduct(request,pk):
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

###  Product Create uby admin

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createProduct(request):
    user = request.user
    product = Product.objects.create(
        user= user,
        name='Sample Name',        
        brand='Sample brand',
        category='Sample Text',
        description='Test description'

    )    
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)  

### Product Update by admin

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateProduct(request,pk):
    data = request.data
    product = Product.objects.get(_id=pk)

    product.name = data['name']
    product.brand = data['brand']
    product.category = data['category']
    product.description = data['description']

    product.save()    

    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

### Product Delete by admin 

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteProduct(request,pk):
    product = Product.objects.get(_id=pk)
    product.delete()
    return Response('Product Deleted')


@api_view(['POST'])

def uploadImage(request):
    data = request.data

    product_id = data['product_id']
    product = Product.objects.get(_id=product_id)

    product.image = request.FILES.get('image')
    product.save()
    return Response('Image uploaded !')

