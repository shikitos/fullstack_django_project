from django.shortcuts import render


# My Imports
from django.contrib.auth.decorators import login_required

def frontend(request):
    return render(request, "frontend.html")

# ---------------- BACKEND SECTION ----------------
@login_required(login_url="login")
def backend(request):
    return render(request, "backend.html")