from django.db import models

class FaqQuestion(models.Model):
	question = models.CharField(max_length = 100)
	answer = models.TextField()

	def __unicode__(self):
		return self.question


