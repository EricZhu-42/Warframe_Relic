#Include %A_ScriptDir%\lib\JSON.ahk ;包含JSON库

config_location = %A_ScriptDir%\json\config.json ;config.json的地址
FileRead, json_str, %config_location% 
config := JSON.Load(json_str) ;读取config.json文件

python_path = % config.python_path
script_path = %A_ScriptDir%/scripts
MsgBox, "%python_path%/pythonw.exe" "%script_path%/Warframe_Relic.py"
^g::
	Run "%python_path%/pythonw.exe" "%script_path%/Warframe_Relic.py"
	sleep 7000
	Runwait, taskkill /im pythonw.exe /f