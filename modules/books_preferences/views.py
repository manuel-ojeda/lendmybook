#for the front integrated with back
from django.shortcuts import render, redirect
from .models import BookPreferences
#from .forms import BaseBookRegister

#for the API
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookPreferencesSerializer
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
#from .permissions import ApiUserPermissions

"""
def UserBookPreferences(request):

	book_preferences = BaseBookRegister()
	if request.method == 'POST':
		book_preferences = BaseBookRegister(request.POST,request.FILES)
		if book_preferences.is_valid():

			book_preferences = BookPreferences.objects.create(
				title = book_preferences.cleaned_data['title'],
				author = book_preferences.cleaned_data['author'],
				description = book_preferences.cleaned_data['description'],
				cover_image = book_preferences.cleaned_data['cover_image'],
				isbn = book_preferences.cleaned_data['isbn'],
				categories = book_preferences.cleaned_data['categories'],
				)

			book_preferences.save()

			return redirect('/')
	return render(request, 'book_preferencess/new_base.html', {'book_preferences':book_preferences})
"""


########################################################################################################
#API#
########################################################################################################
class BookPreferencesDetail(APIView):

	#permission_classes = (IsAuthenticated,)
	#authentication_classes = (JSONWebTokenAuthentication,)

	def get_object(self,pk):
		try:
			return BookPreferences.objects.get(pk=pk)
		except BookPreferences.DoesNotExist:
			raise Http404

	def get(self,request,pk,format=None):
		book_preferences = self.get_object(pk)
		serializer = BookPreferencesSerializer(book_preferences, context={"request": request})
		return Response(serializer.data)

	def put(self,request,pk,format=None):
		book_preferences = self.get_object(pk)
		serializer = BookPreferencesSerializer(book_preferences,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

	def delete(self,request,pk,format=None):
		book_preferences = self.get_object(pk)
		book_preferences.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)