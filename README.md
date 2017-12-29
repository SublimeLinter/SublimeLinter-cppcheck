SublimeLinter-cppcheck
=========================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-cppcheck.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-cppcheck)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [cppcheck](http://cppcheck.sourceforge.net/). It will be used with files that have the “C++” or “C” syntax.

## Installation
SublimeLinter must be installed in order to use this plugin. 

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before using this plugin, you must ensure that `cppcheck` is installed on your system. To install `cppcheck`, do one of the following:

* Install `cppcheck` from your favorite package manager:
   ```
   <package manager> install cppcheck
   ```

* For Windows, you can download a copy from the [official site of cppcheck](http://cppcheck.sourceforge.net/).

Once `cppcheck` is installed, you must ensure it is in your system PATH so that SublimeLinter can find it. The docs cover [troubleshooting PATH configuration](http://sublimelinter.readthedocs.io/en/latest/troubleshooting.html#finding-a-linter-executable).


## Settings
- SublimeLinter settings: http://sublimelinter.readthedocs.org/en/latest/settings.html
- Linter settings: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html

Additional SublimeLinter-cppcheck settings:

|Setting|Description|
|:------|:----------|
|std|Set the language standard used.|
|enable|A comma-delimited list of checks to enable. Defaults to `style`.|


### Examples

For ``enable``, you can use a single string (ex: ``"style,unusedFunction"``), or an array of strings if not inline (ex: ``["style", "unusedFunction"]``).

For ``std``, you can use a single string for a single value, but you have to use an array of strings for multiple values (ex. ``["c89", "c99"]``), which means you can't use multiple values in inline settings.

