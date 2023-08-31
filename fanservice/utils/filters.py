from django_filters import FilterSet

from callboard.models import UserResponse

# Создаем свой набор фильтров
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.


class UserResponseFilter(FilterSet):
     class Meta:
       # В Meta классе мы должны указать Django модель,
       # в которой будем фильтровать записи.
         model = UserResponse
       # В fields мы описываем по каким полям модели
       # будет производиться фильтрация.
         fields = {
           # поиск по названию
             'advert': ['exact'],
         }