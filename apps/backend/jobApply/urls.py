from django.urls import path
from .views import *

app_name = 'jobApply'
urlpatterns = [
    path('', Index.as_view(), name='job_list'),
    path('upload/', job_upload, name='job_upload'),
    path('upload_sms/', sms_upload, name='sms_upload'),
    path('apply/<int:job_id>/', apply_job, name='apply_job'),
    path('apply_job_response/<int:job_id>/', apply_job_response, name='apply_job_response'),
]
