from unicodedata import category
from django.shortcuts import render, get_object_or_404
from django.http.response import Http404
from .models import Company


def index(request):
    return render(request, "recruit/index.html")


def home(request):
    template = "recruit/error.html"
    try:
        # Check if the logged in credenitals are belongs to candidate or company.
        company = get_object_or_404(Company, user=request.user)
        template = "recruit/company_home.html"
        category = "Company"
        name = company.name
        parameters = {
            "jobs": company.job_set.all()
        }
    except (Http404, Company.DoesNotExist):
        try:
            candidate = get_object_or_404(Company, user=request.user)
            template = "recruit/candidate_home.html"
            category = "Candidate"
            name = f"{candidate.first_name} {candidate.last_name}"
        except (Http404, Company.DoesNotExist):
            name = ""
            category = ""
            template = "recruit/404.html"    
        
    return render(request, template, {"name": name, "category": category, **parameters})
