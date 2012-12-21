#!/usr/bin/python

""" 
Moves content from a user's home directory to another directory, this is
useful when you're on a box where a user might not have the proper permissions to chown
files. You can set this to run on a cron job to avoid manually moving content.
"""

import os
import shutil
import sys
import hashlib

# Set the user id and the gid, you can get this by using id $user.
userID = 974
groupID = 752

# Set the From and To paths for the content copy.
pathFrom = '/home/user/test/'
pathTo = '/home/user/test2/'
# An example of pathFrom = '/home/user/test/'
# An example of pathTo = '/home/user/test2/'

for uploadedFile in os.listdir(pathFrom):
        # Checks if the path exists once we scan through the from dir.
        if os.path.exists(pathTo + uploadedFile):
                # This section just compares the md5 data to see if the file changed.
                md5FileFrom = hashlib.sha224(open(pathFrom + uploadedFile).read()).hexdigest()
                md5FileTo = hashlib.sha224(open(pathTo + uploadedFile).read()).hexdigest()
                
                if md5FileFrom != md5FileTo:
                        #Copies the file, then chowns it if the md5 data doesn't match.
                        shutil.copy(pathFrom + uploadedFile, pathTo + uploadedFile)
                os.chown(pathTo + uploadedFile, userID, groupID)

        else:
                # Copies the file and chowns it if it doesn't already exist.
                shutil.copy(pathFrom + uploadedFile, pathTo + uploadedFile)
                os.chown(pathTo + uploadedFile, userID, groupID)


