from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class client(models.Model):
	name = models.CharField(max_length = 45)
	telephone = models.CharField(max_length = 20)
	address = models.CharField(max_length = 45)

	def __str__(self):
		return '%s' % (self.name)


class project(models.Model):
	percent = models.IntegerField()
	project_date = models.DateField(auto_now_add = True)
	client_id = models.ForeignKey(client, on_delete = models.CASCADE)
	product_owner = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'owner')
	scrum_master = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'master')

	def __str__(self):
		return '%s %s %s' % (self.percent, self.product_owner, self.scrum_master)


class requirement(models.Model):
	title = models.CharField(max_length = 45)
	start_date = models.DateField()
	end_date = models.DateField()
	hours = models.IntegerField()
	project_id = models.ForeignKey(project, on_delete = models.CASCADE)

	def __str__(self):
		return '%s %s %s' % (self.title, self.start_date, self.end_date)


class homework(models.Model):
	percent = models.IntegerField()
	state_choices = (
		('Not Started', 'Not Started'),
		('In Progress', 'In Progress'),
		('Completed', 'Completed'),
		)
	state = models.CharField(
		max_length = 12,
		choices = state_choices,
		default = 'Not Started',
		)
	hours = models.IntegerField()
	requirement_id = models.ForeignKey(requirement, on_delete = models.CASCADE)
	user_id_in_charge = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'in_charge')
	user_id_supervisor = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'supervisor')

	def __str__(self):
		return '%s %s %s' % (self.percent, self.state, self.hours)


class mistakes(models.Model):
	mistake_type = models.CharField(max_length = 45)
	mistake_title = models.CharField(max_length = 45)
	comment = models.TextField()
	state_choices = (
		('Not Solved', 'Not Solved'),
		('In Progress', 'In Progress'),
		('Reviewed', 'Reviewed'),
		)
	state = models.CharField(
		max_length = 12,
		choices = state_choices,
		default = 'Not Solved',
		)
	qualification = models.IntegerField()
	homework_id = models.ForeignKey(homework, on_delete = models.CASCADE)

	def __str__(self):
		return '%s %s %s %s' % (self.mistake_type, self.mistake_title, self.comment, self.state)


class comments(models.Model):
	comment = models.TextField()
	homework_id = models.ForeignKey(homework, on_delete = models.CASCADE)

	def __str__(self):
		return '%s' % (self.comment)


class rol(models.Model):
	rol_choices = (
		('Scrum Master', 'Scrum Master'),
		('Product Owner', 'Product Owner'),
		('Team', 'Team'),
		)
	rol = models.CharField(
		max_length = 15,
		choices = rol_choices,
		default = 'Team',
		)
	user_id = models.ForeignKey(User, on_delete = models.CASCADE)

	def __str__(self):
		return '%s %s' % (self.rol, self.user_id)