from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class TasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasks'
    verbose_name = _('tasks') # _() - reiskia kad teksta gali buti verciamas i kita kalba


# nereikia class Meta
    
    #class Meta:
        #verbose_name = _('tasks') # _() - reiskia kad teksta gali buti verciamas i kita kalba
