# Python File Management Scripts
Scripts for (Ubuntu) file management

bulk_rename.py: Renames all of the files within a given folder to a given name plus an index starting from 0. Ignores files starting with a . ,for example .gitignore will not be renamed.

Run from the command line in the folder the python file is with python bulk_rename.py with the following tags:

-d or --directory: The path to the folder, for example ~/test or ~/Documents/ . 

-n or --name: The name you want to rename the files to. If not used, the program will name the files with numbers starting from 0.

-t or --filetype: If you want your files to end in with a filename extension, for example .txt, give it with this tag.


file_remove.py: Removes all of the files in a given folder that include the given substring in the filename. If no directory is given, the files in the directory the scripts is in will be removed. Prompts the user by listing the files found before removing them.

Run from the command line in the folder the python file is with python file_remove.py with the following tags:

-d or --directory: The path to the folder, for example ~/test or ~/Documents/ . If left empty, will default to the folder the script is in.

-n or --name: The name of files you want to remove. Given an input, checks the folder for files that include the input as a substring in their name. If left empty, will list all of the files in the given directory.

-s or --strict: Given this tag and a non-zero number, forces the files to only include perfect matches in the results.