# projekto ir tabu administravimas lenteleje

from django.contrib import admin
from . import models
from django.utils.translation import gettext_lazy as _


class ProjectAdmin (admin.ModelAdmin):
    list_display = ['id', 'name', 'total_tasks', 'undone_tasks', 'owner', 'recent_tasks', 'budget'] # stulpeliu pavadinimai project skiltyje pagal eiliskuma - 'id', stulpelis nera butinas, bet galima tureti
    list_display_links =['id', 'name'] # siuos langus padaro aktyvius (galima dadeti) per kuriuos galima ieiti i projekto vidu. 'id' stulpelis nera butinas, bet galima tureti
    list_filter = ['owner', 'name'] # sukurs nauja filtro langa desineje ir filtruos pagal 'owner', galima dadeti filtrus
    search_fields = ['name'] # padarys search lauka kuriame bus galima filtruoti tik pagal 'name' rakta. Galima dadeti ir kitus raktus
    fieldsets = (
        (None, {
            "fields": (
                ('name', 'owner', 'budget'), # su () bus vienoje eilute, be - atskiruose
            ),
        }),

    )


    def total_tasks(self, obj: models.Project): # sukuria papildoma stulpeli
        return obj.tasks.count()
    total_tasks.short_description = _('total tasks') # galime pakeisti stulpelio pavadinima

    def undone_tasks(self, obj: models.Project): # sukuria papildoma stulpeli
        return obj.tasks.filter(is_done=False).count()
    undone_tasks.short_description = _('undone tasks') # galime pakeisti stulpelio pavadinima

    def recent_tasks(self, obj: models.Project): # sukuria papildoma stulpeli
        return "; ".join(obj.tasks.order_by('-created_at').values_list('name', flat=True)[:3])
    recent_tasks.short_description = _('recent tasks') # galime pakeisti stulpelio pavadinima




class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'project', 'created_at', 'deadline', 'is_done'] # stulpeliu pavadinimai project skiltyje pagal eiliskuma - 'id', stulpelis nera butinas, bet galima tureti
    list_filter = ['is_done', 'project', 'owner', 'deadline', 'created_at'] # sukurs nauja filtro langa desineje ir filtruos pagal nurodytus kriterijus
    search_fields = ['name', 'description', 'project__name', 'owner__last_name', 'owner__username'] # sukurs nauja filtro langa desineje ir filtruos pagal nurodytus, galima dadeti filtrus
    list_editable = ['is_done', 'owner', 'project']
    readonly_fields = ['id', 'created_at', 'updated_at']
    fieldsets = (
        (_('General'), {
            "fields": (
                ('name', 'deadline', 'is_done'), 'description',
            ),
        }),
        (_('Ownership'), {
            "fields": (
                ('owner', 'project'),
            ),
        }),
        (_('Temporal Tracking'), {
            "fields": (
                ('created_at', 'updated_at', 'id'),
            ),
        }),
    )


admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.Task, TaskAdmin)
# Register your models here.
