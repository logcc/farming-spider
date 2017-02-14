#!/usr/bin/env python
# coding:utf-8

from django.db import models

# Create your models here.
class Farmdata(models.Model):
	year = models.IntegerField(default=None)
	province = models.CharField(max_length= 20)
	crop = models.CharField(max_length= 20)
	type_db = models.CharField(max_length= 20)
	account = models.FloatField(default=None)

	#def __str__(self):
		#return self.province
