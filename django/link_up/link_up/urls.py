from django.contrib import admin
from django.urls import path

from api.views import StudentAuthView
from api.views import TeacherAuthView
from api.views import PresenceView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/student/auth/', StudentAuthView.as_view()),
    path('api/teacher/auth/', TeacherAuthView.as_view()),
    path('api/presences/', PresenceView.as_view())
]
