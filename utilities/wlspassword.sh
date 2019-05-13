#!/bin/bash
# Created: alexandru.dragut@db.com
# Capture and store the WebLogic Server password
# Version: 19.6.01
#########################################################
#set -x

if [ ! -e /Users/adragut/OracleWeblogicDomain/.wlspwd ]; then

    # Mask or hide de password input
    stty -echo
    echo -e "\nEnter the Oracle WebLogic  password, followed by [ENTER]:"
    read wlspwd
    # Disable the input masking
    stty echo
#    echo $wlspwd

    echo $wlspwd >> /Users/adragut/OracleWeblogicDomain/.wlspwd
#    cat /Users/adragut/OracleWeblogicDomain/.wlspwd
else
    echo "Oracle WebLogic password previously captured."
    echo "If incorrect please delete the file /Users/adragut/OracleWeblogicDomain/.wlspwd"
fi
