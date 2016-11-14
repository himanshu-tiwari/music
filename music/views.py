from django.shortcuts import render
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
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
		
class AlbumUpdate(UpdateView):
	"""docstring for AlbumUpdate"""
	model = Album
	fields = ['artist', 'album_title', 'genre', 'album_logo']
		
class AlbumDelete(DeleteView):
	"""docstring for AlbumDelete"""
	model = Album
	success_url = reverse_lazy('music:index')		
