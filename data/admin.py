from django.contrib import admin
from .models import client, project, requirement, homework, mistakes, comments, rol
# Register your models here.
admin.site.register(client)
admin.site.register(project)
admin.site.register(requirement)
admin.site.register(homework)
admin.site.register(mistakes)
admin.site.register(comments)
admin.site.register(rol)