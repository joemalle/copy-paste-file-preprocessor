# Copy-Paste File Preprocessor

I wanted to test my JavaScript/CSS/HTML without a full server-side language, so I made this simple preprocessor that sweeps through all .html files in its directory looking for places to replace text.  This makes it easy to have one .html file for headers/footers/etc.

## How to use

1. Download preprocessor.py on a computer that has Python installed.  Put the file in the root directory for the copy-paste action.
2. Create a directory called "include" which will contain files to be copied.
3. In any .html file, write "include header.html" on its own line.  This line will be replaced with the contents of header.html.

This is designed to work a lot like PHP's include function.
