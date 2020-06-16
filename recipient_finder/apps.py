import os

import pickle5 as pickle

from django.apps import AppConfig
from django.conf import settings


class RecipientFinderConfig(AppConfig):
    name = 'recipient_finder'
    # create path to models
    path = os.path.join(settings.MODELS, 'k.sav')
    with open(path, 'rb') as pickled:
        model_ = pickle.load(pickled)
