# -*- coding: utf-8 -*-

from django.urls import path
from apps.agendas.views.professionals import DoctorsView, DoctorProfileAgendaView, DoctorProfileView
from apps.agendas.views.visitors import VisitorProfileView

app_name = 'agendas'
urlpatterns = [
    # > Transactions
    path(
        '',
        DoctorsView.as_view(),
        name='professionals',
    ),

    # >> Profiles
    path(
        'profile/',
        VisitorProfileView.as_view(),
        name='visitor-profile',
    ),
    path(
        'profile/professional/',
        DoctorProfileView.as_view(),
        name='visitor-profile',
    ),
    path(
        'professional/<uuid:professional_uuid>/',
        view=DoctorProfileAgendaView.as_view(),
        name='professional',
    )
]