import pdfplumber
from django.shortcuts import render
from .forms import ResumeUploadForm

def upload_resume(request):
    text_output = None

    if request.method == "POST":
        form = ResumeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            resume_file = request.FILES['resume']
            with pdfplumber.open(resume_file) as pdf:
                pages = [page.extract_text() for page in pdf.pages]
                text_output = "\n\n".join(pages)
    else:
        form = ResumeUploadForm()

    return render(request, "parser/upload.html", {
        "form": form,
        "text_output": text_output,
    })