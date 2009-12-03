#!/bin/bash
for lang in $(find . -mindepth 1 -maxdepth 1 -type d | cut -c3-); do
    msgmerge -U $lang/$lang.po messages.pot
done
