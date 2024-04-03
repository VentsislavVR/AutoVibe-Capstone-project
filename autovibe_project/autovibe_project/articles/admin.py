from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'slug')  # Customize the displayed fields in the admin list view
    prepopulated_fields = {'slug': ('name',)}