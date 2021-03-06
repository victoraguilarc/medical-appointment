# -*- coding: utf-8 -*-
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.agendas.api.v1.serializers.appointments import AppointmentSerializer
from apps.agendas.selectors.appointment import AppointmentSelector
from apps.contrib.api.viewsets import PermissionViewSet


class PatientsViewSet(PermissionViewSet):
    permission_classes = [IsAuthenticated]

    def appointments(self, request, **kwargs):
        """It shows the visitors' appointments."""

        appointments = AppointmentSelector.user_appointments(request.user)
        return Response(AppointmentSerializer(appointments, many=True).data)
