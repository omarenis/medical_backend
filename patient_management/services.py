from common.repositories import Repository
from common.services import Service
from patient_management.models import Patient, Consultation

PATIENT_FIELDS = {
    'first_name': {'type': 'string', 'required': True},
    'last_name': {'type': 'string', 'required': True},
    'age': {'type': 'int', 'required': True},
    'customer': {'type': 'foreign_key', 'required': True},
    'medical_health_status': {'type': 'string', 'required': True}
}

CONSULTATION_FIELDS = {
    'patient': {'type': 'foreign_key', 'required': True},
    'type': {'type': 'string', 'required': True},
    'document': {'type': 'file', 'required': True}
}


class PatientService(Service):
    def __init__(self, repository: Repository = Repository(model=Patient), fields=None):
        if fields is None:
            fields = PATIENT_FIELDS
        super().__init__(repository, fields)


class ConsultationService(Service):
    def __init__(self, repository: Repository = Repository(model=Consultation), fields=None):
        if fields is None:
            fields = CONSULTATION_FIELDS
        super().__init__(repository, fields)
