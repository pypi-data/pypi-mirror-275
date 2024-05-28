import os
import sys

def main():
    binary_path = os.path.join(os.path.dirname(__file__), 'bin', 'rlc-lsp')
    os.execv(binary_path, [binary_path] + sys.argv[1:])

if __name__ == '__main__':
    main()

