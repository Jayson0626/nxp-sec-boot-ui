# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Aug  8 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class advSettingsWin_OtpmkKey
###########################################################################

class advSettingsWin_OtpmkKey ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 619,214 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		wSizer_win = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_notebook_encryptionOpt = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel_encryptionOpt = wx.Panel( self.m_notebook_encryptionOpt, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer_encryptionOpt = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText_keySource = wx.StaticText( self.m_panel_encryptionOpt, wx.ID_ANY, u"Key Source:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_keySource.Wrap( -1 )

		gSizer_encryptionOpt.Add( self.m_staticText_keySource, 0, wx.ALL, 5 )

		m_choice_keySourceChoices = [ u"Fuse OTPMK[255:128]" ]
		self.m_choice_keySource = wx.Choice( self.m_panel_encryptionOpt, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,-1 ), m_choice_keySourceChoices, 0 )
		self.m_choice_keySource.SetSelection( 0 )
		gSizer_encryptionOpt.Add( self.m_choice_keySource, 0, wx.ALL, 5 )

		self.m_staticText_aesMode = wx.StaticText( self.m_panel_encryptionOpt, wx.ID_ANY, u"AES Mode:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_aesMode.Wrap( -1 )

		gSizer_encryptionOpt.Add( self.m_staticText_aesMode, 0, wx.ALL, 5 )

		m_choice_aesModeChoices = [ u"ECB", u"CTR" ]
		self.m_choice_aesMode = wx.Choice( self.m_panel_encryptionOpt, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,-1 ), m_choice_aesModeChoices, 0 )
		self.m_choice_aesMode.SetSelection( 1 )
		gSizer_encryptionOpt.Add( self.m_choice_aesMode, 0, wx.ALL, 5 )

		self.m_staticText_encryptedRegionCnt = wx.StaticText( self.m_panel_encryptionOpt, wx.ID_ANY, u"Encrypted Region Count:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_encryptedRegionCnt.Wrap( -1 )

		gSizer_encryptionOpt.Add( self.m_staticText_encryptedRegionCnt, 0, wx.ALL, 5 )

		m_choice_encryptedRegionCntChoices = [ u"0 - Whole Image", u"1 - User Defined", u"2 - User Defined" ]
		self.m_choice_encryptedRegionCnt = wx.Choice( self.m_panel_encryptionOpt, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,-1 ), m_choice_encryptedRegionCntChoices, 0 )
		self.m_choice_encryptedRegionCnt.SetSelection( 0 )
		gSizer_encryptionOpt.Add( self.m_choice_encryptedRegionCnt, 0, wx.ALL, 5 )


		self.m_panel_encryptionOpt.SetSizer( gSizer_encryptionOpt )
		self.m_panel_encryptionOpt.Layout()
		gSizer_encryptionOpt.Fit( self.m_panel_encryptionOpt )
		self.m_notebook_encryptionOpt.AddPage( self.m_panel_encryptionOpt, u"Encryption Option", False )

		wSizer_win.Add( self.m_notebook_encryptionOpt, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_notebook_encryptedRegionInfo = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel_encryptedRegionInfo = wx.Panel( self.m_notebook_encryptedRegionInfo, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer_encryptedRegionInfo = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText_regionStart = wx.StaticText( self.m_panel_encryptedRegionInfo, wx.ID_ANY, u"Region Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_regionStart.Wrap( -1 )

		gSizer_encryptedRegionInfo.Add( self.m_staticText_regionStart, 0, wx.ALL, 5 )

		self.m_staticText_regionLength = wx.StaticText( self.m_panel_encryptedRegionInfo, wx.ID_ANY, u"Region Length", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_regionLength.Wrap( -1 )

		gSizer_encryptedRegionInfo.Add( self.m_staticText_regionLength, 0, wx.ALL, 5 )

		self.m_textCtrl_region0Start = wx.TextCtrl( self.m_panel_encryptedRegionInfo, wx.ID_ANY, u"0x60001000", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer_encryptedRegionInfo.Add( self.m_textCtrl_region0Start, 0, wx.ALL, 5 )

		self.m_textCtrl_region0Length = wx.TextCtrl( self.m_panel_encryptedRegionInfo, wx.ID_ANY, u"0x1000", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer_encryptedRegionInfo.Add( self.m_textCtrl_region0Length, 0, wx.ALL, 5 )

		self.m_textCtrl_region1Start = wx.TextCtrl( self.m_panel_encryptedRegionInfo, wx.ID_ANY, u"0x60002000", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer_encryptedRegionInfo.Add( self.m_textCtrl_region1Start, 0, wx.ALL, 5 )

		self.m_textCtrl_region1Length = wx.TextCtrl( self.m_panel_encryptedRegionInfo, wx.ID_ANY, u"0xe000", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer_encryptedRegionInfo.Add( self.m_textCtrl_region1Length, 0, wx.ALL, 5 )


		self.m_panel_encryptedRegionInfo.SetSizer( gSizer_encryptedRegionInfo )
		self.m_panel_encryptedRegionInfo.Layout()
		gSizer_encryptedRegionInfo.Fit( self.m_panel_encryptedRegionInfo )
		self.m_notebook_encryptedRegionInfo.AddPage( self.m_panel_encryptedRegionInfo, u"Encrypted Region Info", False )

		wSizer_win.Add( self.m_notebook_encryptedRegionInfo, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText_winNull0 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 348,-1 ), 0 )
		self.m_staticText_winNull0.Wrap( -1 )

		wSizer_win.Add( self.m_staticText_winNull0, 0, wx.ALL, 5 )

		self.m_button_ok = wx.Button( self, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		wSizer_win.Add( self.m_button_ok, 0, wx.ALL, 5 )

		self.m_button_cancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		wSizer_win.Add( self.m_button_cancel, 0, wx.ALL, 5 )


		self.SetSizer( wSizer_win )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_choice_encryptedRegionCnt.Bind( wx.EVT_CHOICE, self.callbackChangeRegionCount )
		self.m_button_ok.Bind( wx.EVT_BUTTON, self.callbackOk )
		self.m_button_cancel.Bind( wx.EVT_BUTTON, self.callbackCancel )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def callbackChangeRegionCount( self, event ):
		event.Skip()

	def callbackOk( self, event ):
		event.Skip()

	def callbackCancel( self, event ):
		event.Skip()


