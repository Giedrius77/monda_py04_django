# project ir tasks pagrindiniu langu suprojektavimas

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _


class Project(models.Model):
    name = models.CharField(_("nameeee"), max_length=100, db_index=True) # _() - reiskia kad teksta gali buti verciamas i kita kalba
    owner = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE, 
        verbose_name=_("ownereee"), # _() - reiskia kad teksta gali buti verciamas i kita kalba
        related_name='projects',
    )

    #budget = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("budget"))
    budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name=_("budget"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("project") # _() - reiskia kad teksta gali buti verciamas i kita kalba
        verbose_name_plural = _("projects") # _() - reiskia kad teksta gali buti verciamas i kita kalba
        ordering = ['id', 'name']

    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"pk": self.pk})


class Task(models.Model):
    name = models.CharField(_("nameeee"), max_length=100, db_index=True) # _() - reiskia kad teksta gali buti verciamas i kita kalba
    description = models.TextField(_("description"), blank=True, max_length=10000) # _() - reiskia kad teksta gali buti verciamas i kita kalba
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE, 
        verbose_name=_("project"), # _() - reiskia kad teksta gali buti verciamas i kita kalba
        related_name='tasks',
    )
    owner = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE, 
        verbose_name=_("owner"), # _() - reiskia kad teksta gali buti verciamas i kita kalba
        related_name='tasks',
    )
    created_at = models.DateTimeField(_("created at"), auto_now_add=True, db_index=True) # _() - reiskia kad teksta gali buti verciamas i kita kalba
    updated_at = models.DateTimeField(_("updated at"), auto_now=True, db_index=True) # _() - reiskia kad teksta gali buti verciamas i kita kalba
    is_done = models.BooleanField(_("is done"), default=False, db_index=True) # _() - reiskia kad teksta gali buti verciamas i kita kalba
    deadline = models.DateTimeField(_("deadline"), null=True, blank=True, db_index=True) # _() - reiskia kad teksta gali buti verciamas i kita kalba

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("task") # _() - reiskia kad teksta gali buti verciamas i kita kalba
        verbose_name_plural = _("tasks") # _() - reiskia kad teksta gali buti verciamas i kita kalba
        ordering = ['is_done', '-created_at']

    def get_absolute_url(self):
        return reverse("task_detail", kwargs={"pk": self.pk})
    


# Create your models here.
