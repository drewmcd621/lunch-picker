from picker.models import History, Restaurant, Option
import pprint

def get_choices():
    exclude = []
    #First see if there are vetoed options
    vetoes = Option.objects.filter(vetoed=True)
    for v in vetoes:
        exclude.append(v.restaurant.id)

    #Next get last resturaunt chosen
    last = History.objects.order_by("-date").first()
    exclude.append(last.restaurant.id)
    #Now lets get the set of places that aren't excluded
    opts = Restaurant.objects.exclude(id__in=exclude).order_by('?')

    #Remove old options
    Option.objects.all().delete()

    for i in range(0, 3):
        if opts[i]:
            o = Options()
            o.restaurant = opts[i]
            o.save()
