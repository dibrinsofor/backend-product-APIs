from django.db import models

# def user_directory_path(instance, filename): 
  
#     # file will be uploaded to MEDIA_ROOT / user_<id>/<filename> 
#     return 'user_{0}/{1}'.format(instance.user.id, filename) 
# def upload_location(instance, filename, **kwargs):
#     file_path = '{author_id/}/{title}-{filename}'.format(
#         author_id = str(instance.author.id), title=str(instance.title), filename=filename
#     )
#     return file_path    


# Create your models here.
class Locations(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    locationDescription = models.CharField(max_length=140)
    country = models.CharField(max_length=20)
#     image = models.ImageField(upload_to=upload_location, null=False, blank=False)
#     name= models.CharField(max_length=500)
    videofile= models.FileField(upload_to='images/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.imagefile)


    ###dont firget to add url path for image now

def __str__(self):
    return self.name 
