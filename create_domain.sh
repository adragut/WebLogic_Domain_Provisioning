# ------------------------------------------------------------------------
# -- DISCLAIMER:
# --    This script is provided for educational purposes only. 
# --    It is NOT supported by Oracle World Wide Technical Support.
# --    The script has been tested and appears to work as intended.
# --    You should always run new scripts on a test instance initially.
# -- 
# ------------------------------------------------------------------------
#!/bin/sh
#set -x
source /Applications/OracleWebLogic/weblogic_domain/utilities/wlspassword.sh

#Delete domain if it already exists
rm -rf /Applications/OracleWebLogic/weblogic_domain/wlsadmin

source /Users/adragut/OracleWeblogic/Middleware/Oracle_Home/wlserver/server/bin/setWLSEnv.sh
java weblogic.WLST create_domain.py $(cat '/Applications/OracleWebLogic/weblogic_domain/.wlspwd')
