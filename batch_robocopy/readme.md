# Batch robocopy utility on Windows

This utility does batch copy using Windows built-in tool robocopy. It can resume copies when copy tasks are interrupted.

## Usage

### Step 1

Enter folders and files in a csv file, e.g. files_to_copy.csv. For each line in the csv file, from_dir, to_dir, file_name are the source file folder, destination file folder and filename, respectively. This csv file can be in any folder.

### Step 2

Run the python script parse_files_call_robocopy.py

### Step 3

Select the csv file from Step 1.

### Step 4

Examine the log file to make sure files are copied properly

## Required

Make sure required python modules are installed
