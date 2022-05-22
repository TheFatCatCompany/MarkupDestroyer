import requests
from collections import namedtuple

MarkupListing = namedtuple("MarkupListing", ["year", "manufacturer", "model", "markup", "notes"])
DealerLocation = namedtuple("DealerLocation", ["state", "name"])
def scrapeForMarkups():
    pagenum = 1
    DealerMarkups = {}
    while pagenum < 25:
        url = "https://markups.org/all?page=" + str(pagenum)
        page = requests.get(url)
        pagehtml = [s.strip() for s in page.text.split("\n")]
        itemindicies = [index for (index, item) in enumerate(pagehtml) if item == '<div class="tw-flex-1">']
        for index in itemindicies:
            notes = ""
            dealernamestring = pagehtml[index + 3]
            dealername = dealernamestring[dealernamestring.index("</span>") + 7: dealernamestring.index("</div>")].strip()
            markupstring = pagehtml[index + 6]
            markup = markupstring[markupstring.index("</span>") + 7: markupstring.index("</div>")].strip()
            statestring = pagehtml[index + 9]
            state = statestring[statestring.index("</span>") + 7: statestring.index("</div>")].strip()
            yearstring = pagehtml[index + 12]
            year = yearstring[yearstring.index("</b>:") + 5: yearstring.index("</div>")].strip()
            carstring = pagehtml[index + 14]
            manufacturer = carstring[carstring.index('bold">') + 6: carstring.index("</b>:")].strip()
            model = carstring[carstring.index("</b>:") + 5: carstring.index("</div>")].strip()
            NewCar = (year, manufacturer, model, markup, notes)
            if state not in DealerMarkups:
                DealerMarkups[state] = {}
                DealerMarkups[state][dealername] = [NewCar]
            else:
                if dealername not in DealerMarkups[state]:
                    DealerMarkups[state][dealername] = [NewCar]
                else:
                    DealerMarkups[state][dealername].append(NewCar)
                print(NewCar)
        pagenum += 1
    return DealerMarkups




        
        



