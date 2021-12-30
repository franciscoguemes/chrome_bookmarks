# chrome_bookmarks

## Introduction
The following application parses your Chrome/Chromium bookmarks list and return the URLs
contained in the folder supplied as parameter. I.e. If you have saved in your bookmarks
a folder named "Art" which contains 10 URLs, the application will return a list that
contains the 10 URLs.

## Usage
The application expects the following parameters:
1. The configuration file (Optional). See more information in the "Configuration" section.
2. The folder (folder path) inside the bookmarks structure that contains the links that we want to be 
   returned by the application. For the folder path it is assumed that the bookmarks itself represent the 
   root directory ("/"). Under the root directory there are two directories "__bookmark_bar__" for the bookmarks
   bar and "__other__" for the bookmarks that are not visible in the bookmarks bar. 
   The root directory can be optionally omitted from the folder path, but still you will have to specify if 
   the bookmarks that you want are in the bookmarks bar or in the non-visible bookmarks.
   If a folder name in the folder path contain spaces or any other special character not handled
   by the command line, you should specify the folder name between double or simple quotes.
   

### Examples of usage:

The following examples provide a configuration file.

```
./chrome_bookmarks.py --config=/home/francisco/conf/chrome_bookmarks/chrome_bookmarks.conf /bookmark_bar/Personal/"Start new Spring Boot project"
```

```
./chrome_bookmarks.py --config=/home/francisco/conf/chrome_bookmarks/chrome_bookmarks.conf bookmark_bar/Personal/"Start new Spring Boot project"
```

**Note**: The path of the bookmarks folder is equivalent in both examples. The folder Personal is supposed to be in the bookmarks bar. Note that the
folder is in double quotes because it contains characters (spaces) that are not handled correctly by the command line.

```
./chrome_bookmarks.py --config=/home/francisco/conf/chrome_bookmarks/chrome_bookmarks.conf /other/Programming/Python
```

```
./chrome_bookmarks.py --config=/home/francisco/conf/chrome_bookmarks/chrome_bookmarks.conf other/Programming/Python
```


## Configuration
The configuration file must have a section called "LOCAL" that contains the property key-value pair
"CHROME_BOOKMARKS_FILE" and as a value the path to your Chrome bookmarks file. I.e.

```
# ----------------------------------------------------------------------
#                   LOCAL CONFIGURATION
# ----------------------------------------------------------------------
[LOCAL]
# This is a possible location for your Bookmarks file..
CHROME_BOOKMARKS_FILE = /home/francisco/snap/chromium/current/.config/chromium/Default/Bookmarks
# If not try with this ohter one ...
# CHROME_BOOKMARKS_FILE = /home/francisco/snap/chromium/common/chromium/Default/Bookmarks
```

## Additional sources:
Here you can find additional information about the bookmarks file.

[Bookmarks file location](https://itstillworks.com/folder-google-chrome-bookmarks-stored-4682.html)

[Bookmarks file structure](https://askubuntu.com/questions/624120/is-it-possible-to-view-google-chrome-bookmarks-and-history-from-the-terminal)