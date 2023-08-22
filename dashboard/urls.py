from django.urls import path
from .views import ResumeCreateAPIView, ResumeListView, ResumeDetailView

urlpatterns = [
    path('resume/create/', ResumeCreateAPIView.as_view(), name='create-resume'),
    path('resume/list/', ResumeListView.as_view(), name='create-list'),
    path('resume/<int:id>/', ResumeDetailView.as_view(), name='create-detail'),
]
