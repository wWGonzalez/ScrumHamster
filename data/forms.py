from django import forms
from .models import client, project, requirement, homework, mistakes, comments, rol

class client_form(forms.ModelForm):
	class Meta:
		model = client
		fields = '__all__'


class project_form(forms.ModelForm):
	class Meta:
		model = project
		fields = '__all__'


class requirement_form(forms.ModelForm):
	class Meta:
		model = requirement
		fields = '__all__'


class homework_form(forms.ModelForm):
	class Meta:
		model = homework
		fields = '__all__'


class mistakes_form(forms.ModelForm):
	class Meta:
		model = mistakes
		fields = '__all__'


class comments_form(forms.ModelForm):
	class Meta:
		model = comments
		fields = '__all__'


class rol_form(forms.ModelForm):
	class Meta:
		model = rol
		fields = '__all__'