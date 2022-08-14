from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import FormView
from .models import Answer, Question
from .forms import AnswerCreateForm, QuestionCreateForm
from django.urls import reverse, reverse_lazy
from django.core.paginator import Paginator

class QuestionList(View):
    def get(self, request):
        
        questions = Question.objects.all()
        paginator = Paginator(questions, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {'page_obj': page_obj}
        if "search" in request.GET:
            search=request.GET['search']
            questions=Question.objects.filter(Q(title__icontains=search) | Q(body__icontains=search))
            return render(self.request,
                     template_name='home.html', 
                     context={'quest': questions})
        return render(self.request,
                     template_name='home.html', 
                     context=context)
    
    
class QuestionDetail(View):
    form_class=AnswerCreateForm
    template_name = 'quest_detail.html'
    
    def get(self, request, index):
        question = Question.objects.get(pk=index)
        form = self.form_class
        return render(request, self.template_name, context={'quest': question, 'form': form})

    def post(self, request, index):
        user = self.request.user
        form = self.form_class(request.POST)
        question = Question.objects.get(pk=index)
        if form.is_valid():
            ans = form.save(commit=False)
            ans.author = user
            ans.body = form.cleaned_data['body']
            ans.question = question
            ans.save()  
        return render(request, self.template_name, context={'quest': question})

class QuestCreate(FormView):
    form_class = QuestionCreateForm
    template_name = 'quest_create.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        quest = form.save(commit=False)
        quest.author = self.request.user
        quest.save()
        return super().form_valid(form)