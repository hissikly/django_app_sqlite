from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView)
from .models import Entry
from django.views.generic import (
   ListView,
   DetailView,
   CreateView, #Импортируем дополнительное представление для создания записей.
   UpdateView, #Импортируем дополнительное представление для обновления записей.
   DeleteView, #Импортируем дополнительное представление для удаления записей.
) 

#like schemas
class EntryListView(ListView):
    model = Entry
    queryset = Entry.objects.all().order_by("-date_created")

class EntryDetailView(DetailView):
    model = Entry

class EntryCreateView(CreateView):
    model = Entry
    fields = ["title", "content"] #какие поля должны будут отображаться
    success_url = reverse_lazy("entry-list")

class EntryUpdateView(UpdateView):
    model = Entry
    fields = ["title", "content"]

    def get_success_url(self) -> str: #функция создает возможность пользователям отредактировавшим запись остаться на странице деталей статьи
        return reverse_lazy(
            "entry-detail",
            kwargs={"pk": self.entry.id}
        )
    
class EntryDeleteView(DeleteView):
    model = Entry
    success_url = reverse_lazy("entry-list")