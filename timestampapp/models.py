from django.db import models

# Create your models here.

class UuidTimeStamp(models.Model):
    uuid_code = models.UUIDField()
    timestamp = models.DateTimeField(auto_now_add=True)
    timestamp_str = models.CharField(max_length=255)


    def save(self, *args, **kwargs):
        self.timestamp_str = str(self.timestamp)
        super(UuidTimeStamp, self).save(*args, **kwargs)
    

    class Meta:
        ordering = ["-timestamp"]


    def __str__(self):
        return str(self.uuid_code)