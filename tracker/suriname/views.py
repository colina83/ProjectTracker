from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from .models import Manager, Company, Project, Product, Status
from django.db.models import Max
from .helper import all_table
import pandas as pd

# Create your views here.
def home(request):
    if request.method == 'GET':
        status = Status.objects.all().order_by('date')
        data = []
          
        for project_status in status:
            data.append({
                "client": project_status.company.name,
                "manager": project_status.manager_name,
                "project_name": project_status.project.name,
                "status": project_status.status,
                "date": project_status.date,
            })

        df = pd.DataFrame(data)
        # Sort the DataFrame by date in descending order
        df_sorted = df.sort_values('date', ascending=False)

        # Drop duplicates based on client, manager, and project_name, keeping the first occurrence (most recent)
        df_unique = df_sorted.drop_duplicates(['client', 'manager', 'project_name'], keep='first')

        # Pivot the DataFrame to long format with project name in columns
        df_long = pd.pivot_table(df_unique, values='status', index=['client', 'manager', 'date'], columns='project_name', aggfunc='first')

        # Reset the index to make client, manager, and date as separate columns
        df_long = df_long.reset_index()
        columns_to_drop = ['date']
        df_long = df_long.drop(columns=columns_to_drop)
        df_long = df_long.fillna('-')
        project_df = df_long .reset_index(drop=True)   
        project_dict = project_df.to_dict(orient='records')
        
        for item in project_dict:
            for key in list(item.keys()):
                new_key = key.replace(" ", "_")
                if new_key != key:
                    item[new_key] = item.pop(key)
        
        print(project_dict)
        
        context = {
        'project_list': project_dict,
        }    
        
        
        
        
    return render(request,'home.html', context)
    