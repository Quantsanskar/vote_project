from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from .models import Vote, VoteCount
import json

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class VoteView(View):
    def get(self, request):
        # Automatically register vote when page is accessed
        ip_address = get_client_ip(request)
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        
        # Check if this IP has already voted
        vote_exists = Vote.objects.filter(ip_address=ip_address).exists()
        
        if not vote_exists:
            # Create new vote
            Vote.objects.create(
                ip_address=ip_address,
                user_agent=user_agent
            )
            # Increment total count
            VoteCount.increment()
            new_vote = True
        else:
            new_vote = False
        
        total_votes = VoteCount.get_count()
        
        return render(request, 'vote_thanks.html', {
            'new_vote': new_vote,
            'total_votes': total_votes
        })

class GirlfriendView(View):
    def get(self, request):
        total_votes = VoteCount.get_count()
        return render(request, 'girlfriend_page.html', {
            'total_votes': total_votes
        })

def get_vote_count(request):
    """API endpoint to get current vote count"""
    total_votes = VoteCount.get_count()
    return JsonResponse({'total_votes': total_votes})
