from rest_framework import viewsets
from rest_framework.status import HTTP_200_OK
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


from fingerprints.api.serializers import (
    FingerprintReadSerializer,
    FingerprintWriteSerializer,
    FingerprintVerificationSerializer
)

from fingerprints.models import Fingerprint, FingerprintVerification
from students.models import Student
from attendances.models import ExamAttendance, StudentAttendance


@api_view(["POST"])
def verify_fingerprint(request):
    """
    Get the reqest data which is a fingerprint id, and
    verify if that student associated with that id is
    supposed to be seated in the room for the exams being
    conducted.

    # Fingerprint ID <-> Student
    # Get registered exams
    # Check exam field (active == True)
    # Add active to model and serializer
    # Access students on the exam 
    # Check if the student is among the ids
    # check the room

    """
    if request.POST == "POST":
        print(request.data)
    
        #  Get student associated with the given fingerprint id
        fingerprint_id = request.data["fingerprint_id"]
        student = Student.objects.get(fingerprint_id=fingerprint_id)

        # Get registered exams and check for the active one
        student_active_exam = None
        for exam in student.registered_exams:
            if exam.active:
                student_active_exam = exam
                break
        
        # Check if student is among the exam registered student
        student_is_registered_for_active_exam = False
        for exam_student in student_active_exam.students.all():
            if student == exam_student:
                student_is_registered_for_active_exam = True
                break
        
        ## CHECKING FOR THE ALLOCATED ROOM
        # Get latest exam attendance instance
        if student_is_registered_for_active_exam:
            student_is_rightly_allocated = False
            latest_exam_attendance = ExamAttendance.objects.first()
            for attendance_student in latest_exam_attendance.room.students:
                if attendance_student == student:
                    student_is_rightly_allocated = True
        
        FingerprintVerification.objects.create(state=student_is_rightly_allocated, student=student)

        if student_is_rightly_allocated:
            StudentAttendance.objects.create(student=student, exam=student_active_exam, room=latest_exam_attendance.room, exam_attendance=latest_exam_attendance)
        
        return Response(status=HTTP_200_OK)

@api_view(["GET"])
def get_latest_fingerprint_verification(request):
    if request.GET == "GET":
        latest = FingerprintVerification.objects.first()
        serializer = FingerprintVerificationSerializer(latest)
        
        return Response(serializer.data, HTTP_200_OK)






class FingerprintViewSet(viewsets.ModelViewSet):
    queryset = Fingerprint.objects.all()  # type: ignore

    def get_serializer_class(self):
        if self.action in ["list", "retrieve", "destroy"]:
            return FingerprintReadSerializer
        elif self.action in ["create", "update", "partial_update"]:
            return FingerprintWriteSerializer
