from django.urls import path
from .views import ReorderSectionsView, ResumePDFView, CreateResumeView

urlpatterns = [
    path('reorder/',         ReorderSectionsView.as_view(), name='reorder'),
    path('pdf/<slug:slug>/', ResumePDFView.as_view(),       name='pdf'),
    path('create/',          CreateResumeView.as_view(),    name='create_resume')
]