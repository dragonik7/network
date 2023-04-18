from django.contrib import admin

from post.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('uuid', 'title', 'text', 'category', 'user', 'created_at')
	list_filter = ('category', 'user')
