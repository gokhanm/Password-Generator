#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import pygtk
pygtk.require20()
import gtk
import string
from random import choice

class PassGen(object):
	def __init__(self):
		self.win = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.win.set_title("Pass Generator")
		self.win.set_position(gtk.WIN_POS_CENTER)
		self.win.resize(250,10)
		self.win.set_border_width(10)
		self.win.connect("delete_event", gtk.main_quit)

		self.lb = gtk.Label("Random Password")
		

		self.btn = gtk.Button("Generate")
		self.btn.connect("clicked", self.generate)

		self.ent = gtk.Entry()
		self.ent.set_text("")

		self.haz = gtk.Table(1, 3)
		self.haz.set_row_spacings(10)
		self.haz.set_col_spacings(10)
		self.win.add(self.haz)

		self.haz.attach(self.lb, 0, 1, 0, 1)
		self.haz.attach(self.ent, 0, 1, 1, 2)
		self.haz.attach(self.btn, 0, 1, 2, 3)

		self.win.show_all()

	def generate(self, penar):
		size = 9
		self.pas = ''.join([choice(string.letters + string.digits) for i in range(size)])
		self.ent.set_text(str(self.pas))

	def main(self):
		gtk.main()

uyg = PassGen()
uyg.main()	
