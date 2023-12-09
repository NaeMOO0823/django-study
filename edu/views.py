from django.views.generic import View
from django.shortcuts import get_object_or_404, render,redirect
from .models import Feed
from django.views.generic import View, DetailView

class Index(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)
    

class TagStudy(View):
    template_name = 'tag_study.html'

    def get(self, request):
        feeds = Feed.objects.all().order_by("id")

        return render(
            request,
            self.template_name,
            {'feed_list' : feeds}
            )
    
class NewContent(View):
    template_name = 'upload_form.html'

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        age = request.POST.get('age', '0')
        age = int (age)

        pwd = request.POST.get('pwd', '')
        print(f'비밀번호:{pwd}')

        tel = request.POST.get('phone', '')
        print(f'전화번호:{tel}')

        param = request.POST.get("content", '')
        param2 = request.FILES.get('up_photo', False)
        print("전달받은 내용:" + param)
        feed = Feed(content=param, photo = param2)
        feed.save()

        return redirect('edu:tag_study')
    
class Survey(View):
    template_name = 'survey.html'

    def get(self, request):
        return render(request, self.template_name)

class Palgong(View):
    template_name = 'palgong.html'

    def get(self, request):
        return render(request, self.template_name)
        
    def post(self, request):
        param = request.POST.get('tea', '')
        print(f"param = {param}")
        return redirect("edu:tag_study")
        
class FeedDetail(DetailView):
    model = Feed
    template_name = "feed/detail.html"
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        feed = get_object_or_404(Feed, pk = self.kwargs['pk'])
        context['feed'] = feed

        return context