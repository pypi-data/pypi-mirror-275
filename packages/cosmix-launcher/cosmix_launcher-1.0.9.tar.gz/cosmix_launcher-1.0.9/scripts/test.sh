#!/usr/bin/sh

# THIS SCRIPT IS FOR DEVELOPERS
# It rebuilds and reinstalls Cosmix to the user's Python installation.
# If you are not a developer then I highly advise against using this script.

rm ./dist/*
/usr/bin/python3 -m build && /usr/bin/python3 -m pip install \
    --user --force-reinstall --break-system-packages \
    ./dist/*.whl
