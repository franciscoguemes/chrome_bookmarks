#!/usr/bin/env python3

import sys
from pathlib import Path
import configparser

from error import InvalidBookmarkFolderException
from jsonparser.JsonParser import JsonParser

# Default configuration files
DEFAULT_CONFIG_FILE = "chrome_bookmarks.conf"

# Dictionary Keys
CONFIG_FILE = "config_file"
BOOKMARK_FOLDER = "bookmark_folder"


def process_arguments(args):
    """
        This method expects to receive the arguments of the application in the format.
            chrome_bookmarks.py [--config=/path/to/the/config/file] BOOKMARK_FOLDER
        Note that the configuration file is optional.
    :param args: The command line arguments.
    :return: A map containing all parameters that the application needs to run.
    """

    msg = """Please provide the arguments in the following way: 
            $> chrome_bookmarks.py [--config=/path/to/the/config/file] BOOKMARK_FOLDER
            ex: 
            $> chrome_bookmarks.py --config=/home/francisco/conf/chrome_bookmarks/chrome_bookmarks.conf /Personal/MyBookmark
            """

    # A dictionary for holding the arguments once they are processed
    parameters = {
        BOOKMARK_FOLDER: "",
        CONFIG_FILE: ""
    }

    if len(args) == 2:
        parameters[BOOKMARK_FOLDER] = args[1]
        parameters[("%s" % CONFIG_FILE)] = DEFAULT_CONFIG_FILE
    elif len(args) == 3:
        args.__delitem__(0)
        for arg in args:
            #print(f"Processing arg {arg} ...")
            chunks = str.split(arg, "=")
            if len(chunks)==1:
                parameters[BOOKMARK_FOLDER] = arg
            elif len(chunks)==2:
                if str.lower(chunks[0]) == "--config":
                    parameters[CONFIG_FILE] = chunks[1]
                else:
                    sys.exit(msg)
            else:
                sys.exit(msg)
    else:
        sys.exit(msg)

    return parameters


def check_config(config):
    if 'LOCAL' not in config:
        msg = "The configuration file must have a section called [LOCAL]." + "\n "
        msg += """Please have a look at the documentation of the project and edit the config file in the pertinent way.
        More info about config files on: https://docs.python.org/3/library/configparser.html
        """
        sys.exit(msg)
    #TODO: Check the rest of the configuration parameters here...


# TODO: Handle error and corner cases...
def main():
    parameters = process_arguments(sys.argv)

    bookmark_folder = parameters[BOOKMARK_FOLDER]
    config_file = parameters["config_file"]

    # print(f"The ticket is: {ticket}")
    # print(f"The config file is: {config_file}")

    #Check if the config file exists...
    cfile = Path(config_file)
    if not cfile.is_file():
        msg = "The configuration file: " + config_file + " does not exists." \
            + "Please read the app documentation and fix the issue."
        sys.exit(msg)

    config = configparser.ConfigParser()
    config.read(config_file)
    check_config(config)

    chrome_bookmarks_file = config['LOCAL']['CHROME_BOOKMARKS_FILE']

    # print(f"The Chrome bookmarks file is: {chrome_bookmarks_file}")
    # print(f"The bookmark folder to open is: {bookmark_folder}")

    # ##########################################################################################################
    # ./chrome_bookmarks.py --config=/home/francisco/conf/chrome_bookmarks/chrome_bookmarks.conf /Personal/"Start new Spring Boot project"

    # with open(chrome_bookmarks_file) as f:
    #     data = json.load(f)


    #
    # # print(data)
    #
    # # Personal
    # print(type(data["roots"]["bookmark_bar"]["children"][20]))
    # print(data["roots"]["bookmark_bar"]["children"][20]["name"])
    # # Manitu
    # print(type(data["roots"]["bookmark_bar"]["children"][20]["children"][2]["name"]))
    # print(data["roots"]["bookmark_bar"]["children"][20]["children"][2]["name"])
    #
    # # Bookmarks in /Personal/Manitu
    # print(type(data["roots"]["bookmark_bar"]["children"][20]["children"][2]["children"]))

    parser = JsonParser(chrome_bookmarks_file)
    try:
        bookmarks = parser.get_all_bookmarks_in_folder(bookmark_folder)
        print(bookmarks)
    except InvalidBookmarkFolderException as e:
        print(e)


if __name__ == "__main__":
    main()
