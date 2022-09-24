from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from students.api.serializers import ProgrammeSerializer, StudentSerializer
from students.models import Programme, Student


class StudentListCreateAPIView(ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class StudentRetrieveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    lookup_field = "id"


class ProgrammeListCreateAPIView(ListCreateAPIView):
    serializer_class = ProgrammeSerializer
    queryset = Programme.objects.all()


class ProgrammeRetrieveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProgrammeSerializer
    queryset = Programme.objects.all()
    lookup_field = "id"
