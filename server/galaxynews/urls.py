from django.urls import path
from .views import *

urlpatterns = [
    path('post/create/', PostCreateView.as_view()),
    path('post/list/', PostListView.as_view()),
    path('post/update/<int:pk>', PostUpdateView.as_view()),

    path('tag/create/', TagCreateView.as_view()),
    path('tag/list/', TagListView.as_view()),
    path('tag/update/<int:pk>', TagUpdateView.as_view()),

    path('category/create/', CategoryCreateView.as_view()),
    path('category/list/', CategoryListView.as_view()),
    path('category/update/<int:pk>', CategoryUpdateView.as_view()),

]
