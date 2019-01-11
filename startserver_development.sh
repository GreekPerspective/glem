#!/bin/bash
if [ ! -z "$VIRTUAL_ENV" ]; then
    python setup.py develop
else
    echo "No virtual environment detected, you have to take care of  running setup.py install or setup.py develop yourself!">&2
fi
clamservice -d webglem.webglem
