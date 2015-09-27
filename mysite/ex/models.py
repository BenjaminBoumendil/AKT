from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
import uuid

class Gallery(models.Model):
	"""
	Models for Artwork
	"""
	name = models.CharField(_('name'), max_length=255)
	image = models.ImageField(_('image'), upload_to='ex/gallery', blank=True)

	def __unicode__(self):
		return self.name

class Titles(models.Model):
	"""
	Models for Titles
	"""
	id = models.UUIDField(_('id'), primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(_('Title'), max_length=255, blank=True)
	vote = models.IntegerField(_('vote'), default=0)
	ressource = models.ForeignKey(Gallery, unique=False, blank=True)
	user = models.ForeignKey(User, unique=False, blank=True)

	def __unicode__(self):
		return self.name