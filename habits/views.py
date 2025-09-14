from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    DestroyAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from .models import Habit
from .serializers import HabitSerializer, PublicHabitSerializer
from users.permissions import IsUser
from .paginators import CustomPaginator
from users.models import User


class HabitCreateApiView(CreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.user = self.request.user
        habit.save()


class HabitListApiView(ListAPIView):
    queryset = Habit.objects.get_queryset().order_by('id')
    serializer_class = HabitSerializer
    pagination_class = CustomPaginator


class PublicHabitListApiView(ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = PublicHabitSerializer
    pagination_class = CustomPaginator


class HabitRetrieveApiView(RetrieveAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitUpdateApiView(UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (
        IsUser,
    )


class HabitDestroyApiView(DestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (
        IsUser,
    )
