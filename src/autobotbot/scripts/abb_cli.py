import argparse

from ... autobotbot import __version__ as application_version


def main():

    # parse -v
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--version', action='version', version=application_version)

    parser.parse_args()

    # autobotbot f()altiy


if __name__ == "__main__":
    main()
