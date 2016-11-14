from django.shortcuts import render
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Album

# Create your views here.

class IndexView(generic.ListView):
	"""docstring for IndexView"""
	template_name = "music/index.html"
	context_object_name = "all_albums"

	def get_queryset(self):
		return Album.objects.all()

class DetailView(generic.DetailView):
	"""docstring for DetailView"""
	model = Album
	template_name = "music/detail.html"
				
class AlbumCreate(CreateView):
	"""docstring for AlbumCreate"""
	model = Album
	fields = ['artist', 'album_title', 'genre', 'album_logo']
		
