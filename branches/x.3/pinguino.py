#!/usr/bin/env python
#-*- coding: utf-8 -*-

import wx
from wxgui.pinguino import getOptions, Pinguino, setGui

# ------------------------------------------------------------------------------
# MAIN
# ------------------------------------------------------------------------------

if __name__ == "__main__":
	app = wx.PySimpleApp(0)

# ------------------------------------------------------------------------------
# ---Command Line---------------------------------------------------------------
# ------------------------------------------------------------------------------

	options = getOptions()

	if options.version == True:
		print "current version is " + pinguino_version
		sys.exit(1)

	if options.author == True:
		print "jean-pierre mandon"
		print "regis blanchot"
		sys.exit(1)

	if options.board != False:
		curBoard = boardlist[options.board]

		if options.filename == False:
			print "missing filename"
			sys.exit(1)
		filename = options.filename[0]
		fname, extension = os.path.splitext(filename)
		if extension != ".pde":
			print "bad file extension, it should be .pde"
			sys.exit(1)

		pobject=Pinguino(None, -1, "")
		print "board " + curBoard.name
		print "mcu   " + curBoard.proc

		print "preprocessing ..."
		retour=pobject.preprocess(fname, curBoard)
		if retour == "error":
			print "error while preprocessing " + filename
			sys.exit(1)

		print "compiling ..."
		retour = pobject.compile(filename, curBoard)
		if retour != 0:
			print "error while compiling file " + filename
			sys.exit(1)

		print "linking ..."
		retour=pobject.link(filename, curBoard)

		if curBoard.arch == 8:
			MAIN_FILE="main.hex"
		else:
			MAIN_FILE="main32.hex"

		if os.path.exists(os.path.join(SOURCE_DIR, MAIN_FILE))!=True:
			print "error while linking "
			sys.exit(1)

		shutil.copy(os.path.join(SOURCE_DIR, MAIN_FILE), fname + ".hex")
		print "compilation done"
		print pobject.getCodeSize(fname, curBoard)
		os.remove(os.path.join(SOURCE_DIR, MAIN_FILE))
		os.remove(fname + ".c")	   
		sys.exit(0)

# ------------------------------------------------------------------------------
# ---Graphic User Interface-----------------------------------------------------
# ------------------------------------------------------------------------------

	wx.InitAllImageHandlers()
	#gui=True
	setGui(True)
	#frame_1 = Pinguino(None, -1, "")
	frame_1 = Pinguino(None)
	app.SetTopWindow(frame_1)
	frame_1.Show()
	app.MainLoop()

