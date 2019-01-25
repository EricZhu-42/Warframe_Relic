import win32con

import win32clipboard

def settext(sentence):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT,sentence)
    win32clipboard.CloseClipboard()