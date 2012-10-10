import sublime, sublime_plugin
import os
from subprocess import call
class OpenShortcutsCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    call(["open", "http://www.google.com"])