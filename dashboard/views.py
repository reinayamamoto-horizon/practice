from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from accounts.models import Todo,Character
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction


class IndexView(LoginRequiredMixin,View):
    def get(self, request):
        character = request.user.character
        todo = Todo.objects.filter(character=character, delete_flag=False,display_flag=True)
        now = timezone.now()
        #経験値計算
        MAX_EXP = 100
        #割合計算(0〜100に収める)
        exp_percentage = min((character.exp / MAX_EXP) * 100, 100)
            
        context = {
            "character": character,
            "current_level": character.level,
            "character_name": character.character_name,
            "exp_total_data": character.exp,
            "character_standing_img":character.image_url.url,
            "todo_list": todo,
            "current_time": now,
            "evolution_button": request.session.get("evolution_ticket", 0) > 0,
            "evolution_ticket": request.session.get("evolution_ticket", 0),
            "exp_current_data": f"{character.exp} / {MAX_EXP}",
            "exp_percentage": exp_percentage,
            
        }
        return render(request, "dashboard/Index.html", context)
        
    def save(self, *args, **kwargs):
        #一定値以上になったらレベルアップ
        if self.exp >= 100:
            self.level += 1
            #100の時0に戻す
            self.exp = (self.exp - 100)
        
        super().save(*args, **kwargs)

        
class TodoListView(View):
    def get(self, request):
        character = request.user.character

        todos = Todo.objects.filter(
            character=character,
            delete_flag=False,
            display_flag=True,
        ).order_by("-created_at")

        context = {
            "todos_A": todos.filter(rank='A'),
            "todos_B": todos.filter(rank='B'),
            "todos_C": todos.filter(rank='C'),
        }
        return render(request, "dashboard/todo_list.html", context)


class TodoCreateView(LoginRequiredMixin,View):
    def get(self, request):
        character = request.user.character
        return render(request, 'dashboard/todo_create.html', {
            'character': character,
        })

    def post(self, request):
        character = request.user.character

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

        return redirect("dashboard:todo_list")

class TodoDetailView(View):
    def get(self, request, todo_id):
        todo = get_object_or_404(
            Todo,
            id=todo_id,
            delete_flag=False,
            display_flag=True,
        )
        return render(request, 'dashboard/todo_detail.html', {
            'todo': todo,
            'character': todo.character,
        })

    def post(self, request, todo_id):
        todo = get_object_or_404(
            Todo,
            id=todo_id,
            delete_flag=False,
            display_flag=True,
        )
        return render(request, 'dashboard/todo_detail.html', {
            'todo': todo,
            'character': todo.character,
        })

class TodoEditView(View):
    def get(self, request, todo_id):
        todo = get_object_or_404(
            Todo,
            id=todo_id,
            delete_flag=False,
            display_flag=True,
        )

        return render(request, 'dashboard/todo_edit.html', {
            'todo': todo,
            'character': todo.character,
        })

    def post(self, request, todo_id):
        todo = get_object_or_404(
            Todo,
            id=todo_id,
            delete_flag=False,
            display_flag=True,
        )

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
        todo = get_object_or_404(
            Todo,
            id=todo_id,
            delete_flag=False,
            display_flag=True,
        )

        todo.delete_flag = True
        todo.save()

        return redirect('dashboard:todo_list')


POINT_MAP = {
    'A': 50,
    'B': 30,
    'C': 10,
}

class TodoCompleteView(View):
    def post(self, request, todo_id):
        todo = get_object_or_404(
            Todo,
            id=todo_id,
            delete_flag=False,
            display_flag=True,
        )
        character = todo.character
        point = POINT_MAP.get(todo.rank, 0)

        with transaction.atomic():

            todo.display_flag = False
            todo.save(update_fields= ["display_flag"])

            level_up_count = 0
            character.exp += point
            
            while character.exp >= 100:
                character.exp -= 100
                character.level += 1
                level_up_count += 1

            character.save(update_fields=["exp", "level"])

            # レベルアップ回数ぶん進化チケットを付与
            if level_up_count > 0:
                request.session["evolution_ticket"] = (
                    request.session.get("evolution_ticket", 0) + level_up_count
                )

        return redirect("dashboard:todo_list")

