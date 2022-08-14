from django import forms
from .models import Answer, Question

class QuestionCreateForm(forms.ModelForm):
    title = forms.CharField(max_length=100,
                            label='Question title',
                            widget=forms.Textarea(attrs={
                                'class': 'ui input',
                                'placeholder' : 'Question Title',
                                'rows': 2
                            }))
    body = forms.CharField(label='Detailed description of your question',
                            widget=forms.Textarea(attrs={
                                'class': 'ui input' ,
                                'rows': 5,
                                'placeholder' : 'Detailed description'
                            }))
    
    class Meta:
        model = Question
        fields = ['title', 'body']

class AnswerCreateForm(forms.ModelForm):
    body=forms.CharField(label='Your answer', widget=forms.Textarea(attrs={
        'class':'ui input',
        'placehodler': 'Your answer',
        'rows': 1
    }))
    class Meta:
        model=Answer
        fields=['body']
