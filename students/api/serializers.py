from rest_framework import serializers

from students.models import Programme, Student, Room, Exam
from users.api.serializers import InvigilatorSerializer
from users.models import User


class ProgrammeSerializer(serializers.ModelSerializer):
    # TODO: Add all the students under a particular programme
    class Meta:

        model = Programme
        fields = ["id", "name", "college"]


class StudentSerializer(serializers.ModelSerializer):
    programme_name = serializers.ReadOnlyField(source="programme_of_study.name")

    class Meta:
        model = Student
        fields = [
            "id",
            "created",
            "first_name",
            "last_name",
            "other_names",
            "student_id",
            "index_number",
            "level",
            "programme_name",
            "programme_of_study",
        ]


class RoomSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, read_only=True)
    invigilators = InvigilatorSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ["id", "name", "capacity", "students", "invigilators"]


class ExamSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True)
    rooms = RoomSerializer(many=True)

    class Meta:
        model = Exam
        fields = [
            "id",
            "course_name",
            "course_code",
            "level",
            "students",
            "rooms",
            "start",
            "end",
        ]
