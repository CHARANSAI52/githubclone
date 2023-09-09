from django.shortcuts import render, redirect
from .forms import UploadFileForm

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success.html')
    else:
        form = UploadFileForm()
    return render(request, 'file.html', {'form': form})
def success(request):
    return render(request, 'success.html')

