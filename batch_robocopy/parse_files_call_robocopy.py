# Do a batch file copy using robocopy
# This is to solve the problem that default windows copy from network
# drives got interrupted by "Error 0x8007003B: An unexpected network error occurred"
# robocopy can copy files and resume copying after it's interrupted
# This script can parse list of files and feed them to robocopy
# 
# For single file to copy, use below command
# robocopy "c:\source_dir" "c:\destination_dir" file_name_1.pdf /LOG+:copy.log /TEE /Z
#
# /LOG+:copy.log - To keep and append(+) a log file
# /TEE - To also display the log and progress in the command window
# /Z - Flag to allow resume copying after interrupted (This is an important flag)

# from subprocess import check_output
import subprocess
import pandas as pd
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
file_path = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(file_path)

df = pd.read_csv(file_path, names=['from_dir', 'to_dir', 'file_name'], sep=',', header=0, index_col=False)
df = df.reset_index()  # make sure indexes pair with number of rows
for index, row in df.iterrows():
    cmd_str = 'robocopy \"' + str(row['from_dir']).replace('\\', '/')
    cmd_str = cmd_str + '\" \"'
    cmd_str = cmd_str + str(row['to_dir']).replace('\\', '/')
    cmd_str = cmd_str + '\" '
    cmd_str = cmd_str + str(row['file_name'])
    cmd_str = cmd_str + ' /LOG+:batch_robocopy.log /TEE /Z'

    print('\n' + cmd_str + '\n')

    # check=False, because robocopy return non 0
    subprocess.run(cmd_str, shell=True, check=False)
    
print('robocopy task completed')
