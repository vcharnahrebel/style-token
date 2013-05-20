StyleToken sublime plugin
===========

A sublime plugin that allows to highlight certain pieces of text with different colors (similar to notepad++ "Style token" functionality)

Usage
------------

Plugin adds "Style token" context menu and few commands:
 - token_style, args: styleIndex : Highlight selected text with style = styleIndex.
 - token_style_clear, args: styleIndex: Clear hightlights of style = styleIndex. If no arg provided, clears all styles.
 - token_style_go, args: styleIndex: Go to the next highlighted text. If styleIndex arg provided, go to the specific style. If no arg provided, go to the any next style.

See "Default (Windows).sublime-keymap" for example of command usage. 

By default, has only windows keymap

By default, contains 3 configured styles, but supports up to 10, check "StyleToken.sublime-settings"

Screenshots:

![Context menu ](https://raw.github.com/vcharnahrebel/Main/master/img/sublime-styletoken-ScreenClip1.png)

![Style 1 hightlight ](https://raw.github.com/vcharnahrebel/Main/master/img/sublime-styletoken-ScreenClip2.png)

![Context menu ](https://raw.github.com/vcharnahrebel/Main/master/img/sublime-styletoken-ScreenClip3.png)

![Style 2 hightlight ](https://raw.github.com/vcharnahrebel/Main/master/img/sublime-styletoken-ScreenClip4.png)



