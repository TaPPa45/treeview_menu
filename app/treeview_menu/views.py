from django.views.generic import TemplateView


class MenuPageView(TemplateView):
    template_name = "page.html"
    page_title = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = self.kwargs.get("page_title", "Default Page")
        return context
