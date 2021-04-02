from django.contrib import admin
from .models import Categoria, Post
# Register your models here.


class CategotiaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')


admin.site.register(Categoria, CategotiaAdmin)
admin.site.register(Post, PostAdmin)