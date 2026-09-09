#!/usr/bin/env python3

from myman import myman

def main():
    print(myman.myman(ind=1))

    print(myman.myman(target="Bessent"))

    print(myman.myman(ind="maitre"))

if __name__ == "__main__":
    main()
