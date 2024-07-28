from django_unicorn.components import UnicornView
from django import forms
from ..models import TodoItem

class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ['title', 'completed']

class TodoView(UnicornView):
    task = ""
    todo_items = TodoItem.objects.all()
    form_class = TodoForm
    
    def add_task(self):
        form = self.form_class({'title': self.task, 'completed': False})
        if form.is_valid():
            form.save()
            self.todo_items = TodoItem.objects.all()
            self.task = ""
            
    def update_task(self, task_id):
        task = TodoItem.objects.get(id=task_id)
        task.completed = not task.completed
        task.save()
        self.todo_items = TodoItem.objects.all()


    def delete_task(self, task_id):
        print(task_id)
        TodoItem.objects.get(id=task_id).delete()
        self.todo_items = TodoItem.objects.all()
        
    def reset(self):
        self.todo_items = TodoItem.objects.all()
        self.task = ""
        print("Reset method called")
