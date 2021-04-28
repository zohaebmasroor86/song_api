from django.db import models

# Create your models here.
class Song(models.Model):
    Id = models.Integerfield(blank=False, null=False)
    Name = models.Charfield(max_length=100, null=False, blank=False)
    Duration = models.Decimalfield(max_digits=4, decimal_places=2, blank=False)
    Uploaded time = models.Integerfield(datetime.Datetime, blank=False)

class Podcast(models.Model):
    Id = models.Integerfield(blank=False, null=False)
    Name = models.Charfield(max_length=100, null=False, blank=False)
    Duration = models.Decimalfield(max_digits=4, decimal_places=2, blank=False)
    Uploaded time = models.Integerfield(datetime.Datetime, blank=False)
    Host = models.Charfield(max_length=100, blank=False)
    Participants = models.Textfield(max_length=100, blank=True, end={''})

class Audiobook(models.Model):
    Id = models.Integerfield(blank=False, null=False)
    Title = models.Charfield(max_length=100, null=False, blank=False, end={''})
    Author = models.Charfield(max_length=100, null=False, blank=False, end={''})
    Narrator = models.Charfield(max_length=100, null=False, blank=False, end={''})
    Duration = models.Decimalfield(max_digits=4, decimal_places=2, blank=False)
    Uploaded time = models.Integerfield(datetime.Datetime, blank=False)


    def __str__(self):
        return self.name
