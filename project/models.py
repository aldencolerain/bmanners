from django.db import models

class Entry(models.Model):
	server_name = models.CharField(max_length=1000)
	server_ip = models.CharField(max_length=100)
	message = models.CharField(max_length=10000)