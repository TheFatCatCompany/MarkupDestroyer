"""
This script runs the AntiMarkup application using a development server.
"""
import json
import asyncio
from os.path import exists
from os import environ
from AntiMarkup import app
from collections import namedtuple
from markupScraper import scrapeForMarkups, MarkupListing, DealerLocation

if __name__ == '__main__':
    if not exists(r"AntiMarkup\static\markups.json"):
        markupDict = scrapeForMarkups()
        with open(r"AntiMarkup\static\markups.json", "w") as outfile:
            json.dump(markupDict, outfile)
    '''
       async def doScraping():
       markupDict = await asyncio.coroutine(scrapeForMarkups)()
       with open(r"AntiMarkup\static\markups.json", "w") as outfile:
           json.dump(markupDict, outfile)
       await asyncio.sleep(3600)
    loop = asyncio.get_event_loop()
    task = loop.create_task(doScraping())

    try:
        loop.run_until_complete(task)
    except asyncio.CancelledError:
        pass
    '''
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
