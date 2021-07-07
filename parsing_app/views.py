from bs4 import BeautifulSoup  # xml parsing
from django.contrib.sites import requests

from parsing_app.forms import TaskForm
# from celery_app.tasks import send_mail as celery_send_mail
from parsing_app.parsing import parsing_html

from django.contrib import messages
from django.shortcuts import render, redirect


def index(request):
    if request.method == 'POST':
        quotes = parsing_html()
        long_str = ''
        if quotes:
            for i in range(len(quotes)):
                long_str += quotes[i]+'\n\n'
        else:
            long_str = ' '
        form = TaskForm(initial={'text': long_str})
        # if form.is_valid():
        #     subject = 'Celery test'
        #     from_email = 'sergemk@entecheco.com'
        #     recipient_list = [form.cleaned_data['email']]
        #     due_date = form.cleaned_data['date']
        #     message = form.cleaned_data['text']
        #     celery_send_mail.apply_async((subject, message, from_email, recipient_list), eta=due_date)
        messages.add_message(request, messages.SUCCESS, f'{len(quotes)} quotes added')
        redirect('index')
    else:
        form = TaskForm(initial={'text': ' '})

    return render(request, 'parsing_app/task.html', {'form': form})
