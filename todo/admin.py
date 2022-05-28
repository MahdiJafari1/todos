from django.contrib import admin
from todo.models import List, Todo


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    pass

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    pass

