from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, ResultViewSet, FeeViewSet, NoteViewSet, ReportCardViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'results', ResultViewSet)
router.register(r'fees', FeeViewSet)
router.register(r'notes', NoteViewSet)
router.register(r'reportcards', ReportCardViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]