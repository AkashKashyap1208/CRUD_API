from django.contrib import admin
from django.urls import path , include
# from rest_framework.urlpatterns import format_suffix_patterns
from crud_api.views import *

urlpatterns = [
    path('signup/', CustomeUserPostAndGet.as_view()),
    path('signup/<int:id>/', CustomUserDetail.as_view()),
    path('employee/' , EmployeePostandGet.as_view()),

]

# urlpatterns = format_suffix_patterns(urlpatterns)