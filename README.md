Sublime-Flow
==============

A Sublime package for Flow, the static JavaScript analyzer.

   * Run [Flow](http://flowtype.org) on JavaScript projects from SublimeText
   * Linux and OS X are supported. 

Prerequisites
-------------

  * [Flow](http://flowtype.org) must be installed on your system.  It's recommended to install `flow` to `/usr/local/bin/`.
  * To allow Flow to work in your project directory you must either
    - run `flow init` in your project directory
    - or create an empty `.flowconfig` file in your project's root directory

Installation
------------

### Using Package Control:
   * Install the [Package Control](https://sublime.wbond.net/installation) plugin if you don't have it
   * Press Ctrl+Shift+P to bring up the Command Palette (or use Tools > Command Palette menu)
   * Select Package Control: Install Package
   * Type 'Flow' to find Flow for Sublime Text 2 and 3
   * Select 'Flow for Sublime Text 2 and 3' to install


### Not using Package Control:
   * Get files from the [package archive](https://github.com/darrenderidder/Sublime-Flow/archive/master.zip)
   * unzip to your Packages/Flow directory, for example:
      * Linux: ~/.config/sublime-text-2/Packages/JSLint
      * Mac: ~/Library/Application Support/Sublime Text 2/Packages/JSLint
      * Windows: %APPDATA%/Sublime Text 2/Packages/JSLint
   * Relaunch Sublime Text

Usage
-----

You must run `flow init` in your project directory before Flow can be used on it.

Flow checks entire directories.  Any JavaScript files that you want checked with 
Flow must include the following line in their headers:

```
/* @flow */
```

Sublime-Flow includes both a command plug-in and a build system.

There are several ways to run the Flow command:

* Bring up the **Command Palette** (`Command+Shift+P` on OS X, `Control+Shift+P` on Linux/Windows), then type `Flow`.
* Click the **Tools > Flow** menu entry.
* Press `CTRL+F`.

Using the Flow build system:
* Set the Build System to Flow, then run Build (`Command+B` on OSX)
* Alternately, set the Build System to automatic; the Flow build system will be selected for `.js` files automatically. If another build system has already been configured to work with `.js` files, this may not work.

Settings
--------
* Navigate to **Preferences > Package Settings > Flow > Settings - Default**.
* To preserve custom settings:
  * copy default settings to **Preferences > Package Settings > Flow > Settings - User**
  * modify them to your requirements

