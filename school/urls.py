from django.contrib import admin

from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', views.students),
    path('add_student/', views.add_student),
    path('del_student/', views.del_student),
    path('edit_student/', views.edit_student)
]