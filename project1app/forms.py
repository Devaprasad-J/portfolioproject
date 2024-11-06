from django import forms
from .models import Profile, Project, Experience, Education, Certification


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'skills', 'contact_email']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'project_link', 'image']


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['job_title', 'company_name', 'description']


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['school_name', 'degree', 'graduation_year']


class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = ['certification_name', 'organization', 'date_received']
