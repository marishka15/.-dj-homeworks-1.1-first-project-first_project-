from django.db import models

class Phone(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField()
    release_date = models.DateField()
    lte_exists = models.NullBooleanField()
    slug = models.SlugField(null=True)

    def __str__(self):
            return self.name