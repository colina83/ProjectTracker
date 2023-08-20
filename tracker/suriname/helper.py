from django.db.models import Max
from .models import Status,Project
from django.db.models import Case, When, F, Value, CharField

def all_table():
    status = Status.objects.all()
    print(status)
     
    