from django.contrib import admin
from .models import BotUsers, Feedbacks

# Register your models here.


class CustomBotUserAdmin(admin.ModelAdmin):
    model = BotUsers
    list_display = ["username", "name", "user_id", "created_at"]
    search_fields = ["username", "name"]
    list_filter = ["created_at"]


class CustomBFeedbacksAdmin(admin.ModelAdmin):
    model = Feedbacks
    search_fields = ["body"]
    list_display = ["user_id", "body", "created_at"]
    list_filter = ["created_at"]


admin.site.register(BotUsers, CustomBotUserAdmin)
admin.site.register(Feedbacks, CustomBFeedbacksAdmin)
