#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sublime
import sublime_plugin
import re
import os

EXEC_FLOW = 'flow'
SETTINGS_FILE = 'Flow.sublime-settings'

# Invoked via Tools > Flow 
class FlowCommand(sublime_plugin.WindowCommand):

	def run(self, files=[]):
		# Flow operates on directories and will use the path prefix
		files = files or [self.window.active_view().file_name()]

		settings = sublime.load_settings(SETTINGS_FILE)
		if os.name == "posix":
			path = "/usr/local/bin:" + os.environ['PATH']
		else:
			path = os.environ['PATH']
		self.window.run_command('exec', {
			'cmd':
				settings.get('flow_command', ['flow']) +
				settings.get('options', []) +
				files,
			'path': path,
			'file_regex': settings.get('file_regex', '(\\/.*\\.js):(\\d+):(\\d+),.*$')
		})


class FlowOnSave(sublime_plugin.EventListener):

	def on_post_save(self, view):
		settings = sublime.load_settings(SETTINGS_FILE)
		if settings.get('run_on_save', False) == False:
			return
		if re.search(settings.get('filename_filter'), view.file_name()):
			view.window().run_command(EXEC_FLOW, {
				'files': [view.file_name()]
			})

