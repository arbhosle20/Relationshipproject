from django.urls import path
from .import views

urlpatterns = [
    path('add/',views.AddStudentView.as_view(),name='add_student'),
    path('show',views.ShowStudentView.as_view(),name='show_student'),
    path('delete/<int:i>/',views.StudentDelete.as_view(),name='delete_student'),
    path('update/<int:i>/',views.StudentUpdate.as_view(),name='update_student'),

]