from django.shortcuts import render
from .forms import LogsForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.logic_measurement import create_Logs, get_Logs

def logs_list(request):
    logs = get_Logs()
    context = {
        'logs_list': logs
    }
    return render(request, 'Logs/Logs.html', context)

def log_create(request):
    if request.method == 'POST':
        form = LogsForm(request.POST)
        if form.is_valid():
            create_Logs(form)
            messages.add_message(request, messages.SUCCESS, 'Log create successful')
            return HttpResponseRedirect(reverse('logCreate'))
        else:
            print(form.errors)
    else:
        form = LogsForm()

    context = {
        'form': form,
    }

    return render(request, 'Logs/LogsCreate.html', context)