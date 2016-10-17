from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm, LoginForm
from .models import User
from .functions import LogIn

def index(request):
	return render(request, 'profile.html')

def profile(request):
	if request.user.is_authenticated():

		user = User.objects.get(id=request.user.id_user)
		return render(request, 'users/profile.html', {'user':user})
	else:
		return redirect('/')

def edit(request):
	if request.method == "POST":
		if request.user.is_authenticated():

			user = User.objects.get(id=request.user.id_user)
			user.username = request.POST["username"]
			user.first_name = request.POST["fist_name"]
			user.last_name = request.POST["last_name"]
			user.email = request.POST["email"]
			user.birth_date = request.POST["birth_date"]
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
					username = user_register.cleaned_data['username'],
					first_name = user_register.cleaned_data['first_name'],
					last_name = user_register.cleaned_data['last_name'],
					email = user_register.cleaned_data['email'],
					password = user_register.cleaned_data['password'],
					birth_date = user_register.cleaned_data['birth_date'],
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
				user = authenticate(
					login_form.cleaned_data['username'], 
					login_form.cleaned_data['password'],
				)
				if user is not None:
					login(request, user)
					return redirect('/')
				
	else:
		user_register = UserRegisterForm()
		login_form = LoginForm()
	return render(request, 'users/login.html', {'user_register': user_register, 'login_form': login_form})

def userlogout(request):
	logout(request)

	return redirect('/')