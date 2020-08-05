from django.contrib import admin

# Register your models here.
from .models import Post
from sorl.thumbnail.admin import AdminImageMixin


@admin.register(Post)
class PostAdmin(AdminImageMixin, admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
