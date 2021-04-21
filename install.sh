#!/bin/bash

if [ $(id -u) == "0" ]
then

    cp "xthreader.py" "/usr/bin/xthreader"
    cp "xt_libx.py" "/usr/bin/xt_libx.py"

    chmod +x "xthreader.py" "/usr/bin/xthreader"

    printf "installation done.\n"

else

    printf "you should run the installation script as root:\n\n"
    echo "sudo $0"

fi
