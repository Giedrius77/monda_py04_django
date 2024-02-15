# kuriame nauja front end view vietoj raketos
# kuris yra vienas puslapis

from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import gettext_lazy as _ # kad veiktu vertimas
from . import models

# web browser agrindinio puslapio views

def index(request: HttpRequest) -> HttpResponse:
    context = {
        'projects_count': models.Project.objects.count(),
        'tasks_count': models.Task.objects.count(),
        'users_count': models.get_user_model().objects.count(),
    }
    return render(request, 'tasks/index.html', context)

def task_list(request: HttpRequest) -> HttpResponse:
    return render(request, 'tasks/task_list.html', {
        'task_list': models.Task.objects.all(),
    })

def task_detail(request: HttpRequest, pk:int) -> HttpResponse:
    return render(request, 'tasks/task_detail.html', {
        'task': get_object_or_404(models.Task, pk=pk)
    })

def task_done(request: HttpRequest, pk: int) -> HttpResponse:
    task = get_object_or_404(models.Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    messages.success(request, "{} {} {} {}".format( # tik tokiu formatavimo budu galimas vertimas, su f"{} neveiks
        _('task').capitalize(), # _() - reiskia kad teksta gali buti verciamas i kita kalba
        task.name,
        _('marked as'), # _() - reiskia kad teksta gali buti verciamas i kita kalba
        _('done') if task.is_done else _('undone') # _() - reiskia kad teksta gali buti verciamas i kita kalba
    ))
    if request.GET.get('next'):
        return redirect(request.GET.get('next'))
    return redirect(task_list)
  