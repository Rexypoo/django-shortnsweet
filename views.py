from django.shortcuts import get_object_or_404, redirect, render

from .models import ShortURL

def redirect_alias(request, short_name):
    shorturl = get_object_or_404(ShortURL, alias=short_name)
    return redirect(shorturl.url)
