from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm, LoginForm
from .models import User
from .functions import LogIn

def index(request):
	return render(request, 'index.html')

def profile(request):
	if request.user.is_authenticated():

		user = User.objects.get(id=request.user.id)
		return render(request, 'users/profile.html', {'user':user})
	else:
		return redirect('/')

def edit(request):
	if request.method == "POST":
		if request.user.is_authenticated():

			user = User.objects.get(id=request.user.id)
			user.username = request.POST["username"]
			user.name = request.POST["name"]
			user.lastname = request.POST["lastname"]
			user.email = request.POST["email"]

			if request.POST["age"] != 'None':
				user.age = int(request.POST["age"])
			else:
				user.age = None

			user.save()

			return redirect('/profile/')
		return redirect('/')
	return redirect('/')

def userlogin(request):
	if request.method == "POST":
		user_register = UserRegisterForm()

		if 'register_form' in request.POST:
			user_register = UserRegisterForm(request.POST)

			if user_register.is_valid():
				User.objects.create_user(
					username= user_register.cleaned_data['username'],
					email = user_register.cleaned_data['email'],
					password = user_register.cleaned_data['password']
				)
				LogIn(
					request, 
					user_register.cleaned_data['username'], 
					user_register.cleaned_data['password']
				)

				return redirect('/')
		if 'login_form' in request.POST:
			login_form = LoginForm(request.POST)

			if login_form.is_valid():
				LogIn(
					request, 
					login_form.cleaned_data['username'], 
					login_form.cleaned_data['password']
				)
				return redirect('/')
				
	else:
		user_register = UserRegisterForm()
		login_form = LoginForm()
	return render(request, 'users/login.html', {'user_register': user_register, 'login_form': login_form})

def userlogout(request):
	logout(request)

	return redirect('/')