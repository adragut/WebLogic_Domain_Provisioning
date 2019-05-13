# Scope: Creates the domain when needed.
# Created: alexandru.dragut@db.com
# Version: 19.5.0.1
# ------------------------------------------------------------------------

# get operating system (for vars)
import os

# get regular expression module (for string manipulation)
import re
import sys

# paths
javapath = os.getenv('JAVA_HOME')

wlspath = os.getenv('WL_HOME')

# variables
templatefile = wlspath + '/common/templates/wls/wls.jar'
templatename = 'base_domain'
domainname = 'Domain_US_3'
domainpath = '/Users/adragut/OracleWeblogicDomain/' + domainname
startmode = 'prod'
username = 'weblogic'
password = sys.argv[1]
managed1name = 'US1'
managed2name = 'US2'
machine1name = 'machine1_US'
machine2name = 'machine2_US'
nodemgrport = 25556
clustername = 'cluster_US'
host1address = 'MacBook-Air-adragut.local'
host2address = 'MacBook-Air-adragut.local'

adminport = 27001
managedport = 27011


# Load the base template
readTemplate(templatefile)
print '>>>Domain template loaded: ' + templatefile

# Set domain options
setOption('JavaHome',javapath)
setOption('ServerStartMode',startmode)
setOption('OverwriteDomain','true')

# Set admin credentials
cd('/Security/' + templatename + '/User/' + username)
cmo.setPassword(password)
print '>>>Admin user created.'

# create the first machine
cd('/')
create(machine1name, 'Machine')
cd('/Machine/' + machine1name)
create(machine1name, 'NodeManager')
cd('NodeManager/' + machine1name)
set('ListenAddress', host1address)
set('ListenPort', nodemgrport)
set('NMType', 'Plain')
print '>>>' + machine1name + ' created.'

# create the second machine
cd('/')
create(machine2name, 'Machine')
cd('/Machine/' + machine2name)
create(machine2name, 'NodeManager')
cd('NodeManager/' + machine2name)
set('ListenAddress', host2address)
set('ListenPort', nodemgrport)
set('NMType', 'Plain')
print '>>>' + machine2name + ' created.'

# Update admin server
cd('/Servers/AdminServer')
set('ListenAddress', host1address)
set('ListenPort', adminport)
set('Machine', machine1name)
print '>>>Admin server updated.'

# create first managed server
cd('/')
create(managed1name, 'Server')
cd('Servers/' + managed1name)
set('ListenAddress', host1address)
set('ListenPort', managedport)
set('Machine', machine1name)
print '>>>' + managed1name + ' created.'

# create second managed server
cd('/')
create(managed2name, 'Server')
cd('Servers/' + managed2name)
set('ListenAddress', host2address)
set('ListenPort', managedport)
set('Machine', machine2name)
print '>>>' + managed2name + ' created.'

# create the cluster & assign servers
cd('/')
create(clustername, 'Cluster')
cd('/')
assign('Server', managed1name, 'Cluster', clustername)
assign('Server', managed2name, 'Cluster', clustername)
print '>>>' + clustername + ' created and managed servers added to it.'

# Write domain to file system
writeDomain(domainpath)
closeTemplate()
print '>>>Domain created successfully at ' + domainpath + '.'

# create boot.properties for admin server / managed servers
os.mkdir(domainpath + '/servers')
os.mkdir(domainpath + '/servers/AdminServer')
os.mkdir(domainpath + '/servers/AdminServer/security')
bootFile = open(domainpath + '/servers/AdminServer/security/boot.properties', 'w')
bootFile.write('username=' + username + '\n')
bootFile.write('password=' + password + '\n')
bootFile.close()
print '>>>Created boot.properties for admin server.'

#import pdb; pdb.set_trace()
# update node manager.properties
text = open(domainpath + '/nodemanager/nodemanager.properties').read()
text = re.sub('SecureListener=true', 'SecureListener=false', text)
text = re.sub('NativeVersionEnabled=true', 'NativeVersionEnabled=false', text)
open(domainpath + '/nodemanager/nodemanager.properties', 'w').write(text)
print '>>>Updated nodemanager.properties so it is no longer expecting a secure listener.'

#text1 = open(domainpath + '/nodemanager/nodemanager.properties').read()
#text1 = re.sub('NativeVersionEnabled=true', 'NativeVersionEnabled=false', text1)
#open(domainpath + '/nodemanager/nodemanager.properties', 'w').write(text1)
#print '>>>Updated nodemanager.properties so native librieries are set to false now.'
