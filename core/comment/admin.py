from django.contrib import admin
from .models import Comment

# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "post",
        "name",
        "email",
        "subject",
        "message",
        "approved",
        "created_date",
        "updated_date",
    ]


admin.site.register(Comment,CommentAdmin)

