from django.contrib import admin
from .models import Vote, VoteCount

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['ip_address', 'timestamp']
    list_filter = ['timestamp']
    readonly_fields = ['ip_address', 'user_agent', 'timestamp']

@admin.register(VoteCount)
class VoteCountAdmin(admin.ModelAdmin):
    list_display = ['total_votes', 'last_updated']
    readonly_fields = ['last_updated']
