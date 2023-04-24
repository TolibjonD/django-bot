from .models import BotUsers, Feedbacks
from rest_framework.serializers import ModelSerializer


class BotUsersSerializer(ModelSerializer):
    class Meta:
        model = BotUsers
        fields = ("name", "username", "user_id", "created_at")


class FeedbacksSerialzer(ModelSerializer):
    class Meta:
        model = Feedbacks
        fields = ("user_id", "created_at", "body")
