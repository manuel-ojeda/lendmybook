from django.shortcuts import render

#for the front integrated with back
from django.shortcuts import render, redirect
from .models import Event
from modules.users.models import User
from modules.books.models import Book


#for the API
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EventSerializer
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class EventDetail(APIView):

	#permission_classes = (IsAuthenticated,)
	#authentication_classes = (JSONWebTokenAuthentication,)

	def get_object(self,pk):
		try:
			return Event.objects.get(pk=pk)
		except EventPreferences.DoesNotExist:
			raise Http404

	def get(self,request,pk,format=None):
		event = self.get_object(pk)
		serializer = EventSerializer(event, context={"request": request})
		return Response(serializer.data)

	def put(self,request,pk,format=None):
		event = self.get_object(pk)
		serializer = EventSerializer(event,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

	def delete(self,request,pk,format=None):
		event = self.get_object(pk)
		event.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class NewEvent(APIView):

	def post(self, request):
		serializer = EventSerializer(data= request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		