import sublime, sublime_plugin

REGION_NAME = 'StyleTokenListener'
MAX_STYLES = 10

cs_settings = sublime.load_settings('StyleToken.sublime-settings')
styles = [cs_settings.get('styletoken_style'+ str(i+1), 'invalid') for i in range(MAX_STYLES)]


class TokenStyleCommand(sublime_plugin.TextCommand):
	def run(self, edit, style_index):
		color_selection(self.view, styles[rollover(style_index)])

class TokenStyleGoCommand(sublime_plugin.TextCommand):
	def run(self, edit, style_index=-1):
		currentRegions = []
		if style_index < 0:
			for style in styles:
				currentRegions = currentRegions + self.view.get_regions(REGION_NAME + style)
			currentRegions = sorted(currentRegions, key=lambda region: region.begin())
		else:
			currentRegions = currentRegions + self.view.get_regions(REGION_NAME + styles[rollover(style_index)])
		pos = self.view.sel()[0].end()
		#print 'current sel' + str(self.view.sel()[0])
		#print 'current pos ' + str(pos)
		for region in currentRegions:
			if region.begin() > pos:
				move_selection(self.view, region)
				return
		move_selection(self.view, currentRegions[0])

class TokenStyleClearCommand(sublime_plugin.TextCommand):
	def run(self, edit, style_index=-1):
		if style_index < 0:
			for style in styles: self.view.erase_regions(REGION_NAME + style)
		else: self.view.erase_regions(REGION_NAME + styles[rollover(style_index)])

class StyleTokenListener(sublime_plugin.EventListener):
    def on_modified(self, view):
        return
    def on_activated(self, view):
		return
    def on_load(self, view):
        return

def color_selection(view, color):
	currentSelection = view.sel()[0]
	#print view.substr(view.sel()[0])
	if currentSelection.size() > 0:
		currentRegions = view.get_regions(REGION_NAME + color)
		currentRegions.extend(view.find_all(view.substr(currentSelection), sublime.LITERAL))
		view.add_regions(REGION_NAME + color, currentRegions, color, sublime.DRAW_EMPTY)

def move_selection(view, region):
	#print 'move_selection ' + str(region.begin())
	view.sel().clear()
	view.sel().add(sublime.Region(region.begin(), region.begin()))
	view.show(region)

def rollover(style_index):
	if style_index > len(styles) - 1:
				style_index = style_index - len(styles)
	return style_index