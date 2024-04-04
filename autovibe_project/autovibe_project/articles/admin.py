from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'slug')
    prepopulated_fields = {'slug': ('name',)}