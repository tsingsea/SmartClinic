from django.urls import path
from .views import clinic_list, clinic_detail, clinic_new, clinic_edit, clinic_delete, export_clinics_to_excel

urlpatterns = [
    path('clinics/', clinic_list, name='clinic_list'),
    path('clinics/<int:pk>/', clinic_detail, name='clinic_detail'),
    path('clinics/new/', clinic_new, name='clinic_new'),
    path('clinics/<int:pk>/edit/', clinic_edit, name='clinic_edit'),
    path('clinics/<int:pk>/delete/', clinic_delete, name='clinic_delete'),
    path('export-clinics/', export_clinics_to_excel, name='export_clinics_to_excel'),
]
