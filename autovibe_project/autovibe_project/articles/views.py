from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins
from autovibe_project.articles.models import Article


# Create your views here.
class ArticlesListView(views.ListView):
    template_name = 'articles/list_articles.html'
    model = Article
    paginate_by = 3


class ArticlesDetailView(auth_mixins.LoginRequiredMixin,views.DetailView):
    template_name = 'articles/details_articles.html'
    model = Article


class ArticlesCreateView(PermissionRequiredMixin,auth_mixins.LoginRequiredMixin, views.CreateView):
    template_name = 'articles/create_article.html'
    model = Article
    fields = ['name', 'article_img', 'content']
    permission_required = 'articles.add_article'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('article_details',
                            kwargs={
            'pk': self.object.pk,
            'slug': self.object.slug
                            })


class ArticlesUpdateView(PermissionRequiredMixin,auth_mixins.LoginRequiredMixin,views.UpdateView):
    template_name = 'articles/update_articles.html'
    model = Article
    permission_required = 'articles.change_article'

    fields = ['name', 'article_img', 'content']

    def get_success_url(self):
        return reverse_lazy('article_details',
                            kwargs={
                                'pk': self.object.pk,
                                'slug': self.object.slug
                            })


class ArticlesDeleteView(PermissionRequiredMixin,auth_mixins.LoginRequiredMixin,views.DeleteView):
    template_name = 'articles/delete_articles.html'
    model = Article
    permission_required = 'articles.delete_article'
    success_url = reverse_lazy('articles_list')
