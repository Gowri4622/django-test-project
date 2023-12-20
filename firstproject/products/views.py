from django.shortcuts import render
from .models import Product
from .serializer import ProductSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.generics import GenericAPIView,ListAPIView
from rest_framework.mixins import ListModelMixin
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth.models import User
from .serializer import UserSerializer
from rest_framework import permissions
from rest_framework import generics
from .permission import IsOwnerOrReadOnly




#Generic view
class ProductList(generics.ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        
        return User.objects.filter(id=self.request.user.id)

    def perform_create(self, serializer):
        user = User.objects.get(id=self.request.user.id)
        serializer.save(owner=user)
	

class ProductListAPI(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]  

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        # Associate the updated product with the authenticated user
        serializer.save(owner=self.request.user)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProductAPIList(APIView):
	def get(self,request):
		all_hostel=User.objects.all()
		serializers=UserSerializer(all_hostel, many=True)
		return Response(serializers.data)




# # Function Based View
# @api_view(['GET','POST','DELETE'])
# def product_api(request):
# 	if(request.method == 'GET'):
# 		productz=Product.objects.all()
# 		serializer = ProductSerializer(productz, many=True)
# 		return Response(serializer.data)

# 	if(request.method == 'POST'):
# 		data=request.data
# 		serializer = ProductSerializer(data = data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			res = {'msg':'Dta has been created Successfully'}
# 			return Response(res)
# 		return Response({'msg':serializer.errors})

# 	if(request.method == 'DELETE'):
# 		products=request.data																																									
# 		id = products.get('id')
# 		products=Product.objects.get(id=id)
# 		products.delete()
# 		res = {'msg':'Student deleted successfully'}
# 		return Response(res)



# # Serializer

# def product_details(request):
# 	product=Product.objects.get(id = 2)
# 	serializer=ProductSerializer(product)
# 	json_data=JSONRenderer().render(serializer.data)
# 	return HttpResponse(json_data, content_type='application/json')


# # Class Based View
# class ProductAPIList(APIView):

# 	permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
	
	

# 	def get(self,request):
# 		products=Product.objects.all()
# 		serializers=ProductSerializer(products, many=True)
# 		return Response(serializers.data)

# 	def post(self,request):
# 		data=request.data
# 		serializers=ProductSerializer(data=data)
# 		if serializers.is_valid():
# 			serializers.save()
# 			res = {'msg':'Data has been created successfully'}
# 			return Response(res)
# 		return Response({'msg':serializers.errors})

	


# class ProductDetails(APIView):

# 	permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

# 	def get_object(self, pk):
# 		try:
# 			return Product.objects.get(pk=pk)
# 		except Product.DoesNotExist:
# 			raise Http404	
	
# 	def get(self, request, pk, format=None):
# 		snippet = self.get_object(pk)
# 		serializer=ProductSerializer(snippet)
# 		return Response(serializer.data)

# 	def put(self, request, pk, format=None):
# 		snippet = self.get_object(pk)
# 		serializer = ProductSerializer(snippet, data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 	def delete(self, request, pk, format=None):
# 		snippet = self.get_object(pk)
# 		snippet.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)
