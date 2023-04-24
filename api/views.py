from django.shortcuts import render
from .models import BotUsers, Feedbacks
from rest_framework.generics import ListCreateAPIView
from .serializers import BotUsersSerializer, FeedbacksSerialzer


# Create your views here.
class BotUserApiView(ListCreateAPIView):
    queryset = BotUsers.objects.all()
    serializer_class = BotUsersSerializer


class FeedbacksApiView(ListCreateAPIView):
    queryset = Feedbacks.objects.all()
    serializer_class = FeedbacksSerialzer
