from django.contrib.auth import authenticate, login


def LogIn(request, email, id_facebook):
	user = authenticate(
		username = email,
		password = id_facebook)

	if user is not None:
		login(request, user)