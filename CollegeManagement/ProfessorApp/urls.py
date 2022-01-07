from django.urls import path
from .import views

urlpatterns = [
    path('add/',views.AddProfView.as_view(),name='add_prof'),
    path('show',views.ShowProfView.as_view(),name='show_prof'),
    path('delete/<int:i>/',views.ProfDelete.as_view(),name='delete_prof'),
    path('update/<int:i>/',views.ProfUpdate.as_view(),name='update_prof'),

]