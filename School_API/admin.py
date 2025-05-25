from django.contrib import admin
from .models import (
    User,
    Role,
    RoleUser,
    Student,
    Parent,
    Staff,
    Class,
    Section,
    Subject,
    Timetable,
    Attendance,
    StaffAttendance,
    Fee,
    Exam,
    ExamResult,
    Announcement,
)

admin.site.register(User)
admin.site.register(Role)
admin.site.register(RoleUser)
admin.site.register(Student)
admin.site.register(Parent)
admin.site.register(Staff)
admin.site.register(Class)
admin.site.register(Section)
admin.site.register(Subject)
admin.site.register(Timetable)
admin.site.register(Attendance)
admin.site.register(StaffAttendance)
admin.site.register(Fee)
admin.site.register(Exam)
admin.site.register(ExamResult)
admin.site.register(Announcement)
