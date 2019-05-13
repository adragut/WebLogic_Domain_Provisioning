# ------------------------------------------------------------------------
# -- Created: alexandru.dragut@db.com	
# -- Scope: This script has been create to automate WLS provisioning 12c. 
# -- Version: 19.6.0.1
##########################################################################
#!/bin/sh
#set -x
source /Users/adragut/OracleWeblogicDomain/utilities/wlspassword.sh

#Delete domain if it already exists
rm -rf /Users/adragut/OracleWeblogicDomain/Domain_US

source /Users/adragut/OracleWeblogic/Middleware/Oracle_Home/wlserver/server/bin/setWLSEnv.sh
java weblogic.WLST create_domain.py $(cat '/Users/adragut/OracleWeblogicDomain/.wlspwd')
