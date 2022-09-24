from django.urls import path

from students.api.views import (
    ExamListCreateAPIView,
    ProgrammeListCreateAPIView,
    ProgrammeRetrieveUpdateDeleteAPIView,
    RoomListCreateAPIView,
    RoomRetrieveUpdateDeleteAPIView,
    StudentListCreateAPIView,
    StudentRetrieveUpdateDeleteAPIView,
    ExamRetrieveUpdateDeleteAPIView,
)


app_name = "students"
urlpatterns = [
    path("students", StudentListCreateAPIView.as_view(), name="list-create-students"),
    path(
        "students/<str:id>/",
        StudentRetrieveUpdateDeleteAPIView.as_view(),
        name="retrieve-update-delete-students",
    ),
    path(
        "programmes",
        ProgrammeListCreateAPIView.as_view(),
        name="list-create-programmes",
    ),
    path(
        "programmes/<str:id>/",
        ProgrammeRetrieveUpdateDeleteAPIView.as_view(),
        name="retrieve-update-delete-programmes",
    ),
    path("rooms", RoomListCreateAPIView.as_view(), name="list-create-rooms"),
    path(
        "rooms/<str:id>/",
        RoomRetrieveUpdateDeleteAPIView.as_view(),
        name="retrieve-update-delete-rooms",
    ),
    path("exams", ExamListCreateAPIView.as_view(), name="list-create-exams"),
    path(
        "exams/<str:id>/",
        ExamRetrieveUpdateDeleteAPIView.as_view(),
        name="retrieve-update-delete-exams",
    ),
]
