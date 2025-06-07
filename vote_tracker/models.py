from django.db import models
from django.utils import timezone

class Vote(models.Model):
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField(blank=True)
    timestamp = models.DateTimeField(default=timezone.now)
    
    class Meta:
        unique_together = ['ip_address']  # Prevent duplicate votes from same IP
    
    def __str__(self):
        return f"Vote from {self.ip_address} at {self.timestamp}"

class VoteCount(models.Model):
    total_votes = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    
    @classmethod
    def get_count(cls):
        obj, created = cls.objects.get_or_create(id=1)
        return obj.total_votes
    
    @classmethod
    def increment(cls):
        obj, created = cls.objects.get_or_create(id=1)
        obj.total_votes += 1
        obj.save()
        return obj.total_votes
