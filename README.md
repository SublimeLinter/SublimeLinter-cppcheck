SublimeLinter-cppcheck
=========================

This linter plugin for [SublimeLinter][docs] provides an interface to [cppcheck](http://cppcheck.sourceforge.net/). It will be used with files that have the “C++” syntax.

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here][installation].

### Linter installation
Before using this plugin, you must ensure that `cppcheck` is installed on your system. To install `cppcheck`, do one of the following:

* Install `cppcheck` from your favorite package manager by typing the following in a terminal:
   ```
   <package manager> install cppcheck
   ```

* For Windows, you can download a copy from the [official site of cppcheck](http://cppcheck.sourceforge.net/).

Once `cppcheck` is installed, you must ensure it is in your system PATH so that SublimeLinter can find it. This may not be as straightforward as you think, so please read about [how linter executables are located][locating-executables] in the documentation.

### Linter configuration
In order for `cppcheck` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further, please read and follow the steps in [“Finding a linter executable”](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through “Validating your PATH” in the documentation.

Once you have installed and configured `cppcheck`, you can proceed to install the SublimeLinter-cppcheck plugin if it is not yet installed.

### Plugin installation
Please use [Package Control][pc] to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette][cmd] and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `cppcheck`. Among the entries you should see `SublimeLinter-cppcheck`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings
For general information on how SublimeLinter works with settings, please see [Settings][settings]. For information on generic linter settings, please see [Linter Settings][linter-settings].

In addition to the standard SublimeLinter settings, SublimeLinter-cppcheck provides its own settings. Those marked as “Inline Setting” or “Inline Override” may also be [used inline][inline-settings].

|Setting|Description|Inline Setting|Inline Override|
|:------|:----------|:------------:|:-------------:|
|std|Set the language standard used.|&#10003;| |
|enable|A comma-delimited list of checks to enable. Defaults to `style`.| |&#10003;|

### Examples

For ``enable``, you can use a single string (ex: ``"style,unusedFunction"``), or an array of strings if not inline (ex: ``["style", "unusedFunction"]``).

For ``std``, you can use a single string for a single value, but you have to use an array of strings for multiple values (ex. ``["c89", "c99"]``), which means you can't use multiple values in inline settings.

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.
- Please use descriptive variable names, no abbrevations unless they are very well known.

Thank you for helping out!

[docs]: http://sublimelinter.readthedocs.org
[installation]: http://sublimelinter.readthedocs.org/en/latest/installation.html
[locating-executables]: http://sublimelinter.readthedocs.org/en/latest/usage.html#how-linter-executables-are-located
[pc]: https://sublime.wbond.net/installation
[cmd]: http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html
[settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html
[linter-settings]: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
[inline-settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html#inline-settings
