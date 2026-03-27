from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.db import transaction
from accounts.models import Todo,Character 



class EXPbarView(View):
    pass


class TodoListView(View):
    def get(self, request,character_id):
        character = get_object_or_404(Character, id=character_id)

        todos = Todo.objects.filter(
            character=character,
            delete_flag=False,
            display_flag=True
        )

        context = {
            "todos_A": todos.filter(rank='A'),
            "todos_B": todos.filter(rank='B'),
            "todos_C": todos.filter(rank='C'),
        }
        return render(request, "dashboard/todo_list.html", context)

        def post(self, request, todo_id):
            todo = get_object_or_404(Todo, id=todo_id, delete_flag=False)

            return render(request, 'dashboard/todo_detail.html', {
                'todo': todo,
                'character': todo.character,
            })

class TodoCreateView(View):
    def get(self, request, character_id):
        character = get_object_or_404(Character, id=character_id)
        context["character"] = character
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


POINT_MAP = {
    'A': 50,
    'B': 30,
    'C': 10,
}

class TodoCompleteView(View):
    def post(self, request, todo_id):
        todo = get_object_or_404(Todo, id=todo_id, delete_flag=False)
        character = todo.character.id

        if not todo.display_flag:
            return redirect("dashboard:todo_list", character_id=character.id)
    
        if getattr(todo, "is_completed", False):
            return redirect("dashboard:todo_list", character_id=character.id)

        point = POINT_MAP.get(todo.rank, 0)

        with transaction.atomic():
            todo.display_flag = False
            todo.save(update_fields= ["display_flag"])
            character.exp += point
            character.save(update_fields=["exp"])
        return redirect("dashboard:todo_list", character_id=character.id)

