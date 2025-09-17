from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    DestroyAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.views import APIView
from .models import Habit
from .serializers import HabitSerializer, PublicHabitSerializer
from users.permissions import IsUser
from .paginators import CustomPaginator
from rest_framework.response import Response


class HabitCreateApiView(CreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.user = self.request.user
        habit.save()


class HabitApiView(APIView):
    queryset = Habit.objects.get_queryset().order_by("id")
    serializer_class = HabitSerializer
    pagination_class = CustomPaginator

    def get(self, request):
        user = request.user
        habit = Habit.objects.filter(user=user)
        serializer = HabitSerializer(habit, many=True)
        return Response(serializer.data)


class PublicHabitApiView(APIView):
    queryset = Habit.objects.all()
    serializer_class = PublicHabitSerializer
    pagination_class = CustomPaginator

    def get(self, request):
        is_public = request.data.get("is_public")
        habit = Habit.objects.filter(is_public=True)
        serializer = HabitSerializer(habit, many=True)
        return Response(serializer.data)


class HabitRetrieveApiView(RetrieveAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitUpdateApiView(UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsUser,)


class HabitDestroyApiView(DestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsUser,)
