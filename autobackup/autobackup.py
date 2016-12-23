"""Copyright (C) 2016 Adam Deeley

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

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