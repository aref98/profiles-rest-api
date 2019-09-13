from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
	"""Test API View"""


	serializer_class = serializers.HelloSerializer

	def get(self, request, format=None):
		"""Returns a list of APIView featuers"""
		an_apiview=[
		   'Users HTTP method as function (get , post , patch, put , delete)',
		   'Is similar to a traditional Django view',
		   'Gives you  the most control over your application logic',
		   'Is mapped manually to URLs',
		]

		return Response({'message':'Hello','an_apiview':an_apiview})

	def post(self, request):
		"""Create a hello message with our name"""
		serializer = self.serializer_class(data=request.data)

		if serializer.is_valid():
			name = serializer.validated_data.get('name')
			message = f'Hello {name}!'
			return Response({'message': message})
		else:
			return Response(
				serializer.errors,
				status=status.HTTP_400_BAD_REQUEST
			)

	def put(self, request, pk=None):
		"""handle updating object"""
		return Response({'message':'method is PUT'})

	def patch(self, request, pk=None):
		"""handle a partial update of an  object"""
		return Response({'message':'method is PATCH'})

	def delete(self, request, pk=None):
		"""handle a delete request"""
		return Response({'message':'method is delete'})


class HelloViewSet(viewsets.ViewSet):
	"""Test api viewsets"""
	serializer_class=serializers.HelloSerializer
	def list(self,request):
		"""return hello message"""
		a_viewset = [
			'Uses actions (list  , creates,retrieve,update,partaial_update)',
			'automatically maps to urls using Routers',
			'Provides more functionality with less code'
		]

		return Response({'message':'hello!','a_viewset':a_viewset})

	def create(self, request):
		"""create a new hello message"""
		serializer = self.serializer_class(data=request.data)

		if serializer.is_valid():
			name = serializer.validated_data.get('name')
			message = f'hello {name}! from Mr.Aref'
			return Response({'message':message})
		else:
			return Response(
                serializer.errors,
				status=status.HTTP_400_BAD_REQUEST
			)

	def retrieve(self,request,pk=None):
		"""Handle getting an object by its Id"""
		return Response({'http_method': 'GET'})

	def update(self,request,pk=None):
		"""Handle updating an object"""
		return Response({'http method':'PUT'})

	def partial_update(self , request, pk=None):
		"""Handle updating part of an object"""
		return Response({'http_method':'PATCH'})

	def destroy(self ,request, pk=None):
		"""handle removing an object"""
		return Response({'http_method':'DELETE'})
