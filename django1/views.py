from django.views import View
from django.http import HttpResponse

class zargar(View):
    def get(self, request):
        return HttpResponse('zargar')
