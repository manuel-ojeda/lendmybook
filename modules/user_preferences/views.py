from django.shortcuts import render, redirect
from modules.users.models import User
from .forms import BookRegister

def setPreferences(request):

	new_preferences = Preferences()
	if request.method == 'POST':
		new_preferences = Preferences(request.POST,request.FILES)
		if new_preferences.is_valid():

			preferences = Book.objects.create(
				zones = new_preferences.cleaned_data['zones'],
				fav_categories = new_preferences.cleaned_data['fav_categories'],
				)

			user = User.objects.get(pk=request.user.id)

			user.user_preferences = preferences
			user.save()
			return redirect('user_preferences/preferences/?=created=OK')
	return render(request, 'user_preferences/new.html', {'new_preferences':new_preferences})

	#return redirect('/')

def viewPreferences(request):
	#if request.user.is_authenticated():
	book = Book.objects.get(id=request.user.book.id)
	return render(request,'books/login.html',{'book':book})
	#return redirect('/')

def reviewUser(request):

	new_preferences = Preferences()
	if request.method == 'POST':
		new_preferences = Preferences(request.POST,request.FILES)
		if new_preferences.is_valid():

			preferences = Book.objects.create(
				review = new_preferences.cleaned_data['review'],
				)

			user = User.objects.get(pk=request.user.id)

			user.user_preferences = preferences
			user.save()
			return redirect('user_preferences/preferences/?=edited=OK')
	return render(request, 'user_preferences/review.html', {'new_preferences':new_preferences})
