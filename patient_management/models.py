from django.db import models
from django.db.models import Model, TextField, IntegerField, FileField, CASCADE, ForeignKey
from rest_framework.serializers import ModelSerializer


# Create your models here.
class Patient(Model):
    first_name = TextField()
    last_name = TextField()
    age = IntegerField()
    phone = TextField()
    medical_health_status = TextField()

    class Meta:
        db_table = 'patients'


class Consultation(Model):
    patient = ForeignKey(to='Patient', on_delete=CASCADE, null=False)
    type = TextField()
    document = FileField(upload_to='files/documents')

    class Meta:
        db_table = 'consultations'


class PatientSerializer(ModelSerializer):

    class Meta:
        model = Patient
        fields = '__all__'


class ConsultationSerializer(ModelSerializer):

    class Meta:
        model =Consultation
        fields = '__all__'
