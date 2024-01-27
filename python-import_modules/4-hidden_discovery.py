#!/usr/bin/python3
import sys

# Add the path to the module if it is not in the default Python path
sys.path.append('/path/to/hidden_4')

if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if name[:2] != "__":
            print(name)
