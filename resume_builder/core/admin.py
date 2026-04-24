from django.contrib import admin
from .models import Resume, Skill

#---------------RESUME ADMIN------------------

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display    = ('id', 'name', 'slug', 'theme', 'views')
    search_fields   = ('name', 'slug')
    list_filter     = ('theme',)
    readonly_fields = ('views',)

#---------------SKILL ADMIN----------------

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'resume', 'endorsements')
    search_fields = ('name',)
    list_filter = ('resume',)
    list_editable = ('endorsements',)
