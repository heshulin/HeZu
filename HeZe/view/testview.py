from HeZe.models import SendHezu
from HeZe.bean.lbs_amap import get_distance, get_around
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def f(request):
    list = []
    res = SendHezu.objects.filter().all()
    for i in res:
        state, distance = get_distance('111.688844,40.814395', i.Address)
        if state == 1:

            if distance <= 200000:
                array = {
                    'UserId': i.UserId,
                    'Information': i.Information,
                    'Address': i.Address,
                    'Picture': i.Picture,
                    'PictureEx': i.Picture.replace('?imageView2/0/w/200/h/200/format/png/interlace/1/', ''),
                    'Number': i.Number,
                    'distance': distance
                }
                list.append(array)
    list = sorted(list, key=lambda list: list['distance'])
    for i in list:
        print(i['distance'])
    return HttpResponse('111')