from django.urls import path

from students.api.views import (
    ProgrammeListCreateAPIView,
    ProgrammeRetrieveUpdateDeleteAPIView,
    StudentListCreateAPIView,
    StudentRetrieveUpdateDeleteAPIView,
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
]
