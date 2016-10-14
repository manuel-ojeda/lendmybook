from django.shortcuts import render, redirect
from .models import Book
from modules.users.models import User
from .forms import BookRegister

def postNewBook(request):

	new_book = BookRegister()
	if request.method == 'POST':
		new_book = BookRegister(request.POST,request.FILES)
		if new_book.is_valid():

			book = Book.objects.create(
				title = new_book.cleaned_data['title'],
				author = new_book.cleaned_data['author'],
				description = new_book.cleaned_data['description'],
				edition = new_book.cleaned_data['edition'],
				categories = new_book.cleaned_data['categories'],
				book_images = new_book.cleaned_data['book_images'],
				action_tags = new_book.cleaned_data['action_tags'],
				cover_image = new_book.cleaned_data['cover_image'],
				)

			user = User.objects.get(pk=request.user.id)

			user.book = book
			user.save()
			return redirect('books/postnew/?=created=OK')
	return render(request, 'books/new.html', {'new_book':new_book})

	#return redirect('/')

def profile(request):
	#if request.user.is_authenticated():
	book = Book.objects.get(id=request.user.book.id)
	return render(request,'books/profile.html',{'book':book})
	#return redirect('/')
