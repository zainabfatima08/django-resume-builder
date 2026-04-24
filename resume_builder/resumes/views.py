from django.shortcuts import render, redirect
import json
from django.http import HttpResponse, JsonResponse
from django.views import View
from .utils import generate_pdf
from core.models import Resume, Skill

from .models import Section

#----------------REORDER VIEW-----------------

class ReorderSectionsView(View):
    def post(self, request):
        data = json.loads(request.body)

        for index, section_id in enumerate(data.get("order")):
            Section.objects.filter(id = section_id).update(order = index)

            return JsonResponse({"status" : "ok"})

#-------------PDF VIEW---------------------------

class ResumePDFView(View):
    def get(self, request, slug):
        resume = Resume.objects.get(slug = slug)

        pdf = generate_pdf("themes/default.html", {
            "resume" : resume
        })

        return HttpResponse(pdf, content_type = 'application/pdf')

#---------------CREATE VIEW--------------------------

class CreateResumeView(View):
    def get(self, request):
        return render(request, "core/create_resume.html")

    def post(self, request):
        name = request.POST.get("name")

        resume = Resume.objects.create(name=name)

        Section.objects.create(
            resume=resume,
            title="About",
        )

        return redirect(f"/{resume.slug}/")
