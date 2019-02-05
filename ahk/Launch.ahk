#Include %A_ScriptDir%\lib\JSON.ahk ;包含JSON库

;config_location = %A_ScriptDir%\config.json ;config.json的地址
;FileRead, json_str, %config_location% 
;config := JSON.Load(json_str) ;读取config.json文件


^g::
	Send, {F12}
	Run "%A_ScriptDir%\client.exe"