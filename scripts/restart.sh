#!/bin/bash

kill $(pidof python) && gunicorn -b 0.0.0.0:8000 settings.wsgi &
