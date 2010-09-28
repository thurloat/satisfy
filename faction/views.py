from faction.forms import RegisterCompanyForm
from faction.models import CompanyWatch, Topic
from django.template import RequestContext
from django.http import Http404, HttpResponseRedirect, HttpResponseForbidden

from django.shortcuts import render_to_response, get_object_or_404

def overview(request):
    return render_to_response('/register.html', {'blah':'blah',})

def company_dashboard(request, company_slug):
    cp = get_object_or_404(CompanyWatch, company_slug=company_slug)
    topics = Topic.objects.filter(company=cp.id)
    context = {
        'company': cp,
        'topics': topics
    }
    return render_to_response('faction/dashboard.html', context, context_instance = RequestContext(request))

def company_topics(request, company_slug):
    cp = get_object_or_404(CompanyWatch, company_slug=company_slug)
    
def company_list(request):
    cps = CompanyWatch.objects.all()
    context = {
        'companies': cps
    }
    return render_to_response('faction/company_list.html', context, context_instance = RequestContext(request))
    
def register_company(request):
    form = RegisterCompanyForm(request.POST or None)
    if form.is_valid():
        cp = form.save()
        return HttpResponseRedirect(cp.get_absolute_url())
    context = {
        'form': form
    }
    return render_to_response('faction/register.html', context, context_instance = RequestContext(request))
