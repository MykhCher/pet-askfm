from django.urls import path
from .views import QuestionList, QuestionDetail, QuestCreate

urlpatterns = [
    path('', QuestionList.as_view(), name='home'),
    path('question/<int:index>', QuestionDetail.as_view(), name='quest_detail'),
    path('create', QuestCreate.as_view(), name='quest_create')
]
