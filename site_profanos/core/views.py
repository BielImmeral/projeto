from django.shortcuts import render
from friends.models import Friend

def dashboard(request):
    friends = Friend.objects.all()
    return render(request, 'core/dashboard.html', {'friends': friends})
