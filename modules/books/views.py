from django.shortcuts import render, redirect
from .models import Book
from modules.users.models import User
from .forms import BookRegister
from .functions import getBookData

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
	return render(request,'books/profile.html',{'book':book})
	#return redirect('/')
