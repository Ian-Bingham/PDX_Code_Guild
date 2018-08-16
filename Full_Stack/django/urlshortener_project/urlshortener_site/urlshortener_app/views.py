from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import URL
import random, string, requests

# Create your views here.
def index(request):
    url_list = URL.objects.all()
    context = {'url_list': url_list}
    return render(request, 'urlshortener_app/index.html', context)


def saveurl(request):
    if request.method == 'POST':
        og_url = request.POST['urlInput']
        if not og_url.startswith('http'):
            og_url = 'http://' + og_url
        try:
            url = URL.objects.get(og_url=og_url)
            return HttpResponse("You've already converted that site")
        except URL.DoesNotExist:
            try:
                r = requests.get(og_url)
                if r.status_code == 200:
                    letters_list = list(string.ascii_letters)
                    random.shuffle(letters_list)
                    shuffled_letters = ''.join(letters_list)
                    url_tag = shuffled_letters[:10]
                    short_url = 'localhost:8000/urlshortener/redirect/' + url_tag
                    new_url = URL(og_url=og_url, short_url=short_url, url_tag=url_tag)
                    new_url.save()
                    return HttpResponseRedirect(reverse('urlshortener_app:index'))
                else:
                    raise Exception
            except:
                return HttpResponse('Website does not exist: ' + og_url)

def redirect_site(request, url_tag):
    url = get_object_or_404(URL, url_tag=url_tag)
    return redirect(url.og_url)
