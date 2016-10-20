from django.contrib.auth import authenticate, login


def LogIn(request, password):
	pass
	user = authenticate(
		username = username,
		password = password)

	if user is not None:
		login(request, user)