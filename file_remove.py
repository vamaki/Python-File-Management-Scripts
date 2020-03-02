import argparse
import os
from os.path import isfile, join

def remove(directory, filename, strict):
    #Gets the files in the directory, doesn't include other directories
    files = [f for f in os.listdir(directory) if (isfile(join(directory, f)) and filename in f)]

    if not files:
        print("Didn't find any matching files in the directory")

    else:
        if not strict:
            print('Found the following files matching the given condition:\n')
            for file in files:
                print(file)
            print('')
            while True:
                try:
                    num = input('To remove the files input a non-zero number, to cancel input 0: ')
                    break
                except:
                    print("Invalid input, please input a number.")

            if num:
                if not directory.endswith('/'):
                    directory = directory + '/'
                for file in files:
                    os.remove(directory + file)
                    print('Removed ' + file)
            else:
                print('Files not removed')
        
        else:
            filteredFiles = [f for f in files if filename == f]
            if not filteredFiles:
                print("Didn't find any matching files in the directory")
            else:
                print('Found the following files matching the given condition:\n')
                for file in filteredFiles:
                    print(file)
                print('')
                while True:
                    try:
                        num = input('To remove the files input a non-zero number, to cancel input 0: ')
                        break
                    except:
                        print("Invalid input, please input a number.")

                if num:
                    if not directory.endswith('/'):
                        directory = directory + '/'
                    for file in files:
                        os.remove(directory + file)
                        print('Removed ' + file)
                else:
                    print('Files not removed')

if __name__ == '__main__':
    #Parser creation to get inputs from command line
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directory', required=False, default=os.getcwd())
    parser.add_argument('-n', '--name', default='')
    parser.add_argument('-s', '--strict', default=0)
    args = parser.parse_args()

    remove(args.directory, args.name, args.strict)