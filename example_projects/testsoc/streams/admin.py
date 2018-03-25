from django.contrib import admin

# from .models import Post
# admin.site.register(Post)



from .models import Post 
class PostAdmin(admin.ModelAdmin):
  list_display = ['user_id', 'link_or_text', 'title']
admin.site.register(Post, PostAdmin)