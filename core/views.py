from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdmin, IsTeacher, IsStudent
from .models import Student, Result, Fee, Note, ReportCard
from .serializers import StudentSerializer, ResultSerializer, FeeSerializer, NoteSerializer, ReportCardSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        """
        Assign permissions based on the action being performed.
        """
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            # Only teachers can add, edit, or delete results
            return [IsTeacher()]
        elif self.action == 'list':
            # Only admins can list all results
            return [IsAdmin()]
        elif self.action == 'retrieve':
            # Students can retrieve their own result
            return [IsStudent()]
        return super().get_permissions()

    def get_queryset(self):
        """
        Restrict queryset based on user role.
        """
        user = self.request.user
        if user.role == 'student':
            # Students only see their own results
            return Result.objects.filter(student=user)
        elif user.role == 'teacher':
            # Teachers see all results (could be filtered by class later)
            return Result.objects.all()
        elif user.role == 'admin':
            # Admins see everything
            return Result.objects.all()
        return Result.objects.none()


class FeeViewSet(viewsets.ModelViewSet):
    queryset = Fee.objects.all()
    serializer_class = FeeSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class ReportCardViewSet(viewsets.ModelViewSet):
    queryset = ReportCard.objects.all()
    serializer_class = ReportCardSerializer