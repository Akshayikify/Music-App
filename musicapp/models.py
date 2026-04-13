from django.db import models

class Song(models.Model):
    title=models.TextField()
    artist=models.TextField()
    audio_file=models.FileField()
    audio_link=models.CharField(max_length=200,blank=True,null=True)
    lyrics=models.TextField(blank=True,null=True)
    duration=models.CharField(max_length=200)
    paginated_by=2
    
    def __str__(self):
        return self.title
