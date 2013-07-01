import sublime, sublime_plugin

REGION_NAME = 'StyleTokenListener'
MAX_STYLES = 10
cs_settings = sublime.load_settings('StyleToken.sublime-settings')

class TokenStyleCommand(sublime_plugin.TextCommand):
    def run(self, edit, style_index):
        color_selection(self.view, rollover(style_index))

class TokenStyleGoCommand(sublime_plugin.TextCommand):
    def run(self, edit, style_index=-1):
        currentRegions = get_current_regions(self.view, style_index)
        pos = self.view.sel()[0].end()
        for region in currentRegions:
            if region.begin() > pos:
                move_selection(self.view, region)
                return
        move_selection(self.view, currentRegions[0])

class TokenStyleGoBackCommand(sublime_plugin.TextCommand):
    def run(self, edit, style_index=-1):
        currentRegions = get_current_regions(self.view, style_index)
        pos = self.view.sel()[0].end()
        for region in reversed(currentRegions):
            if region.end() < pos:
                move_selection(self.view, region)
                return
        move_selection(self.view, currentRegions[-1])

class TokenStyleClearCommand(sublime_plugin.TextCommand):
    def run(self, edit, style_index=-1):
        if style_index < 0:
            for style in range(MAX_STYLES): self.view.erase_regions(REGION_NAME + str(style))
        else: self.view.erase_regions(REGION_NAME + str(rollover(style_index)))

class StyleTokenListener(sublime_plugin.EventListener):
    def on_modified(self, view):
        return
    def on_activated(self, view):
        return
    def on_load(self, view):
        return

def get_current_regions(view, style_index):
    currentRegions = []
    if style_index < 0:
        for style in range(MAX_STYLES):
            currentRegions = currentRegions + view.get_regions(REGION_NAME + str(style))
        currentRegions = sorted(currentRegions, key=lambda region: region.begin())
    else:
        currentRegions = currentRegions + view.get_regions(REGION_NAME + str(rollover(style_index)))
    return currentRegions

def color_selection(view, style_ind):
    currentSelection = view.sel()[0]
    if currentSelection.size() > 0:
        currentRegions = view.get_regions(REGION_NAME + str(style_ind))
        currentRegions.extend(view.find_all(view.substr(currentSelection), sublime.LITERAL))
        view.add_regions(REGION_NAME + str(style_ind), currentRegions, get_style(style_ind), "dot", sublime.DRAW_EMPTY)

def move_selection(view, region):
    #print 'move_selection ' + str(region.begin())
    view.sel().clear()
    view.sel().add(sublime.Region(region.begin(), region.begin()))
    view.show(region)

def rollover(style_index):
    if style_index > MAX_STYLES - 1:
                style_index = style_index - MAX_STYLES
    return style_index

def get_style(style_ind):
    return cs_settings.get('styletoken_style'+ str(style_ind+1), 'invalid')