from django.urls import path
from .views import BotUserApiView, FeedbacksApiView

urlpatterns = [
    path("bot-users/", BotUserApiView.as_view(), name="bot_users"),
    path("feedbacks/", FeedbacksApiView.as_view(), name="feedbacks"),
]
