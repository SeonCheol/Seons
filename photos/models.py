from django.db import models
from django.utils import timezone
# Create your models here.

class Photo(models.Model):
	id = models.AutoField(primary_key=True)
	author = models.ForeignKey('auth.User')
	content = models.TextField(max_length=500, null=True, blank=True)
	image = models.ImageField(upload_to='uploads/%Y/%m/%d/orig')
	filtered_image = models.ImageField(upload_to='uploads/%Y/%m/%d/filtered')
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def delete(self, *args, **kwagrs):
		self.image.delete()
		self.filtered_image.delete()
		super(Photo, self).delete(*args, **kwagrs)
	def __str__(self):
		return self.content