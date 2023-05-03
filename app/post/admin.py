from django.contrib import admin

from post.models import Post, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_title',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'post_title', 'text', 'category', 'user', 'created_at')
    list_filter = ('category', 'user')
