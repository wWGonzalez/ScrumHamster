from django.shortcuts import render, redirect
from .models import client, project, requirement, homework, mistakes, comments, rol
from .forms import client_form, project_form, requirement_form, homework_form, mistakes_form, comments_form, rol_form
# Create your views here.


def index(request):
	return render(request, 'index.html')


# client
def list_client(request):
	data = client.objects.all()
	return render(request, 'client_list.html', {'data': data})


def create_client(request):
	if request.method == 'POST':
		form = client_form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('list_client')
	else:
		form = client_form()
		return render(request, 'client.html', {'form': form})
# end client


# project
def list_project(request):
	data = project.objects.all()
	return render(request, 'project_list.html', {'data': data})


def create_project(request):
	if request.method == 'POST':
		form = project_form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('list_project')
	else:
		form = project_form()
		return render(request, 'project.html', {'form': form})
# end project


# requirement
def list_requirement(request):
	data = requirement.objects.all()
	return render(request, 'requirement_list.html', {'data': data})


def create_requirement(request):
	if request.method == 'POST':
		form = requirement_form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('list_requirement')
	else:
		form = requirement_form()
		return render(request, 'requirement.html', {'form': form})
# end requirement


# homework
def list_homework(request):
	data = homework.objects.all()
	return render(request, 'homework_list.html', {'data': data})


def create_homework(request):
	if request.method == 'POST':
		form = homework_form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('list_homework')
	else:
		form = homework_form()
		return render(request, 'homework.html', {'form': form})
# end homework


# mistakes
def list_mistakes(request):
	data = mistakes.objects.all()
	return render(request, 'mistakes_list.html', {'data': data})


def create_mistakes(request):
	if request.method == 'POST':
		form = mistakes_form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('list_mistakes')
	else:
		form = mistakes_form()
		return render(request, 'mistakes.html', {'form': form})
# end mistakes


# comments
def list_comments(request):
	data = comments.objects.all()
	return render(request, 'comments_list.html', {'data': data})


def create_comments(request):
	if request.method == 'POST':
		form = comments_form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('list_comments')
	else:
		form = comments_form()
		return render(request, 'comments.html', {'form': form})
# end comments


# rol
def list_rol(request):
	data = rol.objects.all()
	return render(request, 'rol_list.html', {'data': data})


def create_rol(request):
	if request.method == 'POST':
		form = rol_form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('list_rol')
	else:
		form = rol_form()
		return render(request, 'rol.html', {'form': form})
# end rol