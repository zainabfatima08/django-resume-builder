from django.urls import path
from .views import ResumeDetailView, EndorseSkillView, TopResumeView

urlpatterns = [
    path('top/',                    TopResumeView.as_view(),    name='top_resumes'),
    path('endorse/<int:skill_id>/', EndorseSkillView.as_view(), name='endorse_skill'),
    path('<slug:slug>/',            ResumeDetailView.as_view(), name='resume_detail'),
]