from datetime import date
import os
import shutil

# ----------- Adjustable vartiables --------------

from_dir = "F:\\mystuff"
archive_path = "I:\\mystuff_archive"

# ----------- Assertions and prerequisites -----------

# Check if the destination directory exists
assert os.path.exists("I:\\"), "\n\n ** Destination drive not attached. Attach" \
                               "drive %s before proceeding **\n" % "I:\\"  \

# check if the from directory exists
assert os.path.exists(from_dir), "\n\n ** From folder \"%s\" does not exist." \
                                       "Check directory spelling. **\n" % from_dir  \
                               
# If the archive has not yet been made, create this directory                               
if not os.path.exists(archive_path):
    os.mkdir(archive_path)
    
# creat destination folder name and date
date_today = date.today().isoformat()
dest_folder = os.path.join(archive_path, date_today)

assert not os.path.exists(dest_folder), "Already backed up today."
 
# back that thang up
print("Backing up.")
try:
    shutil.copytree(from_dir, dest_folder)    
except shutil.Error, exc:
    errors = exc.args[0]
    for error in errors:
        src, dst, msg = error
        print(src, dst, msg)
    
print("All done backing up.")