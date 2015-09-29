from django.db import models

class Staff(models.Model):
	full_name = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
	bio = models.TextField()
	image = models.ImageField(upload_to='img/profile', max_length=100)

	def __unicode__(self):
		return self.full_name

class Fellow(models.Model):
	full_name = models.CharField(max_length=100)
	city = models.CharField(max_length=50)
	current_position = models.CharField(max_length=100)
	bio = models.TextField()
	year = models.IntegerField(default=0)
	image = models.ImageField(upload_to='img/profile', max_length=100)

	def __unicode__(self):
		return self.full_name