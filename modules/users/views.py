from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .forms import UserRegisterForm
from .models import User
from .functions import LogIn
from .serializers import UserSerializer


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
			user.id_facebook = reques.POST["id_facebook"]
			user.name = request.POST["name"]
			user.email = request.POST["email"]
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
					id_facebook = user_register.cleaned_data['id_facebook'],
					name = user_register.cleaned_data['name'],
					email = user_register.cleaned_data['email'],
				)

				LogIn(
					request,
					id_facebook = user_register.cleaned_data['id_facebook'],
				)

				return redirect('/')
		if 'login_form' in request.POST:
			login_form = LoginForm(request.POST)

			if login_form.is_valid():
				user = authenticate(
					id_facebook = user_register.cleaned_data['id_facebook'],
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

class SignUp(APIView):

	def post(self,request):

		serializer = UserSerializer(data= request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(status=status.HTTP_201_CREATED)
		return Response(status=status.HTTP_400_BAD_REQUEST)




class LogIn(APIView):
	def get_object(self,request):
		try:
			facebook = request.data["id_facebook"]
			return User.objects.get(facebook=id_facebook)
		except User.DoesNotExist:
			raise Http404

	def post(self,request):
		current_user = self.get_object(request)
		serializer = UserSerializer(current_user)
		return Response(serializer.data,status=status.HTTP_200_OK)