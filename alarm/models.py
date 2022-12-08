from django.db import models
from django.utils.timezone import now

# Create your models here.
class SendMssg(models.Model):
    img_url = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200, primary_key=True)
    open_date = models.CharField(max_length=200)
    open_date_m = models.IntegerField(default=1)
    open_date_d = models.IntegerField(default=1)
    open_date_dn = models.IntegerField(default=1)
    cur_stat = models.CharField(max_length=200)
    c_date = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.title} - {self.open_date} - {self.cur_stat}"