from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from accounts.models import Todo,Character 
from django.contrib.auth.mixins import LoginRequiredMixin



class IndexView(LoginRequiredMixin,View):
    def get(self, request):
        User_data = Character()
        context = {
            "Current_level": User_data.level,
            "Character_name": User_data.character_name,
        }
        return render(request, "dashboard/Index.html", context)
    

        
class TodoListView(LoginRequiredMixin,View):
    pass

class TodoCreateView(LoginRequiredMixin, View):
    def get(self, request, character_id):
        character = get_object_or_404(Character, id=character_id)
        return render(request, 'dashboard/todo_create.html', {
            'character': character,
        })

    def post(self, request, character_id):
        character = get_object_or_404(Character, id=character_id)

        # ToDoを作成
        Todo.objects.create(
            character=character,
            title=request.POST.get('title'),
            body=request.POST.get('body'),
            start_at=request.POST.get('start_at'),
            end_at=request.POST.get('end_at'),
            rank=request.POST.get('rank'),
        )

        # 保存後はトップページ(IndexViewのURL名称)へリダイレクト
        return redirect('Index')

class TodoEditView(LoginRequiredMixin,View):
    pass

class TodoDeleteView(LoginRequiredMixin,View):
    pass

Index = IndexView.as_view()