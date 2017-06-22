"""
Kurt Lewis
Instructions:
Set the following variables and setup a cron job to regurarly run the script!
"""
# VARIABLES TO SET
serverIp = '0.0.0.0' # IP of server
serverUser = 'username' # User on server with access to dokku. Should have ssh keys configured for passwordless login
dbName = 'db-name' # Name of db on dokku instance
storageLocation = '.' # Location to store backups - full path preferred
createMonthFolders = True # set to True to store in folders structure 'month/backup' inside 'Location/'
# END VARIABLES TO SET

from subprocess import call
import time
import os

# Create filename
dateString = time.strftime('%d-%m-%Y', time.gmtime())
filename = dbName + '-' + dateString + '.dump.tar'

# Create ssh command
sshCmd = 'ssh ' + serverUser + '@' + serverIp + ' '
createBackupCmd = sshCmd + '"dokku mongo:export ' + dbName + ' > ' + filename + '"'

# create location and directory
if createMonthFolders:
    storageLocation = storageLocation + '/' + time.strftime('%B-%Y', time.gmtime())
    if not os.path.exists(storageLocation):
        call(["mkdir", storageLocation])

# Create scp command
storageLocation =  storageLocation + '/' + filename
scpCmd = 'scp ' + serverUser + '@' + serverIp + ':' + filename + ' ' + storageLocation

# Create delete command
deleteBackupOnServerCmd = sshCmd + '"rm ' + filename + '"'

print(createBackupCmd)
print(scpCmd)
print(deleteBackupOnServerCmd)

# call(createBackupCmd)
# call(scpCmd)
# call(deleteBackupOnServerCmd)