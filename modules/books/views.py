#For the front integrated with back
from django.shortcuts import render, redirect
from .models import Book
from modules.users.models import User
from modules.base_books.models import BaseBook
from .forms import BookRegister
from .functions import getBookData

#for the API
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookSerializer
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
#from .permissions import ApiUserPermissions

def postNewBookUser(request):

	new_book = BookRegister()
	if request.method == 'POST':
		new_book = BookRegister(request.POST,request.FILES)
		if new_book.is_valid():

			book = Book.objects.create(
				edition = new_book.cleaned_data['edition'],
				book_images = new_book.cleaned_data['book_images'],
				aditional_info = new_book.cleaned_data['aditional_info'],
				)

			user = User.objects.get(pk=request.user.id)

			user.book = book
			user.save()
			return redirect('/')
	return render(request, 'books/new.html', {'new_book':new_book})

	#return redirect('/')

def profile(request):
	#if request.user.is_authenticated():
	book = Book.objects.get(id=request.user.book.id)
	return render(request,'books/login.html',{'book':book})
	#return redirect('/')

def search(request):
	if request.method == "POST":
		title = request.POST['title']

		try:
			base_books = BaseBook.objects.all().filter(title__icontains=title)
		except BaseBook.DoesNotExist:
			base_books = None

		return render(request, 'books/search.html', {'base_books': base_books, 'title': title})
	return render(request, 'landing/index.html')

def list(request, base_book_id):
	if request.method == "GET":
		print('id_base_book')
		print(base_book_id)

		try:
			base_book = BaseBook.objects.filter(pk=base_book_id)
		except Book.DoesNotExist:
			base_book = None

		try:
			books = Book.objects.filter(base_book=base_book)
		except Book.DoesNotExist:
			books = None

		return render(request, 'books/list.html', {'books': books})
	return redirect('/')

def view(request, id_book):
	if request.method == "GET":
		try:
			book = Book.objects.get(id_book=id_book)
		except Book.DoesNotExist:
			book = None

		if book != None:
			try:
				owner = User.objects.get(id_user=book.owner)
			except User.DoesNotExist:
				owner = None
		else:
			owner = None

		return render(request, 'books/view.html', {'book': book, 'owner': owner})
	return render(request, 'books/view.html')

##########################################
				# API #
##########################################


class ShowBook(APIView):

	#permission_classes = (IsAuthenticated,)
	#authentication_classes = (JSONWebTokenAuthentication,)

	def get_object(self,pk):
		try:
			return Book.objects.get(pk=pk)
		except Book.DoesNotExist:
			raise Http404

	def get(self,request,pk,format=None):
		book = self.get_object(pk)
		serializer = BookSerializer(book)
		return Response(serializer.data)

	def put(self,request,pk,format=None):
		book = self.get_object(pk)
		serializer = BookSerializer(book,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

	def delete(self,request,pk,format=None):
		book = self.get_object(pk)
		book.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


class ListAllBooks(APIView):
	#permission_classes = (ApiUserPermissions,)
	#authentication_classes = (JSONWebTokenAuthentication,)

	def get(self,request):
		books = Book.objects.all()
		serializer = BookSerializer(books, many=True)
		return Response(serializer.data)

	def post(self,request):
		serializer = BookSerializer(data= request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookImage(APIView):
	#permission_classes = (ApiUserPermissions,)
	#authentication_classes = (JSONWebTokenAuthentication,)

	def get_object(self,pk):
		try:
			return Book.objects.get(pk=pk)
		except Book.DoesNotExist:
			raise Http404

	def get(self,request,pk,format=None):
		book = self.get_object(pk)
		serializer = BookSerializer(book)
		return Response(serializer.data)
