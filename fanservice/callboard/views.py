from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)

from django.urls import reverse_lazy
from .models import Advert, UserResponse
from .form import AdvertForm, UserResponseForm


from utils.filters import UserResponseFilter

class AdvertList(ListView):
    """Все объявления"""
    model = Advert
    queryset = Advert.objects.all()
    template_name = "callboard/advert-list.html"


class AdvertDetail(DetailView):
    """Подробно об объявлении"""
    model = Advert
    queryset = Advert.objects.all()
    context_object_name = "advert"
    template_name = "callboard/advert-detail.html"


class AdvertCreate(CreateView):
    """Добавление объявления"""
    form_class = AdvertForm
    model = Advert
    template_name = 'callboard/advert_edit.html'


class AdvertUpdate(UpdateView):
    """Редактирование объявления пользователя"""
    form_class = AdvertForm
    model = Advert
    template_name = 'callboard/advert_edit.html'


class AdvertDelete(DeleteView):
    """Удаление объявления пользователя"""
    model = Advert
    template_name = 'callboard/advert-delete.html'
    success_url = reverse_lazy('advert-list')

class UserResponseList(ListView):
    """Все отклики пользователя"""
    model = UserResponse
    queryset = UserResponse.objects.all()
    template_name = "callboard/user_response_list.html"

    def get_queryset(self):
        return UserResponse.objects.filter(user=self.request.user)

class UserResponseCreate(CreateView):
    """Добавление отклика"""
    form_class = UserResponseForm
    model = UserResponse
    template_name = 'callboard/user_response_edit.html'
    success_url = reverse_lazy('advert-list')

class SearchUserResponseList(ListView):
    model = UserResponse
    ordering = 'subject'
    template_name = 'callboard/user_response_list_search.html'
    context_object_name = 'newsposts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = UserResponseFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context
