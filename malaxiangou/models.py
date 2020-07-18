from django.db import models

class Social(models.Model):
	title = models.CharField(max_length=20)
	body = models.TextField()
	author = models.CharField(max_length=20)
	date = models.DateTimeField()

	def __str__(self):
		return self.title
