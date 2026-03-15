from django.shortcuts import render

# Create your views here.
def evolution_view(request):
    if request.method == "POST":
        evolution = request.POST.get("evolution")
        pass
    return render(request, "ai_prompt/evolution.html")