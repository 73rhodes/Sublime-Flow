#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sublime
import sublime_plugin
import re
import os

EXEC_FLOW = 'flow_exec'
SETTINGS_FILE = 'Flow.sublime-settings'

class FlowExecCommand(sublime_plugin.WindowCommand):

	def run(self, files=[]):
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
			'line_regex': settings.get('line_regex', '.*// Line ([0-9]*), Pos ([0-9]*)$'),
			'file_regex': settings.get('file_regex', '(^[^# ]+.*$)')
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


# Invoked via Tools > Flow 

class FlowCommand(sublime_plugin.WindowCommand):

	def run(self):
		self.window.run_command(EXEC_FLOW, {
			'files': [self.window.active_view().file_name()]
		})
