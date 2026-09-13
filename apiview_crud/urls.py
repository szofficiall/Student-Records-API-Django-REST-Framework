from django.urls import path
from .views import StudentApi

urlpatterns = [
    path(
        "students/",
        StudentApi.as_view(),
        name="get_post_students",
    ),
    path(
        "students/<int:pk>/",
        StudentApi.as_view(),
        name="update_delete_students",
    ),
]
