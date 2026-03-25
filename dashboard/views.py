from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import EXP
from accounts.models import Todo,Character 


class EXPbarView(View):
    def get(self, request, user_id):
        User_EXPdata = get_object_or_404(EXP, user_id=user_id)
        context = {
            "Current_level": User_EXPdata.level,
            "Character_name": User_EXPdata.character_name,
        }
        return render(request, "dashboard/EXP_bar.html", context)
    
EXP_bar = EXPbarView.as_view()
        
class TodoListView(View):
    pass

class TodoCreateView(View):
    def get(self, request, character_id):
        character = get_object_or_404(Character, id=character_id)
        return render(request, 'dashboard/todo_create.html', {
            'character': character,
        })

    def post(self, request, character_id):
        character = get_object_or_404(Character, id=character_id)

        title = request.POST.get('title')
        body = request.POST.get('body')
        start_at = request.POST.get('start_at')
        end_at = request.POST.get('end_at')
        rank = request.POST.get('rank')

        Todo.objects.create(
            character=character,
            title=title,
            body=body,
            start_at=start_at,
            end_at=end_at,
            rank=rank,
        )

        return render(request,"dashboard/EXP_bar.html")

class TodoEditView(View):
    pass

class TodoDeleteView(View):
    pass
