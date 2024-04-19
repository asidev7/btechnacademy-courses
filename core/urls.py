from core.views import CategoryCourse, about, affiliate, affiliate_success, courses, details_course, enquire, home, mail_succes,enroll_success
from django.urls import path


urlpatterns = [
    path('',home,name="home"),
    path('<slug:slug>/',details_course,name="details"),
    path('emailSent',mail_succes),
    path('enroll_success',enroll_success),
    path('courses',courses),
    path('about',about),
    path('affiliate',affiliate),
    path('success',affiliate_success),
    path('category/<int:category_id>/course_link/2024',CategoryCourse,name="course_by_category"),
    path('enquire',enquire)
]
