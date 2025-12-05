from django.shortcuts import render
from .models import poll, Option
from django.views.generic import ListView, DetailView, RedirectView
from django.urls import reverse

# Create your views here.
def poll_list(req):
    polls = poll.objects.all()
    return render(req, "default/list.html", {'poll_list': polls, 'msg': 'Hello!'})

class PollList (ListView):
    model = poll

    #應用程式名稱/資料模型_list.html
    #default/poll_list.html

class PollView(DetailView):
    model = poll

    #default/poll_detail.htm
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        option_list = Option.objects.filter(poll_id=self.object.id)
        ctx['option_list'] = option_list
        return ctx
    
class PollVote(RedirectView):
   # redirect_url = "http://www.google.com/"

   def get_redirect_url(self, *args, **kwargs):
       option = Option.objects.get(id = self.kwargs['oid'])
       option.votes += 1
       option.save()
       #return "/poll/{}/".format(option.poll_id)
       #return f"/poll/{option.poll_id}"
       #return reverse('poll_view' , args = [option.poll_id])
       return reverse('poll_view' , kwargs={'pk': option.poll_id})
   