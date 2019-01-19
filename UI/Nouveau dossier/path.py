"""
import os
print(os.getcwd())
print(os.path.dirname())
"""

from os import path
stpath = str(path.abspath(path.curdir))  # r"I:\py\ERP\UI"
# print(path.curdir)
print(path.abspath(stpath))
print(path.dirname(path.abspath(path.curdir)))
print(path.basename(stpath))

stpath = path.abspath(path.curdir)
pixmap = r'{}\images\login-user-icon.png'.format(stpath)

print(pixmap)
