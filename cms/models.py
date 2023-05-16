from django.db import models
from django.db.models import TextField, Model, CharField, ImageField
from rest_framework.serializers import ModelSerializer


# Create your models here.
class Partner(Model):
    label = CharField(max_length=255, unique=True, null=False)
    image = ImageField(max_length=255, null=False)
    description = TextField(null=False)

    class Meta:
        db_table = 'partners'


class PartnerSerializer(ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'
