from django.shortcuts import render, redirect
from .models import BaseBook
from .forms import BaseBookRegister


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
