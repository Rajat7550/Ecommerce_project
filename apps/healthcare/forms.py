from django import forms
from apps.healthcare.models import Department, Category, JobAi


class CreateDepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'

class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class CreateJobAiForm(forms.ModelForm):
    class Meta:
        model = JobAi
        fields = '__all__'


class XlsUploadForm(forms.Form):
    xls_file = forms.FileField(label='UploadXlsFile')