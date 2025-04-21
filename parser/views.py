import pdfplumber
import requests

from bs4 import BeautifulSoup
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import ResumeUploadForm
from .models import LinkedInProfile, JobExperience


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




@login_required
def import_linkedin(request):
    user = request.user
    url = user.linkedin_url

    if not url:
        return redirect("profile")

    # Simple HTML scrape (mock implementation for now)
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        profile, _ = LinkedInProfile.objects.get_or_create(user=user)

        # ⚠️ These selectors are fake - update based on real HTML structure
        name = soup.find("h1").text.strip() if soup.find("h1") else ""
        headline = soup.find("h2").text.strip() if soup.find("h2") else ""
        summary = soup.find("p").text.strip() if soup.find("p") else ""

        if name and not profile.full_name:
            profile.full_name = name

        if headline and not profile.headline:
            profile.headline = headline

        if summary:
            profile.summary = summary

        profile.save()

        # More scraping logic for experiences goes here (future step)

    except Exception as e:
        print(f"[ERROR] LinkedIn import failed: {e}")

    return redirect("profile")