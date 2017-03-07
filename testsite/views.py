import random

from django.shortcuts import render

def pathed_view(request, pk_sorta_lol):
    ctx = {
        'rand_pool': [random.randint(0,255) for _ in xrange(5)],
        'thing': pk_sorta_lol
    }

    return render(request, 'testsite/pathed_template.html', ctx)
