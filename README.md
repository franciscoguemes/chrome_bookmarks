# chrome_bookmarks

## Introduction
The following application parses your Chrome/Chromium bookmarks list and return the URLs
contained in the folder supplied as parameter. I.e. If you have saved in your bookmarks
a folder named "Art" which contains 10 URLs, the application will return a list that
contains the 10 URLs.

## Usage
The application expects the following parameters:
1. The configuration file (Optional). See more information in the "Configuration" section.
2. The folder (folder path) that contains the links that we want to return by the application.
   If a folder name in the folder path contain spaces or any other special character not handled
   by the command line, you should specify the folder name between double or simple quotes.
   For the folder path it is assumed that the bookmarks bar represent the root directory ("/").
   The root directory can be optionally omitted from the folder path.

### Examples of usage:

The following examples provide a configuration file.

```
./chrome_bookmarks.py --config=/home/francisco/conf/chrome_bookmarks/chrome_bookmarks.conf /Personal/"Start new Spring Boot project"
```

```
./chrome_bookmarks.py --config=/home/francisco/conf/chrome_bookmarks/chrome_bookmarks.conf Personal/"Start new Spring Boot project"
```

**Note**: The path of the bookmarks folder is equivalent in both examples.  


## Configuration
The configuration file must have a section called "LOCAL" that contains the property key-value pair
"CHROME_BOOKMARKS_FILE" and as a value the path to your Chrome bookmarks file. I.e.

```
# ----------------------------------------------------------------------
#                   LOCAL CONFIGURATION
# ----------------------------------------------------------------------
[LOCAL]
CHROME_BOOKMARKS_FILE = /home/francisco/snap/chromium/current/.config/chromium/Default/Bookmarks 
```

## Additional sources:
Here you can find additional information about the bookmarks file.

[Bookmarks file location](https://itstillworks.com/folder-google-chrome-bookmarks-stored-4682.html)

[Bookmarks file structure](https://askubuntu.com/questions/624120/is-it-possible-to-view-google-chrome-bookmarks-and-history-from-the-terminal)