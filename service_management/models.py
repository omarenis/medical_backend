from django.db import models
from django.db.models import ImageField, Model, TextField, ForeignKey, FloatField


# Create your models here.
class Service(Model):
    category = ForeignKey(to='CategoryService', )
    image_service = ImageField()
    title = TextField()
    description = TextField()
    full_description = TextField()


class CategoryService(Model):

    image = ImageField()
    title = TextField()
    description = TextField()
    full_description = TextField()
    number_services = FloatField(default=0)
