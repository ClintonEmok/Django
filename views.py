from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from bokeh.client import pull_session
from bokeh.embed import server_session
import pandas as pd


class Home(TemplateView):
    template_name = 'home.html'


def homepage(request):
    # return HttpResponse('Welcome to our page')
    return render(request, "index.html")


def about(request):
    # return HttpResponse('Hello World')
    return render(request, "about.html")


def plot(request):
    return render(request, "plot.html")


def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['data']

        print(uploaded_file.name)
        print(uploaded_file.size)
    return render(request, 'upload.html')


def bkapp_page(request):
    with pull_session(url="http://localhost:5006/Interactive") as session:
        # update or customize that session
        session.document.roots[0].children[1].title.text = "Special Sliders For A Specific User!"

        # generate a script to load the customized session
        script = server_session(session_id=session.id, url="http://localhost:5006/Interactive")

        # use the script in the rendered page
        return render(request, "embed.html", dict(script=script))
