from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import EXP


class EXPbarView(View):
    def get(self, request, user_id):
        User_EXPdata = get_object_or_404(EXP, user_id=user_id)
        context = {
            "Current_level": User_EXPdata.level,
            "Character_name": User_EXPdata.character_name,
        }
        return render(request, "dashboard/EXP_bar.html", context)
    
EXP_bar = EXPbarView.as_view()
        
