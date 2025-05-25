from rest_framework import routers
from django.urls import path, include
from .views import (
    UserViewSet,
    RoleViewSet,
    StudentViewSet,
    ParentViewSet,
    StaffViewSet,
    ClassViewSet,
    SectionViewSet,
    SubjectViewSet,
    TimetableViewSet,
    AttendanceViewSet,
    StaffAttendanceViewSet,
    FeeViewSet,
    ExamViewSet,
    ExamResultViewSet,
    AnnouncementViewSet,
)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'students', StudentViewSet)
router.register(r'parents', ParentViewSet)
router.register(r'staff', StaffViewSet)
router.register(r'classes', ClassViewSet)
router.register(r'sections', SectionViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'timetables', TimetableViewSet)
router.register(r'attendances', AttendanceViewSet)
router.register(r'staff-attendances', StaffAttendanceViewSet)
router.register(r'fees', FeeViewSet)
router.register(r'exams', ExamViewSet)
router.register(r'exam-results', ExamResultViewSet)
router.register(r'announcements', AnnouncementViewSet)

urlpatterns = [
    path('', include(router.urls)),  
]
