from rest_framework import generics, permissions
from .models import Resume
from .serializers import ResumeCreateSerializer, ResumeSerializer


class ResumeCreateAPIView(generics.CreateAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ResumeListView(generics.ListAPIView):
    serializer_class = ResumeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_resumes = Resume.objects.filter(user=self.request.user)
        return user_resumes.prefetch_related('skills')


class ResumeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    lookup_field = 'id'
