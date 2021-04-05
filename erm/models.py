from django.db import models

# Create your models here.


class Users(models.Model):
    employee_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)  # Mutturaj
    age = models.IntegerField()  # 22


    def upload_photo(self, filename):
        path = 'erm/photo/{}'.format(filename)
        return path
    photo = models.ImageField( upload_to=upload_photo, null=True, blank=True)

    def upload_file(self, filename):
        path = 'erm/photo/{}'.format(filename)
        return path
    resume = models.FileField( upload_to=upload_file, null=True, blank=True)

    def __str__(self):
        return f"{self.employee_id} - {self.name}"