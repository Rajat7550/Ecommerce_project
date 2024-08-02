# Create your views here.
import pandas as pd
from braces.views import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, FormView

from application.custom_classes import AdminRequiredMixin, AjayDatatableView
from apps.healthcare.forms import XlsUploadForm, CreateDepartmentForm, CreateCategoryForm, CreateJobAiForm
from apps.healthcare.models import Department, Category, JobAi


# Create your views here.


#-----------Department--------------#
class CreateDepartmentView(AdminRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Department
    form_class = CreateDepartmentForm
    template_name = 'admin/healthcare/form.html'
    success_message = "Department created successfully"
    success_url = reverse_lazy('admin-department-list')

class ListDepartmentView(AdminRequiredMixin, LoginRequiredMixin, TemplateView):
    template_name = 'admin/healthcare/lists.html'


class ListDepartmentViewJson(AdminRequiredMixin, AjayDatatableView):
    model = Department
    columns = ['name','actions']
    exclude_from_search_columns = ['actions']


#-----------Category--------------#


class CreateCategoryView(AdminRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Category
    form_class = CreateCategoryForm
    template_name = 'admin/healthcare/form.html'
    success_message = "Category created successfully"
    success_url = reverse_lazy('admin-category-list')


class ListCategoryView(AdminRequiredMixin, LoginRequiredMixin, TemplateView):
    template_name = 'admin/healthcare/category_lists.html'


# -----------JobAi--------------#

class CreateJobAiView(AdminRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = JobAi
    form_class = CreateJobAiForm
    template_name = 'admin/healthcare/form.html'
    success_message = "JobAi created successfully"
    success_url = reverse_lazy('admin-jobAi-list')


class ListJobAiView(AdminRequiredMixin, LoginRequiredMixin, TemplateView):
    template_name = 'admin/healthcare/jobai_lists.html'

# -----------Xls_file--------------#

class XlsUploadView(FormView):
    template_name = 'admin/healthcare/uploadXls.html'
    form_class = XlsUploadForm
    success_url = reverse_lazy('admin-department-list')

    def form_valid(self, form):
        xls_file = form.cleaned_data['xls_file']
        df = pd.read_excel(xls_file)

        # Print the headers of the Excel file
        print("Excel file headers:", df.columns.tolist())

        for index, row in df.iterrows():
            # Ensure there is no ambiguity in Department and Category creation
            department, created = Department.objects.get_or_create(
                name=row.get('Department', '')
            )

            # Use a unique description to distinguish categories within the same department
            category, created = Category.objects.get_or_create(
                name=row.get('Category', ''),
                description=row.get('Description', ''),
                department=department
            )

            # Create the JobAi
            JobAi.objects.create(
                department=department,
                category=category,
                description=row.get('Job Description', ''),
                roles=row.get('Roles', {}),
                skills=row.get('Skills', {})
            )

        return super().form_valid(form)