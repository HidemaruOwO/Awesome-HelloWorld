# -*- coding: utf-8 -*-

import sys

def main(args):
    name = args[1]
    message = 'Hello {}!'.format(name)

    print(message)

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
