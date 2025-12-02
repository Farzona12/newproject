from django.views import generic
from .models import Market

class MarketCreateView(generic.CreateView):
    model = Market
    template_name = "market/market_create.html"
    fields = ("name", "description", "address", "image")
    success_url = "/market/market_list/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class MarketListView(generic.ListView):
    model = Market
    template_name = "market/market_list.html"
    context_object_name = "markets"
    queryset = Market.objects.all().order_by("-id")


class MarketDetailView(generic.DetailView):
    model = Market
    template_name = "market/market_detail.html"
    context_object_name = "market"

class MarketUpdateView(generic.UpdateView):
    model = Market
    template_name = "market/market_update.html"
    fields = ("name", "description", "address", "image")
    success_url = "/market/market_list/"


class MarketDeleteView(generic.DeleteView):
    model = Market
    template_name = "market/market_delete_confirm.html"
    success_url = "/market/market_list/"
