from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from accounts.models import Todo,Character
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin,View):
    def get(self, request):
        User_EXPdata = get_object_or_404(Character)
        Todo_data = get_object_or_404(Todo)
        Now = timezone.now()
        context = {
            "Current_level": User_EXPdata.level,
            "Character_name": User_EXPdata.character_name,
            "EXP_current_data":User_EXPdata.exp,
            "Todo_list":Todo_data.body,
            "Current_time":Now,
        }
        return render(request, "dashboard/Index.html", context)
        
    def save(self, *args, **kwargs):
        #一定値以上になったらレベルアップ
        if self.exp >= 100:
            self.level += 1
            #100の時0に戻す
            self.exp = (self.exp - 100)
        
        super().save(*args, **kwargs)
        
        
    

        
class TodoListView(LoginRequiredMixin,View):
    pass

class TodoCreateView(LoginRequiredMixin,View):
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

        return render(request,"dashboard/Index.html")

class TodoDetailView(View):
    def get(self, request, todo_id):
        todo = get_object_or_404(Todo, id=todo_id, delete_flag=False)
        return render(request, 'dashboard/todo_detail.html', {
            'todo': todo,
            'character': todo.character,
        })

    def post(self, request, todo_id):
        todo = get_object_or_404(Todo, id=todo_id, delete_flag=False)
        return render(request, 'dashboard/todo_detail.html', {
            'todo': todo,
            'character': todo.character,
        })

class TodoEditView(View):
    def get(self, request, todo_id):
        todo = get_object_or_404(Todo, id=todo_id, delete_flag=False)

        return render(request, 'dashboard/todo_edit.html', {
            'todo': todo,
            'character': todo.character,
        })

    def post(self, request, todo_id):
        todo = get_object_or_404(Todo, id=todo_id, delete_flag=False)

        title = request.POST.get('title')
        body = request.POST.get('body')
        start_at = request.POST.get('start_at')
        end_at = request.POST.get('end_at')
        rank = request.POST.get('rank')

        todo.title = title
        todo.body = body
        todo.start_at = start_at or None
        todo.end_at = end_at or None
        todo.rank = rank
        todo.save()

        return render(request, "dashboard/todo_detail.html", {
            "character": todo.character,
            "todo": todo,
            "message": "クエストを更新しました",
        })

class TodoDeleteView(View):
    def post(self, request, todo_id):
        todo = get_object_or_404(Todo, id=todo_id, delete_flag=False)

        character_id = todo.character.id

        todo.delete_flag = True
        todo.save()

        return redirect('dashboard:todo_list', character_id=character_id)

class TodoCompleteView(View):
    pass
