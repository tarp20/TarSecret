from django.contrib import admin
from .models import Post,Group,Comment
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk','text','pub_date','author')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = "no data"



class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk','title','slug','description')
    search_fields = ('text',)
    empty_value_display = "no data"

admin.site.register(Post, PostAdmin)
admin.site.register(Group,GroupAdmin)
admin.site.register(Comment)