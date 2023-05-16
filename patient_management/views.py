from django.shortcuts import render

from common.views import ViewSet
from patient_management.services import ConsultationService, PatientService


# Create your views here.


class PatientViewSet(ViewSet):

    def __init__(self, serializer_class, service, **kwargs):
        super().__init__(serializer_class, service=PatientService(), **kwargs)


class ConsultationVewSet(ViewSet):

    def __init__(self, serializer_class, service, **kwargs):
        super().__init__(serializer_class, service=ConsultationService(), **kwargs)
