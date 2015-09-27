from django.shortcuts import render
from .forms import UserForm
from django.views.generic import FormView

class RegisterView(FormView):
	"""
	FormView for register new user
	"""
	template_name = 'register/register.html'
	form_class = UserForm
	success_url = '/'

	def post(self, request, *args, **kwargs):
		user_form = UserForm(request.POST)
		if user_form.is_valid():
			return self.form_valid(user_form)
		return self.get(request, *args, **kwargs)

	def form_valid(self, form):
		form.save()
		return super(RegisterView, self).form_valid(form)