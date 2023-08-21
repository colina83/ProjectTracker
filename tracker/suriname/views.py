from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from .models import Manager, Company, Project, Product, Status
from django.db.models import Max
from .helper import all_table
import pandas as pd
from .forms import StatusUpdateForm
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from collections import defaultdict

def home(request):
    if request.method == 'GET':
        status = Status.objects.all().order_by('date')
        data = [
            {
                "client": project_status.company.name,
                "manager": project_status.manager_name,
                "project_name": project_status.project.name,
                "status": project_status.status,
                "date": project_status.date,
            }
            for project_status in status
        ]
        
        df = pd.DataFrame(data)
        df_sorted = df.sort_values(['client', 'manager', 'project_name', 'date'], ascending=[True, True, True, False])
        
        df_unique = df_sorted.drop_duplicates(['client', 'manager', 'project_name'], keep='first')
        
        pivot_table = pd.pivot_table(df_unique, values='status', index=['client', 'manager'], columns='project_name', aggfunc=lambda x: x.iloc[0])
        
        pivot_table = pivot_table.applymap(lambda x: '-' if pd.isnull(x) else x)
        
        project_dict_list = pivot_table.reset_index().to_dict(orient='records')
        
        final_project_dict_list = []
        for project_dict in project_dict_list:
            new_project_dict = {k.replace(" ", "_"): v for k, v in project_dict.items()}
            final_project_dict_list.append(new_project_dict)
        
        print(final_project_dict_list)
        
        context = {
            'project_list': final_project_dict_list,
        }
        
        return render(request, 'home.html', context)


def update_status(request):
    if request.method == 'GET':
        form = StatusUpdateForm()
        context = {
            'form': form,
        }
        return render(request, 'update_status.html', context)
    else:
        form = StatusUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect back to the home page after updating
        else:
            context = {
                'form': form,
            }
            return render(request, 'update_status.html', context)
    