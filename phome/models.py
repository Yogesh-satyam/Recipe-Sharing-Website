
import datetime
import os
from django.db import models



def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('admin/Cuisines_category', filename)

class Cuisines_category(models.Model):
    name=models.CharField(default=None, null=True,max_length=50)
    desp=models.CharField(default=None, null=True,max_length=500)
    image = models.ImageField(default=None, upload_to=filepath, null=True, blank=True)
    