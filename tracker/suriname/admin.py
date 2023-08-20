from django.contrib import admin
from .models import Manager, Company, Project,Product,Status
@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'manager')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'stage')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('project', 'status', 'date', 'company')
