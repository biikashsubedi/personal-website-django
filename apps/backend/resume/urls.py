from django.urls import path
from .views import *

app_name = 'resume'
urlpatterns = [
    path('education/', Index.as_view(), name='education.index'),
    path('education/create/', Create.as_view(), name='education.create'),
    path('education/update/<str:pk>', Update.as_view(), name='education.update'),
    path('education/delete/<str:pk>', Delete.as_view(), name='education.delete'),

    path('experience/', ExperienceIndex.as_view(), name='experience.index'),
    path('experience/create/', ExperienceCreate.as_view(), name='experience.create'),
    path('experience/update/<str:pk>', ExperienceUpdate.as_view(), name='experience.update'),
    path('experience/delete/<str:pk>', ExperienceDelete.as_view(), name='experience.delete'),

    path('skill/', SkillIndex.as_view(), name='skill.index'),
    path('skill/create/', SkillCreate.as_view(), name='skill.create'),
    path('skill/update/<str:pk>', SkillUpdate.as_view(), name='skill.update'),
    path('skill/delete/<str:pk>', SkillDelete.as_view(), name='skill.delete'),

    path('key-skill/', KeySkillIndex.as_view(), name='key-skill.index'),
    path('key-skill/create/', KeySkillCreate.as_view(), name='key-skill.create'),
    path('key-skill/update/<str:pk>', KeySkillUpdate.as_view(), name='key-skill.update'),
    path('key-skill/delete/<str:pk>', KeySkillDelete.as_view(), name='key-skill.delete'),

    path('project/', ProjectIndex.as_view(), name='project.index'),
    path('project/create/', ProjectCreate.as_view(), name='project.create'),
    path('project/update/<str:pk>', ProjectUpdate.as_view(), name='project.update'),
    path('project/delete/<str:pk>', ProjectDelete.as_view(), name='project.delete'),

]
