from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
  list_display = ('task', 'is_completed', 'updated_at')
  search_fields=('task',)
  
  #this class and list_display and other attribue we did is to modify the admin panel to shoe above field details in front in admin table
  #http://127.0.0.1:8000/admin/todo/task/ <- check here

admin.site.register(Task, TaskAdmin) 

