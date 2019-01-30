import os
print('Checking status of the git repository before staging the changes')
os.system('git status')
print('Adding the changes to the staging area')
os.system('git add .')
print('Checking the status of the git repository after staging the changes')
os.system('git status')
print('Commiting the changes')
os.system('git commit')
