#!/bin/sh

if [ $# -lt 1 ]; then
    uiFiles=`ls *.ui`
else
    uiFiles=$@
fi

for uiFile in $uiFiles; do
    echo "Processing $uiFile"
    filename=`basename $uiFile .ui`
    echo "Writing as ../lib/autokey/qt5ui/$filename.py"
    pyuic5 -o ../lib/autokey/qt5ui/$filename.py $uiFile
done

exit 0
