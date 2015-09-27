from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from .models import Titles

class TitleForm(ModelForm):
	"""
	Form to submit new title
	"""
	class Meta:
		model = Titles
		fields = ['name']