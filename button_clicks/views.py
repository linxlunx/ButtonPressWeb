from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from button_clicks.models import ButtonClickLog
from django.utils import timezone
from django.conf import settings


def button_clicks_home(request):
    clicks = ButtonClickLog.objects.count()
    return render(request, 'button_clicks/home.html', {'clicks': clicks})


@login_required
def button_clicks_api_click(request):
    now = timezone.now()

    # get click count in certain seconds
    clicks = ButtonClickLog.objects.filter(
        user=request.user,
        created_at__gt=now - timezone.timedelta(seconds=settings.CLICK_LIMIT_SECONDS)
    )

    if clicks.count() >= settings.CLICK_LIMIT:
        # calculate waiting time
        allow_click_time = settings.CLICK_LIMIT_SECONDS - (now - clicks.first().created_at).seconds

        return JsonResponse({'status': 'error', 'message': 'Already doing {} clicks in {} seconds, please wait in'
                                                           ' {} seconds'.format(settings.CLICK_LIMIT,
                                                                       settings.CLICK_LIMIT_SECONDS, allow_click_time)
                                                           },
                            status=400)

    # insert new click
    ButtonClickLog(
        user=request.user
    ).save()

    return JsonResponse({'status': 'success', 'count': ButtonClickLog.objects.count()})
