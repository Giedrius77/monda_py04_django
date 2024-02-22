# kuriame nauja front end view vietoj raketos
# kuris yra vienas puslapis

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _ # kad veiktu vertimas
from django.views import generic
from . import models

# pagrindinio puslapio views based on class model, kuris niekuom nepranasesnis uz def model based
# parasius views reikia itraukti i urls.py

class ProjectListView(generic.ListView):
    model = models.Project
    template_name = 'tasks/project_list.html'

class ProjectDetailView(generic.DetailView):
    model = models.Project
    template_name = 'tasks/project_detail.html'

class ProjectCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.Project
    template_name = 'tasks/project_create.html'
    fields = ('name', )

    def get_success_url(self) -> str: # user projekto sukurimas ir jo sukurimo sekme!
        messages.success(self.request, _('project created successfully').capitalize()) # _() tekstas bus verciamas
        return reverse('project_list') # jei teisingai sukurs nuves i project_list, kiu atveju klaida

    def form_valid(self, form): # patikrins ar forma sukurta teisingai
        form.instance.owner = self.request.user # tas kas sukure tas ir bus owneris, nereiks nurodineti pagrindinio ownerio
        return super().form_valid(form)

# web browser agrindinio puslapio views based on def model

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
  