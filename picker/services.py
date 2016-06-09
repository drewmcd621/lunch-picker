from picker.models import Histoy, Restaurant, Options
import pprint

def get_choices():
    exclude = []
    #First see if there are vetoed options
    vetoes = Options.objects.filter(vetoed=True)
    for v in vetoes:
        exclude.append(v.restaurant.id)

    #Next get last resturaunt chosen
    last = History.object.order_by("-date").first()
    exclude.append(last.resturaunt.id)
    #Now lets get the set of places that aren't excluded
    pprint.pprint(exclude)
    opts = Restaurant.objects.exclude(id__in=exclude)


def veto_power():
    #

def end_vote():
    #

if __name__ == "__main__":
    get_choices()
