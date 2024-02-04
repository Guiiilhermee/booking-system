from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=50)

class Record(models.Model):

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    date = models.DateTimeField(blank=True, null=True)
    time = models.CharField(max_length=10,blank=True, null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, max_length=100, blank=True, null=True)


    def __str__(self):

        return self.name + self.email + self.phone
