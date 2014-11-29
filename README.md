Sublime-Flow
==============

A Sublime package for Flow, the static JavaScript analyzer.

   * Run [Flow](http://flowtype.org) on JavaScript projects from SublimeText
   * Linux and OS X are supported. 

Prerequisites
-------------
   * [Flow](http://flowtype.org) must be installed on your system.
   * Recommended: install `flow` to `/usr/local/bin/`.

Installation
------------

TBD

Usage
-----

You must run `flow init` in your project directory before Flow can be used on it.

Flow checks entire directories. Any JavaScript files that you want checked with 
Flow must include the following line in their headers:

```
/* @flow */
```

Any of the following will work:

   * Bring up the **Command Palette** (`Command+Shift+P` on OS X, `Control+Shift+P` on Linux/Windows), then type `Flow`.
   * Click the **Tools > Flow** menu entry.
   * Press `CTRL+F`.
   * Set the Build System to Flow, then run Build (`Command+B` on OSX)

Settings
--------
* Navigate to **Preferences > Package Settings > Flow > Settings - Default**.
* To preserve custom settings:
  * copy default settings to **Preferences > Package Settings > Flow > Settings - User**
  * modify them to your requirements

