from django.contrib import admin
from blog_app.models import Blog
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_title', 'sub_title', 'body',
                    'blog_image', 'created_date_time')
    prepopulated_fields = {'slug': ('blog_title',)}


admin.site.register(Blog, BlogAdmin)
