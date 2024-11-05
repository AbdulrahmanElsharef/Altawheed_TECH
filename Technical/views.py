from django.shortcuts import render,get_object_or_404
from .models import Request,Report,Action_Detail
# from .filter import RequesttFilter
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
# Create your views here.
def print(request):
    requests=Request.objects.all()
    context={"objects":requests,}
    return render(request, "print.html",context)

def invoice(request, id):
    # Retrieve a specific record by ID
    obj = get_object_or_404(Request, id=id)
    context={'obj':obj,}
    return render(request, 'invoice.html', context)


def credit_note(request, id):
    # Retrieve a specific record by ID
    obj = get_object_or_404(Request, id=id)
    context={'obj':obj,}
    return render(request, 'credit_note.html', context)

def replacement(request, id):
    # Retrieve a specific record by ID
    obj = get_object_or_404(Request, id=id)
    context={'obj':obj,}
    return render(request, 'replacement.html', context)



def report(request):
    requests=Report.objects.all()
    context={"objects":requests,}
    return render(request, "report.html",context)

def technical(request, id):
    # Retrieve a specific record by ID
    obj = get_object_or_404(Report, id=id)
    context={'obj':obj,"objects":Action_Detail.objects.all}
    return render(request, 'technical.html', context)
