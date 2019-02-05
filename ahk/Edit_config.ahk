#Include %A_ScriptDir%\lib\JSON.ahk ;包含JSON库

MsgBox, 请选择保存截图的文件夹
FileSelectFolder, raw_screenshot_path
screenshot_path := StrReplace(raw_screenshot_path, "\", "/")

passtest := true
Loop {
if (not passtest) {
MsgBox, 输入非法，请重新输入！
}
InputBox, disappear_time , 消失时间, 请输入界面存在的时间（5~15的整数，单位为秒）, , 640, 480, , , , , 10
Regtest := RegExMatch(disappear_time,"^-?\d+$")
passtest := Regtest = 1 && disappear_time> 4 && disappear_time < 16
} Until (passtest)

config_dict := {}
config_dict["steam_screenshot_dir"] := screenshot_path ;此处不需要%
config_dict["disappear_time"] := disappear_time

FileDelete, %A_ScriptDir%\config.json
FileAppend, % JSON.Dump(config_dict,,4), %A_ScriptDir%\config.json, UTF-8-RAW

