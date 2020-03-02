import argparse
from os import listdir, rename
from os.path import isfile, join

def main(directory, name, filetype):
    #Gets the files in the directory, doesn't include other directories
    files = [f for f in listdir(directory) if isfile(join(directory, f))]

    if not files:
        print("Directory is empty or contains only other directories")

    else:
        i = 0
        print("Renaming the following files:\n")
        for filename in files:
            if not filename.startswith('.'):
                dst = directory + name + str(i) + filetype
                src = directory + filename
                rename(src, dst)
                print('Renamed ' + filename + ' into ' + name + str(i) + filetype)
                i += 1

if __name__ == '__main__':
    #Parser creation to get inputs from command line
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directory', required=True, default=None)
    parser.add_argument('-n', '--name', default='')
    parser.add_argument('-t', '--filetype', default='')
    args = parser.parse_args()

    try:
        main(args.directory, args.name, args.filetype)
    except:
        print("Directory " + args.directory + " is not a valid directory")