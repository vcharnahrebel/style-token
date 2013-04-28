style-token
===========

StyleToken sublime plugin

Provides ability to highlight certain pieces of text with different colors (similar to notepad++ "Style token" functionality)

Adds "Style token" context menu and few commands:
 - token_style, args: styleIndex : Highlight selected text with style = styleIndex
 - token_style_clear, args: styleIndex: Clear hightlights of style = styleIndex
 - token_style_go, args: styleIndex: Go to the next highlighted text

See "Default (Windows).sublime-keymap" for example of usage. 

By default, has only windows keymap

By default, contains 3 configured styles, but supports up to 10, check "StyleToken.sublime-settings"



