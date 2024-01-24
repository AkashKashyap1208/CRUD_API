
from rest_framework.decorators import authentication_classes, permission_classes
# from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import *



class CustomeUserPostAndGet(APIView):
	permission_classes = ()
	authentication_classes=()

	

	def post(self,request):

		''' method will create a instance over the resource'''
		data = request.data
		serializer = UserCreteSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response({
				'message': "user Created",
				'status_code': 201
				}, 201)
		else:
			return Response({
				'message': "Not able to create super",
				'status_code': 400
				}, 400)


		

	def get(self,request):
		''' method to return all instances over resource '''
		user_objs = CustomUser.objects.all()
		serializer = UserCreteSerializer(user_objs, many=True)
		return Response({'status':200 , 'payload':serializer.data})


class CustomUserDetail(APIView):
	permission_classes = ()
	authentication_classes=()
	"""
	Retrieve, update or delete a snippet instance.
	"""
	def get_object(self, id):
		try:
			return CustomUser.objects.get(id=id)
		except CustomUser.DoesNotExist:
			raise Http404

	def get(self, request, id, format=None):
		user_objs = self.get_object(id)
		serializer = UserCreteSerializer(user_objs)
		return Response(serializer.data)

	def put(self, request, id, format=None):
		user_objs = self.get_object(id)
		serializer = UserUpdateSerializer(user_objs, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, id, format=None):
		user_objs = self.get_object(id)
		user_objs.delete()
		return Response({'message': "user deleted successfully",'status_code': 200})

class EmployeePostandGet(APIView):

	permission_classes = ()
	authentication_classes=()

	def post(self,request):
		data = request.data
		serializer = EmployeeCreateSerializer(data=data , context={'request':request})
		if serializer.is_valid():
			serializer.save()
			return Response({'message': "user Created", 'status_code': 201},201)
		else:
			return Response({'message': serializer.errors, 'status_code': 400},400)

	def get(self,request):
		user_objs = Employee.objects.all()
		serializer = EmployeeCreateSerializer(user_objs , many=True)
		return Response(serializer.data)


class EmployeeDetails(APIView):
	pass


























