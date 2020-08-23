from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .models import Tweet

# Create your views here.
def home_view( request, *args, **kwargs):
    return render(request, "pages/home.html", context={}, status=200)


def tweet_detail_view( request,tweet_id, *args, **kwargs):

    """
    REST API VIEW
    Consumed by all
    """

    data ={
        "id": tweet_id,
        # "image_path": obj.image.url
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content']=obj.content
    except:
        data['message'] = "Not Found"
        status=404

    

    return JsonResponse(data, status=status) #json.dumps content_type=application/json

    #return HttpResponse(f"<h1>You are {tweet_id} - {obj.content}</h1>")
