from __future__ import annotations

from os import replace
from typing import ClassVar, Optional, Type, Any

import sublime
from .import core


class Settings:
	updated: core.Event[None] = core.Event()

	open_at_startup: bool = True
	ui_scale: int = 10
	font_face: str = 'IBM Plex Mono'

	external_terminal: str = "terminus"
	hide_status_bar: bool = False
	keep_panel_open: bool = False
	bring_window_to_front_on_pause: bool = False

	log_info: bool = False
	log_exceptions: bool = True
	log_errors: bool = True

	node: str|None = None

	# go.
	go_dlv: str|None = None

	# lldb.
	lldb_show_disassembly: str = "auto"
	lldb_display_format: str = "auto"
	lldb_dereference_pointers: bool = True
	lldb_library: str|None = None
	lldb_python: str|None = None

	breakpoints_verified: bool = False

	@staticmethod
	def on_updated():
		Settings.updated.post()

	@classmethod
	def initialize(cls):
		dot_prefix_conversions = {
			'lldb_': 'lldb.',
			'go_': 'go.',
		}
		settings = sublime.load_settings('debugger.sublime-settings')
		settings.add_on_change('debugger_settings', Settings.on_updated)

		for variable_name in vars(cls):
			if variable_name.startswith('__'): continue
			if variable_name == 'on_updated': continue
			if variable_name == 'updated': continue
			if variable_name == 'initialize': continue
			if variable_name == 'save': continue

			key = variable_name
			for start, replace in dot_prefix_conversions.items():
				if key.startswith(start):
					key = key.replace(start, replace, 1)

			class Set:
				def __init__(self, key: str):
					self.key = key

				def __get__(self, obj: Any, objtype: Any):
					return settings.get(self.key)

				def __set__(self, obj: Any, val: Any):
					settings.set(self.key, val)
					sublime.save_settings('debugger.sublime-settings')

			s = Set(key)
			setattr(cls, variable_name, s)

	@staticmethod
	def save():
		sublime.save_settings('debugger.sublime-settings')


Settings = Settings() #type: ignore
