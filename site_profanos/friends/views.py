from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import check_password
from .models import Friend
from texts.models import TextBlock

def friend_login(request, slug):
    friend = get_object_or_404(Friend, slug=slug)
    session_key = f"friend_unlocked_{friend.id}"

    if request.session.get(session_key):
        return redirect('friend_page', slug=slug)

    error = None

    if request.method == 'POST':
        password = request.POST.get('password')
        if check_password(password, friend.password_hash):
            request.session[session_key] = True
            return redirect('friend_page', slug=slug)
        else:
            error = "Senha incorreta"

    return render(request, 'friends/friend_login.html', {
        'friend': friend,
        'error': error
    })


def friend_page(request, slug):
    friend = get_object_or_404(Friend, slug=slug)
    texts = TextBlock.objects.filter(friend=friend)

    # Lista de textos desbloqueados na sessão
    unlocked_texts = request.session.get('unlocked_texts', [])

    # Marca cada texto se está desbloqueado
    for text in texts:
        text.unlocked = text.id in unlocked_texts

    return render(request, 'friends/friend_page.html', {
        'friend': friend,
        'texts': texts
    })



from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.hashers import check_password


def unlock_text(request, text_id):
    text = get_object_or_404(TextBlock, id=text_id)

    if request.method == 'POST':
        password = request.POST.get('password')
        if check_password(password, text.password_hash):
            unlocked = request.session.get('unlocked_texts', [])
            if text.id not in unlocked:
                unlocked.append(text.id)
                request.session['unlocked_texts'] = unlocked

    return redirect('friend_page', slug=text.friend.slug)


