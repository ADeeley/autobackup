"""Copyright (C) 2017 Adam Deeley

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


def gen_dest_folder(src, dst):
    """ Checks that the folders given exist and creates a 
        new folder with today's date for backup.
        * Pre: Assumes that src and dst are valid system locations
          Pre: src == str and dst == str
        * Post: dst is valid file path
    """
    
    # Generate destination folder name and date
    date_today = date.today().isoformat()
    dst = os.path.join(dst, date_today)

    if not os.path.exists(dst):
        os.mkdir(dst)
        assert os.path.isdir(dst) == True, "Failed to create the destination path."
    else:
        answer = input("Already backed up today. Back up again? (y/n)\n")
        if answer == "y":
            return dst
        else:
            print("Backup procedure aborted")
            quit()
    return dst


def backup(src, dst):
    """ Backs up the source file to the destination file.
        * Pre - dst == string""" 
    print("Backing up.")
   
    errors = []

    shutil.copytree(src, dst)    
 

def auto_backup(src, dst):
    """ Runs the autobackup process """
    # Check if the destination directory exists
    assert os.path.exists(dst[:3]), """\n\n ** Destination drive not attached. Attach
                                        drive {0} before proceeding **\n""".format(dst[:3]) 
    assert os.path.exists(src), """\n\n ** From folder {0} does not exist.
                                    Check directory spelling. **\n""".format(src)                        
    newDst = gen_dest_folder(src, dst)
    backup(src, newDst)


#src = "F:\\mystuff"
dst = "G:\\mystuff_archive"
src = "F:\\test" 
auto_backup(src, dst)
