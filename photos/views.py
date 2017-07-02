from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Photo
from django.utils import timezone
from .forms import PhotoForm
# Create your views here.

def hello(request):
	photos = Photo.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
	return render(request, 'photos/photos.html',	 {'photos': photos})

def detail(request, pk):
	photo = Photo.objects.get(id=pk)
	#msg = (
	#	
     #   '<p>주소는 {url}</p>'.format(url=photo.image.url),
     #   '<p><img src="{url}" /></p>'.format(url=photo.image.url),
     #   )
	#return HttpResponse(msg)
	#photo = Photo.objects.filter(id=pk)
	return render(request, 'photos/detail.html',	 {'photo': photo})

def upload(request):
	if request.method == "GET":
		form = PhotoForm()
	elif request.method == "POST":
		form = PhotoForm(request.POST, request.FILES)

		if form.is_valid():
			obj = form.save()
			return redirect(obj)

	ctx = {
	'form' : form,
	}
	return render(request, 'photos/upload.html', ctx)
	