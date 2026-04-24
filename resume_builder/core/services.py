from django.db.models import F

def increment_views(resume):
    resume.views = F('views') + 1
    resume.save(update_fields=['views'])
    resume.refresh_from_db()