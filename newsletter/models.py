from django.db import models

class SignUp(models.Model):
	full_name = models.CharField(max_length=250)
	timestamp = models.DateTimeField()
	email = models.EmailField()
	updated = models.BooleanField(default=False)

	def __uniclode__(self):
		return self.full_name
