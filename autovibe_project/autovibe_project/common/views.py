from django.views.generic import TemplateView

class Error404View(TemplateView):
    template_name = '404.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context, status=404)

class AboutView(TemplateView):
    template_name = 'common/about_page.html'