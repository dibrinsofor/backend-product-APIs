from django.db import models


# def upload_location(instance, filename, **kwargs):
#     file_path = '{author_id/}/{title}-{filename}'.format(
#         author_id = str(instance.author.id), title=str(instance.title), filename=filename
#     )
#     return file_path    


# Create your models here.
class Locations(models.Model):
    Name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    locationDescription = models.CharField(max_length=140)
    country = models.CharField(max_length=20)

    #######
    image = models.ImageField(null=True, blank=True)

    ###dont firget to add url path for image now

def __str__(self):
    return self.name 
