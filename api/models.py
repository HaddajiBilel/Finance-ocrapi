from django.db import models
# Create your models here.


class File(models.Model):
    id = models.AutoField(primary_key=True)
    file = models.FileField(blank=False, null=False)
    name = models.CharField(max_length=50, null=True)
    remark = models.CharField(max_length=50, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    tabPath = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = "Files_Storage"
