# Python File Management Scripts
Scripts for (Ubuntu) file management

bulk_rename.py: Renames all of the files within a given folder to a given name plus an index starting from 0. Ignores files starting with a . ,for example .gitignore will not be renamed.

Run from the command line in the folder the python file is with python bulk_rename.py with the following tags:

-d or --directory: The path to the folder, for example ~/test/. Always end the path with a '/'. This is a reguired tag, the script won't work without it

-n or --name: The name you want to rename the files to. If not used, the program will name the files with numbers starting from 0.

-t or --filetype: If you want your files to end in with a filename extension, for example .txt, give it with this tag.


