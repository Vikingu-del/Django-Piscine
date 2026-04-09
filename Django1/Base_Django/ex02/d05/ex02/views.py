from django.shortcuts import render, redirect
from django.conf import settings
from .forms import Ex02Form
from django.contrib import messages
from datetime import datetime
import os

def form(request):
    error_msg = None
    if request.method == 'POST':
        form = Ex02Form(request.POST)
        if form.is_valid():
            content = form.cleaned_data['user_text']
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            try:
                with open(settings.LOG_FILE_PATH, 'a') as log_file:
                    log_file.write(f'{timestamp} - {content}\n')
                return redirect('ex02:ex02_form')
            except Exception as e:
                error_msg = f"Error saving to log file: {e}"
                messages.error(request, error_msg)
    else:
        form = Ex02Form()

    history = []
    try:
        if os.path.exists(settings.LOG_FILE_PATH):
                with open(settings.LOG_FILE_PATH, 'r') as log_file:
                    history = log_file.readlines()
    except Exception as e:
        error_msg = f"Error reading from the log file: {e}"
        messages.error(request, error_msg)

    return render(request, 'ex02/form.html', {
        'form': form,
        'history': history,
        'error_msg': error_msg
    })

# Create your views here.
