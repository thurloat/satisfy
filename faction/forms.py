from django import forms

from faction.models import CompanyWatch

class RegisterCompanyForm(forms.Form):
    company = forms.CharField()
    company_url = forms.CharField()
    
    def save(self):
        """docstring for save"""
        cf, created = CompanyWatch.objects.get_or_create(
            company = self.cleaned_data['company'],
            company_url = self.cleaned_data['company_url'],
            )
        return cf