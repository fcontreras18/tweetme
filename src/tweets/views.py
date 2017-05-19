from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView
from .forms import TweetModelForm
from .models import Tweet
# Create your views here.
# Create/Retrieve/Update/Delete

# Create
class TweetCreateView(CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    success_url = '/tweet/create/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed
        # It should retrun an HttpResponse
        form.instance.user = self.request.user
        return super(TweetCreateView, self).form_valid(form)


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