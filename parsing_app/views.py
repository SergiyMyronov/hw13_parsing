from django.contrib import messages
from django.shortcuts import redirect, render

from parsing_app.forms import TaskForm
from parsing_app.parsing import parsing_html


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
        messages.add_message(request, messages.SUCCESS, f'{len(quotes)} quotes added')
        redirect('index')
    else:
        form = TaskForm(initial={'text': ' '})

    return render(request, 'parsing_app/task.html', {'form': form})
