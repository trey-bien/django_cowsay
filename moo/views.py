from django.shortcuts import render, reverse
import subprocess

from moo.models import TextInput
from moo.forms import AddTextForm

def index_view(request):
    moo = ''
    if request.method == "POST":
        form = AddTextForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            text = data.get('text')
            TextInput.objects.create(
                text = data.get('text')
            )
            moo = subprocess.run(['cowsay', text], capture_output=True, text=True).stdout
    form = AddTextForm()
    return render(request, "index.html", {"form": form, "moo": moo})

def most_recent_view(request):
    most_recent = TextInput.objects.filter().order_by('-id')[:10]
    return render(request, 'mostrecent.html', {'most_recent': most_recent})

        
    
    