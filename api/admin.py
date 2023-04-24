from django.contrib import admin
from .models import BotUsers, Feedbacks

# Register your models here.


class CustomBotUserAdmin(admin.ModelAdmin):
    model = BotUsers
    list_display = ["username", "name", "user_id"]
    search_fields = ["username", "name"]
    list_filter = ["created_at"]


class CustomBFeedbacksAdmin(admin.ModelAdmin):
    model = Feedbacks
    search_fields = ["body"]
    list_filter = ["created_at"]


admin.site.register(BotUsers, CustomBotUserAdmin)
admin.site.register(Feedbacks, CustomBFeedbacksAdmin)
