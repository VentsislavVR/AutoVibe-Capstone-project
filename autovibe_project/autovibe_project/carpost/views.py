from django.shortcuts import render
from django.views import generic as views
# Create your views here.
class CreateCarPostView(views.CreateView):
    pass


class DetailsCarView(views.DetailView):
    pass


class UpdateCarView(views.UpdateView):
    pass


class DeleteCarView(views.DeleteView):
    pass