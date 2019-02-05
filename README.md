# Warframe_Relic
该程序旨在快速查询Warframe游戏中打开遗物后获得的物品价值，辅助玩家进行奖励选择。
>当前版本：v2.0.0 
更新时间：2019-02-05    
基于服务器运行的版本已经基本编写完毕，预计近期进行小范围测试

## 开发环境：
1. Python版本：3.72
2. 需求的第三方库：Requests, pywin32, pillow, baidu_aip, fuzzywuzzy

## 项目结构介绍
### \scripts
&emsp;该文件夹存放所有的脚本文件。其中`scripts`中为所有可以直接运行的脚本（程序入口），`scripts\basic`中为所有模块。
### \json
&emsp;该文件夹存放所有的数据文件，其中包括:  
1. `config.json` 用户自定义的配置文件
2. `full_dic.json` 完整的中文名-WM查询名称字典
3. `relic_dic.json` 遗物奖励列表字典
4. `local_sales.json` 遗物奖励价格列表  
*注：以上`full_dic.json`与`relic_dic.json`为供参考使用的历史版本文件，不会在当前版本脚本运行时产生*
### \sampleRaw
&emsp;该文件夹存放了部分样例截图，可作为测试用例
### Others  
1. `Warframe_Relic_AHK.zip` 基于AutoHotkey编写的快速配置与运行脚本，可选择使用

## 使用方法
1. 编辑 `json\config.json` ，设置Python路径与Steam截图路径  
推荐：使用`Warframe_Relic_AHK.zip`中的`Edit_config.exe`快速配置
2. 编辑`scripts\basic\ocr.py`与`scripts\basic\search.py`，填入授权令牌  
（关于获取授权，请参照：[ocr.py部分](http://ai.baidu.com/tech/ocr/general)与[search.py部分](https://blog.richasy.cn/document/wfa/api/how_to_apply.html)）
3. 运行`Sales_create.py`，生成本地价格字典`local_sales.json`
4. 运行`scripts\Warframe_Relic.py`  
推荐：使用`Warframe_Relic_AHK.zip`中的`Warframe_Relic.exe`快速启动

## 作者列表
[Null_42](https://github.com/EricZhu-42) 与 [Xp-from-speit2018](https://github.com/Xp-from-speit2018)

## 历史版本

更新日期|版本号|更新内容
:--:|:--:|:---:
2019-01-25|v1.0.0 |项目创建  
2019-01-25|v1.1.0 |获取物品信息时进行了多线程优化  
2019-01-26|v1.2.0 |调整了文件结构  
2019-01-26|v1.3.0 |增加了GUI  
2019-01-27|v1.3.1 |提高了OCR的识别准确率  
2019-01-27|v1.4.0 |更改查询方式为本地查询  
2019-01-27|v1.4.1 |完善了GUI，增加了定时关闭与拖动功能  
2019-01-27|v1.5.0 |引入了AutoHotkey  
2019-01-27|v1.6.0 |增加了推荐选择物品功能  
2019-01-28|v1.7.0 |适应性优化，采用多进程创建价格表
2019-01-28|v1.8.0 |合并了创建本地价格表的三个脚本
2019-01-29|v1.8.1 |修复了部分OCR结果错误的情况
2019-01-31|v1.9.0 |完善了AutoHotkey脚本与部分注释
2019-02-02|v1.10.0 |物品现在采用模糊匹配，提高了准确度
2019-02-05|v2.0.0 |推出封装完毕的本地客户端，增加了部分功能

## 联系方式  
作者邮箱：  
&emsp;zhuxinhao00@gmail.com  
&emsp;hantjscnxp@outlook.com
 
## 版权信息
 1. [物品字典来源](https://github.com/Richasy/WFA_Lexicon)
 2. [OCR部分使用的API](https://ai.baidu.com)
 3. [WM价格查询API](http://wfa.richasy.cn)
 4. [JSON.ahk来源](https://github.com/cocobelgica/AutoHotkey-JSON)  
 
 感谢[Richasy](https://github.com/Richasy)对本项目开发的支持！
