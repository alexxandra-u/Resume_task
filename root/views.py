from django.shortcuts import render, redirect
from .models import ResumeModel
from django.http import FileResponse
from .forms import ResumeForm


def resume_view(request):
    if not request.user.is_authenticated:
        return redirect('log_in')
    if len(request.user.resumemodel_set.all()) == 0:
        r = request.user.resumemodel_set.create()
    else:
        r = ResumeModel.objects.get(user=request.user)
    if request.method == 'POST':
        form = ResumeForm(request.POST, instance=r)
        if request.POST.get('save_data'):
            if form.is_valid():
                form.save()
        if request.POST.get('export_data'):
            pass
    else:
        form = ResumeForm()
    return render(request, 'root/resume.html', {'form': form})
