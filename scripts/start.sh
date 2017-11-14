#!/bin/bash

unicorn -b 0.0.0.0:8000 settings.wsgi &
