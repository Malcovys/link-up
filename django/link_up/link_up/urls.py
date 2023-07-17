from django.contrib import admin
from django.urls import path

from api.views import StudentView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/student/auth/', StudentView.as_view())
]
