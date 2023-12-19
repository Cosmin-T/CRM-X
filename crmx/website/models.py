from django.db import models

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    subject = models.TextField(max_length=2000)
    email = models.CharField(max_length=100)
    status = models.CharField(max_length=15)
    resolution = models.CharField(max_length=50)
    description = models.TextField(max_length=50000)
    comment = models.TextField(max_length=50000)

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")
