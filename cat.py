import sys

def readfile(filename):
    f = file(filename)
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print line
    f.close()

if len(sys.argv) < 2:
    print 'No action'
    sys.exit()
if sys.argv[1].startswith('--'):
    option = sys.argv[1]
    if option == '--version':
        print 'Version 1.2'
    elif option == '--help':
        print 'use:python 1.py a.txt'
else:
    for filename in sys.argv[1:]:
        print readfile(filename)
