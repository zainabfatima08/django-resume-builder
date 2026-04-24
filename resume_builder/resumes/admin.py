from django.contrib import admin
from .models import Section, ResumeTheme

#-----------------SECTION---------------------

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display  = ('id', 'resume', 'title', 'order')
    list_filter   = ('resume',)
    search_fields = ('title',)
    ordering      = ('resume', 'order')
    list_editable = ('order',)

#---------------RESUME THEME------------------

@admin.register(ResumeTheme)
class ResumeThemeAdmin(admin.ModelAdmin):
    list_display  = ('id', 'name', 'primary_color')
    search_fields = ('name',)
