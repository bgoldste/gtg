from django.db import models
from django.utils.text import slugify 
from autoslug import AutoSlugField


# Create your models here.

class Song(models.Model):

	title = models.CharField(max_length=300)
	artist_name = models.CharField(max_length=300)
	tab = models.TextField()

	slug = AutoSlugField(populate_from='title', unique=True)

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(unicode(self.title))
        	super(Song, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title