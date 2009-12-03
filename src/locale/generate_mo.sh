#!/bin/bash
for lang in $(find . -mindepth 1 -maxdepth 1 -type d | cut -c3-); do
    pushd $lang
    msgfmt $lang.po -o LC_MESSAGES/debian-rt.mo
    popd
done
