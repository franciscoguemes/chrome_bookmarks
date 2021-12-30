#!/usr/bin/env python3

import json

from error.InvalidBookmarkFolderException import InvalidBookmarkFolderException


class JsonParser:
    """ A JSON parser for the Chromium bookmarks in Linux.
    """

    PATH_SEPARATOR = "/"
    ROOTS = "roots"
    BOOKMARK_BAR = "bookmark_bar"
    OTHER = "other"

    def __init__(self, chrome_bookmarks_file):
        self.__chrome_bookmarks_file = chrome_bookmarks_file

    def __is_a_folder(self, element):
        answer = False
        if "type" in element:
            if element["type"].casefold() == "folder".casefold():
                answer = True
        return answer

    def get_all_bookmarks_in_folder(self, bookmark_folder):
        paths = bookmark_folder.split(self.PATH_SEPARATOR)

        # In case of having the first character of the string as the PATH_SEPARATOR, the first path is empty
        if not paths[0]:
            del paths[0]

        print(f"paths: {paths}")

        with open(self.__chrome_bookmarks_file) as f:
            data = json.load(f)

        parent_folder = None
        if paths[0] == self.OTHER:
            parent_folder = data[self.ROOTS][self.OTHER]
            del paths[0]
        elif paths[0] == self.BOOKMARK_BAR:
            parent_folder = data[self.ROOTS][self.BOOKMARK_BAR]
            del paths[0]
        else:
            raise InvalidBookmarkFolderException(
                "The given bookmark_folder {} must start with 'other' or 'bookmark_bar' as parent folder".format(bookmark_folder))

        found = False
        for p in paths:
            #print(f"Analising string: {p}")
            found = False
            children = parent_folder["children"]
            for son in children:
                #print(f"The son is: {son['name']}")
                if son["name"] == p and self.__is_a_folder(son):
                    parent_folder = son
                    found = True
                    break
            if not found:
                parent_folder = None
                break

        if not found:
            raise InvalidBookmarkFolderException("The given bookmark_folder {} does not exists in the file {}".format(bookmark_folder, self.__chrome_bookmarks_file))

        bookmarks = parent_folder["children"]
        return self.__getUrls(bookmarks)

    def __getUrls(self, bookmarks):
        urls = [None] * len(bookmarks)

        index = 0
        for bookmark in bookmarks:
            urls[index] = bookmark["url"]
            index += 1

        return urls
