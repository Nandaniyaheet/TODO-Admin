from django.contrib import admin
from .models import TodoModel
# Register your models here.
admin.site.register(TodoModel)
list_display = ('title', 'description', 'last_modified', 'completed')