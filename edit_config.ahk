#Include %A_ScriptDir%\lib\JSON.ahk ;����JSON��

MsgBox, ��ѡ��python.exe��·��
FileSelectFile, python_location, S, , python.exe, python.exe
SplitPath, python_location,, raw_python_path
python_path := StrReplace(raw_python_path, "\", "/")

MsgBox, ��ѡ�񱣴��ͼ���ļ���
FileSelectFolder, raw_screenshot_path
screenshot_path := StrReplace(raw_screenshot_path, "\", "/")

config_dict := {}
config_dict["steam_screenshot_dir"] := %screenshot_path%
config_dict["python_path"] := %python_path%

FileDelete, %A_ScriptDir%\json\config.json
config_file := FileOpen(config.json, "w")
config_file.Write(JSON.Dump(config_dict, , 4))

