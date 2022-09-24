from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from students.api.serializers import (
    ExamSerializer,
    ProgrammeSerializer,
    RoomSerializer,
    StudentSerializer,
)
from students.models import Exam, Programme, Student, Room


class StudentListCreateAPIView(ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()  # type: ignore


class StudentRetrieveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()  # type: ignore
    lookup_field = "id"


class ProgrammeListCreateAPIView(ListCreateAPIView):
    serializer_class = ProgrammeSerializer
    queryset = Programme.objects.all()  # type: ignore


class ProgrammeRetrieveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProgrammeSerializer
    queryset = Programme.objects.all()  # type: ignore
    lookup_field = "id"


class RoomListCreateAPIView(ListCreateAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()  # type: ignore


class RoomRetrieveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()  # type: ignore
    lookup_field = "id"


class ExamListCreateAPIView(ListCreateAPIView):
    serializer_class = ExamSerializer
    queryset = Exam.objects.all()  # type: ignore


class ExamRetrieveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ExamSerializer
    queryset = Exam.objects.all()  # type: ignore
    lookup_field = "id"
