from django.shortcuts import render


def evolution(request):
    return render(request, 'ai_prompt/evolution.html')
