Sublime-Flow
==============

   This is a beta version. Please feel free to raise issues
   or pull requests.

A Sublime package for Flow, the static JavaScript analyzer

   * It needs [Flow](http://flowtype.org) installed on your system.
   * The `flow` command must be in your `PATH`.
   * Works on Linux and MacOS only.

Prerequisites
-------------
Flow must be installed on your system globally. It's recommended to
install flow to /usr/bin/.

Installation
------------

TBD

Usage
-----
You *must* first run `flow init` in your project directory.

Flow checks entire directories. Any JavaScript files 
that you want checked with Flow should 
include the following line in their headers:

```
/* @flow */
```

Any of the following will work:

   * Bring up the **Command Palette** (`Command+Shift+P` on OS X, `Control+Shift+P` on Linux/Windows), then type `Flow`.
   * Click the **Tools > Flow** menu entry.
   * Press `CTRL+F`.
   * (After enabling flow-on-save in the settings) Just save a `.js` file.

Settings
--------
* Navigate to **Preferences > Package Settings > Flow > Settings - Default**.
* To preserve custom settings:
  * copy default settings to **Preferences > Package Settings > Flow > Settings - User**
  * modify them to your requirements

