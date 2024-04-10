from django.views.generic import TemplateView


class Error404View(TemplateView):
    template_name = 'errors/404.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context, status=404)


class Error403View(TemplateView):
    template_name = 'errors/403.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context, status=403)


class Error500View(TemplateView):
    template_name = 'errors/500.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context, status=500)


class AboutView(TemplateView):
    template_name = 'common/about_page.html'
