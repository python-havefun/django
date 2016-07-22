from django import forms
 
class QuestionForm(forms.Form):
    ques_title = forms.CharField(max_length=256)
    ques = forms.CharField(max_length=256)
