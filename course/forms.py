from django import forms
from .models import Add,Course

class Add_Form(forms.ModelForm):
    class Meta:
        model = Add
        fields = ['name','course_code', 'contact']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control shadow'}),
            'course_code': forms.TextInput(attrs={'class':'form-control shadow'}),
            'contact': forms.TextInput(attrs={'class':'form-control shadow'})
        }
        def __init__(self, *args, **kwargs): 
            super(Add_Form, self).__init__(*args, **kwargs)
            self.fields['name'].widget.attrs.update({'class': 'form-control'})
            self.fields['course_code'].widget.attrs.update({'class': 'form-control'})
            self.fields['contact'].widget.attrs.update({'class': 'form-control'})

class Course_Form(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title','descrition', 'language','programming','level','creator','code','price']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control shadow'}),
            'descrition': forms.TextInput(attrs={'class':'form-control shadow'}),
            'language': forms.TextInput(attrs={'class':'form-control shadow'}),
            'programming': forms.TextInput(attrs={'class':'form-control shadow'}),
            'level': forms.TextInput(attrs={'class':'form-control shadow'}),
            'creator': forms.TextInput(attrs={'class':'form-control shadow'}),
            'code': forms.TextInput(attrs={'class':'form-control shadow'}),
            'price': forms.TextInput(attrs={'class':'form-control shadow'}),
        }