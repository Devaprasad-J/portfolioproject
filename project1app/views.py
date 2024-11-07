from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
from .forms import ProfileForm, ProjectForm, ExperienceForm, EducationForm, CertificationForm
from .models import Project, Experience, Education, Certification
from django.contrib import messages


@login_required
def profile_view(request):
    form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/profile.html', {'form': form})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/edit_profile.html', {'form': form})


@login_required
def portfolio_view(request):
    projects = Project.objects.filter(user=request.user)
    experiences = Experience.objects.filter(user=request.user)
    education = Education.objects.filter(user=request.user)
    certifications = Certification.objects.filter(user=request.user)

    return render(request, 'profiles/portfolio.html', {
        'projects': projects,
        'experiences': experiences,
        'education': education,
        'certifications': certifications,
    })


@login_required
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user  # Associate the project with the logged-in user
            project.save()
            return redirect('portfolio')
    else:
        form = ProjectForm()
    return render(request, 'profiles/add_project.html', {'form': form})


@login_required
def update_project(request, pk):
    project = Project.objects.get(pk=pk)
    if project.user != request.user:
        return redirect('portfolio')  # Prevent users from editing others' projects

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('portfolio')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'profiles/update_project.html', {'form': form})


@login_required
def delete_project(request, pk):
    project = Project.objects.get(pk=pk)
    if project.user == request.user:
        project.delete()
    return redirect('portfolio')


@login_required
def add_work_experience(request):
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.user = request.user
            experience.save()
            return redirect('portfolio')
    else:
        form = ExperienceForm()
    return render(request, 'profiles/add_work_experience.html', {'form': form})


@login_required
def add_education(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            education = form.save(commit=False)
            education.user = request.user
            education.save()
            return redirect('portfolio')
    else:
        form = EducationForm()
    return render(request, 'profiles/add_education.html', {'form': form})


@login_required
def add_certification(request):
    if request.method == 'POST':
        form = CertificationForm(request.POST)
        if form.is_valid():
            certification = form.save(commit=False)
            certification.user = request.user
            certification.save()
            return redirect('portfolio')
    else:
        form = CertificationForm()
    return render(request, 'profiles/add_certification.html', {'form': form})


@login_required
def delete_profile(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        logout(request)
        return redirect('login')  # Redirect to home page after deletion
    return render(request, 'profiles/delete_profile.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('profile')  # Redirect to profile or any desired page
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})