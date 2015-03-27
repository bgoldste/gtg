from django.db import models
from django.utils.text import slugify 


# Create your models here.

class Song(models.Model):

	title = models.CharField(max_length=300)
	artist_name = models.CharField(max_length=300)
	tab = models.TextField()

	slug = models.SlugField()

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(unicode(self.title))
        	super(Song, self).save(*args, **kwargs)