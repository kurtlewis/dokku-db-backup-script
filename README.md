# Dokku Backup
I've created this script as a way of automating dokku backups. I use the dokku mongodb extension for a lot of projects, and having automated backups is better than manually doing them. To facilitate this, I've created this script.

## Dependencies
- Python3
- Private keys for ssh'ing

## Setup
First, replace the variable values at the top of the script with their appropriate values. 

Second, it is necessary to configure the server to facilitate password-less use of dokku. 

*!!!This is a security vulnerability - do so with caution!!!*

```shell
# Run this command to allow passwordless execution of dokku commands
$ sudo visudo
# Append the following to the end of the /etc/sudoers file
# Assuming username of my-dokku-backup-user-name
my-dokku-backup-user-name ALL = (root) NOPASSWD: /usr/bin/dokku
```
Finally, ensure that the user account you configured has the private key of the machine that will be used for backup.

You can now setup a cron job to run backup whenever needed.

