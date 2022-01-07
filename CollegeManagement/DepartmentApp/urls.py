from django.urls import path
from .import views

urlpatterns = [
    path('add/',views.AddDeptView.as_view(),name='add_dept'),
    path('show',views.ShowDeptView.as_view(),name='show_dept'),
    path('delete/<int:i>/',views.DeptDelete.as_view(),name='delete_dept'),
    path('update/<int:i>/',views.DeptUpdate.as_view(),name='update_dept'),

]