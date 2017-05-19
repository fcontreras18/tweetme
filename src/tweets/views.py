from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView

from .forms import TweetModelForm
from .mixins import FormUserNeededMixin
from .models import Tweet

# Create/Retrieve/Update/Delete

# Create
class TweetCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    success_url = '/tweet/create/'
    # login_url = '/admin/'

    # def form_valid(self, form):
    #     if self.request.user.is_authenticated():
    #         form.instance.user = self.request.user
    #         return super(TweetCreateView, self).form_valid(form)
    #     else:
    #         form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["User must be logged in to continue"])
    #         return self.form_invalid(form)


# def tweet_create_view(request):
#     form = TweetModelForm(request.POST or None)
#     if form.is_valid():
#         instance = form.save(commit=false)
#         instance.user = request.user
#         instance.save()
#     content = {
#         "form":form
#     }
#     return render(request, 'tweets/create_view.html', context)


# Retrieve
class TweetDetailView(DetailView):
    # template_name = "tweets/tweet_detail_view.html"
    queryset = Tweet.objects.all()

    # def get_object(self):
    #     print(self.kwargs)
    #     pk = self.kwargs.get("pk")
    #     print(pk)
    #     return Tweet.objects.get(id=pk)

class TweetListView(ListView):
    # template_name ="tweets/list_view.html"
    queryset = Tweet.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        # context["another_list"] = Tweet.objects.all()
        # print(context)
        return context


# def tweet_detail_view(request, id=1):
#     obj = Tweet.objects.get(id=id) # GET from database
#     print(obj)
#     context = {
#         "object": obj
#     }
#     return render(request, "tweets/detail_view.html", context)


# def tweet_list_view(request):
#     queryset = Tweet.objects.all()
#     print(queryset)
#     for obj in queryset:
#         print(obj.content)
#     context = {
#         "object_list": queryset
#     }
#     return render(request, "tweets/list_view.html", context)