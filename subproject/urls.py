from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('hall/', views.hall_list, name='hall_list'),
    path('lecturers/', views.lecturer_list, name='lecturer_list'),
    path('registerLect/', views.registerLect, name='registerLect'),
    path('registerLect/tryreg', views.tryreg, name='tryreg'),
    path('login/', views.login, name='login'),
    path('update/<str:LecturerID>/<str:event_id>/', views.update, name='update'),
    path('add_event/<str:lecturer_id>/', views.add_event, name='add_event'),
    path('delete_event/<str:EventID>/', views.delete_event, name='delete_event'),
    path('LectView/<str:LecturerID>/', views.LectView, name='LectView'),
    path('delete_event/<str:LecturerID>/<str:event_id>/', views.delete_event, name='delete_event'),
    path('delete_profile/<str:lecturer_id>/', views.delete_profile, name='delete_profile'),
    path('login_admin/', views.login_admin, name='login_admin'),
    path('update_profile/<str:lecturer_id>/', views.update_profile, name='update_profile'),
    path('AdminView/', views.admin_view, name='admin_view'),
    path('AdminView/update_admin/<str:event_id>/', views.update_admin, name='update_admin'),
    path('delete_Event/<str:event_id>/', views.delete_Event, name='delete_Event'),
    path('delete/', views.delete_record, name='delete'),

]
