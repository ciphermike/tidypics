# tidypics

## Description

This tool is to clean duplicate pictures / media files.

This first version allows to move any files from a <src_dir> inluding sub-directory tree to a destination folder. 
If duplicate is detected, the destination file is renamed by appending a random string.
The <src_dir> is deleted once empty.
This version detects duplicated only by name.

## Usage 
```bash
python tidypics.py <src_dir> <dest_dir> [-v]
-v stands for verbose mode.