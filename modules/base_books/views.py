#for the front integrated with back
from django.shortcuts import render, redirect
from .models import BaseBook
from .forms import BaseBookRegister

#for the API
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BaseBookSerializer
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
#from .permissions import ApiUserPermissions


def postNewBaseBook(request):

	new_base_book = BaseBookRegister()
	if request.method == 'POST':
		new_base_book = BaseBookRegister(request.POST,request.FILES)
		if new_base_book.is_valid():

			base_book = BaseBook.objects.create(
				title = new_base_book.cleaned_data['title'],
				author = new_base_book.cleaned_data['author'],
				description = new_base_book.cleaned_data['description'],
				cover_image = new_base_book.cleaned_data['cover_image'],
				isbn = new_base_book.cleaned_data['isbn'],
				categories = new_base_book.cleaned_data['categories'],
				)

			base_book.save()

			return redirect('/')
	return render(request, 'base_books/new_base.html', {'new_base_book':new_base_book})



########################################################################################################
#API#
########################################################################################################
class ShowBaseBook(APIView):

	#permission_classes = (IsAuthenticated,)
	#authentication_classes = (JSONWebTokenAuthentication,)

	def get_object(self,pk):
		try:
			return BaseBook.objects.get(pk=pk)
		except BaseBook.DoesNotExist:
			raise Http404

	def get(self,request,pk,format=None):
		base_book = self.get_object(pk)
		serializer = BaseBookSerializer(base_book, context={"request": request})
		return Response(serializer.data)

	def put(self,request,pk,format=None):
		base_book = self.get_object(pk)
		serializer = BaseBookSerializer(base_book,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

	def delete(self,request,pk,format=None):
		base_book = self.get_object(pk)
		base_book.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


class ListAllBaseBooks(APIView):
	#permission_classes = (ApiUserPermissions,)
	#authentication_classes = (JSONWebTokenAuthentication,)

	def get(self,request):
		base_books = BaseBook.objects.all()
		serializer = BaseBookSerializer(base_books, many=True)
		return Response(serializer.data)

	def post(self,request):
		serializer = BaseBookSerializer(data= request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)