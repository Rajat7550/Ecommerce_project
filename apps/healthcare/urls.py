from django.urls import path

from apps.category.views import ListCategoryViewJson, CreateCategoryView
from apps.healthcare.views import XlsUploadView, CreateDepartmentView, ListDepartmentView, ListCategoryView, \
    ListJobAiView, CreateJobAiView, ListDepartmentViewJson

urlpatterns = [
    path('admin/department/add', CreateDepartmentView.as_view(), name='admin-department-add'),
    path('admin/department/list', ListDepartmentView.as_view(), name='admin-department-list'),
    path('admin/department/list/ajax', ListDepartmentViewJson.as_view(), name='admin-department-list-ajax'),

    path('admin/category/add', CreateCategoryView.as_view(), name='admin-category-add'),
    path('admin/category/list', ListCategoryView.as_view(), name='admin-category-list'),
    path('admin/jobAi/add', CreateJobAiView.as_view(), name='admin-jobAi-add'),
    path('admin/jobAi/list', ListJobAiView.as_view(), name='admin-jobAi-list'),
    path('upload/xlsfile/', XlsUploadView.as_view(), name='upload-xls'),


]