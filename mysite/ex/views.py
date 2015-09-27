from django import template
from django.views.generic import ListView
from django.views.generic.edit import FormMixin

from .models import Gallery, Titles
from .forms import TitleForm

register = template.Library()

class FormListView(ListView, FormMixin):
	"""
	Mixing FormView with ListView to submit new title
	"""
	def post(self, request, *args, **kwargs):
		title_form = TitleForm(request.POST)
		if "voteup" in request.POST:
			self.voteup(request.POST.get('voteup'))
		elif title_form.is_valid():
			return self.form_valid(title_form)
		return self.get(request, *args, **kwargs)

class ArtworkListView(FormListView):
	"""
	ListView for Artwork
	"""
	template_name = 'ex/artwork.html'
	model = Gallery
	form_class = TitleForm
	success_url = '/'

	def voteup(self, ressource_id):
		ressource = Titles.objects.get(id=ressource_id)
		ressource.vote += 1
		ressource.save()

	def get_titles(self):
		return list(Titles.objects.order_by('-vote'))

	def get_context_data(self, **kwargs):
		context = super(ArtworkListView, self).get_context_data(**kwargs) 
		context['form'] = self.get_form()
		return context

	def form_valid(self, form):
		form = form.save(commit=False)
		form.user = self.request.user
		form.ressource = Gallery.objects.get(name=self.request.POST.get("wichressource"))
		form.save()
		return super(ArtworkListView, self).form_valid(form)