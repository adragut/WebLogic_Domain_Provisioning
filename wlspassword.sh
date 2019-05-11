#!/bin/bash
#
# Capture and store the WebLogic Server password
#

if [ ! -e /Applications/OracleWebLogic/weblogic_domain/.wlspwd ]; then

    # Mask or hide de password input
    stty -echo
    echo -e "\nEnter the Oracle WebLogic  password, followed by [ENTER]:"
    read wlspwd
    # Disable the input masking
    stty echo
#    echo $wlspwd

    echo $wlspwd >> /Applications/OracleWebLogic/weblogic_domain/.wlspwd
#    cat /Applications/OracleWebLogic/weblogic_domain/.wlspwd
else
    echo "Oracle WebLogic password previously captured."
    echo "If incorrect please delete the file /Applications/OracleWebLogic/weblogic_domain/.wlspwd"
fi
