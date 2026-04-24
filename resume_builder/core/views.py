from django.views import View
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .models import Resume, Skill
from .services import increment_views

#------------------DETAIL VIEW---------------------

class ResumeDetailView(View):
    def get(self, request, slug):
        resume = get_object_or_404(Resume, slug = slug)

        increment_views(resume)

        return render(request, "core/resume.html", {
            "resume": resume
        })

#----------------ENDORSE VIEW---------------------

class EndorseSkillView(View):
    def post(self, request, skill_id):
        skill = get_object_or_404(Skill, id = skill_id)
        skill.endorsements += 1
        skill.save()

        return JsonResponse({
            "endorsements": skill.endorsements
        })

#-----------------RESUME VIEW--------------------

class TopResumeView(View):
    def get(self, request):
        resumes = Resume.objects.order_by('-views')[:5]

        return render(request, "core/top_resume.html", {
            "resumes": resumes
        })
