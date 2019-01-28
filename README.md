# Warframe_Relic
该程序旨在快速查询Warframe游戏中打开遗物后获得的物品价值，辅助玩家进行奖励选择
>当前版本：v1.7.0  
更新时间：2019-01-28  
尚未更新完毕，请继续等待

## 开发环境：
1. Python版本：3.72
2. 需求的第三方库：Requests, pywin32, pillow, baidu_aip

## 项目结构介绍
- **scripts** 
该文件夹存放所有的脚本文件。其中`scripts`中为所有可以直接运行的脚本（程序入口），`scripts\basic`中为所有模块。
- **json**  
该文件夹存放所有的数据文件，其中包括:  
1. `config.json` 用户自定义的配置文件
2. `full_dic.json` 完整的中文名-WM查询名称字典，通过`Fulldic_create.py`生成
3. `relic_dic.json` 遗物奖励列表字典，通过`Relic_filter.py`生成
4. `local_sales.json` 遗物奖励价格列表，通过`Sales_create.py`生成  
- **sampleRaw**  
该文件夹存放了部分样例截图，可作为测试用例
- **根目录下其他文件**  
1. `Warframe_Relic_AHK.zip` 基于AutoHotkey编写的快速配置与运行脚本，可选择使用

## 使用方法
1. 编辑 `json\config.json` ，设置Python路径与Steam截图路径  
~~推荐：使用`Warframe_Relic_AHK.zip`中的`Edit_config.exe`快速配置~~（未完成）
2. 编辑`scripts\basic\ocr.py`与`scripts\basic\search.py`，填入授权令牌  
（关于获取授权，请参照：[ocr.py](http://ai.baidu.com/tech/ocr/general)与[search.py](https://blog.richasy.cn/document/wfa/api/how_to_apply.html)）
3. 依次运行`Fulldic_create.py`，`Relic_filter.py`与`Sales_create.py`，生成本地价格字典`local_sales.json`
4. 运行`scripts\Warframe_Relic.py`  
~~推荐：使用`Warframe_Relic_AHK.zip`中的`Warframe_Relic.exe`快速启动~~（未完成）

## 作者列表
[Null_42](https://github.com/EricZhu-42) 与 [Xp-from-speit2018](https://github.com/Xp-from-speit2018)

## 历史版本
v1.0.0 项目创建  
v1.1.0 获取物品信息时进行了多线程优化  
v1.2.0 调整了文件结构  
v1.3.0 增加了GUI  
v1.3.1 提高了GUI的识别准确率  
v1.4.0 更改查询方式为本地查询  
v1.4.1 完善了GUI，增加了定时关闭与拖动功能  
v1.5.0 引入了AutoHotkey  
v1.6.0 增加了推荐选择物品功能  
v1.7.0 适应性优化，创建价格表时采用多进程，提高了效率

## 联系方式
邮箱：zhuxinhao00@gmail.com; hantjscnxp@outlook.com
 
## 版权信息
 1. [物品字典来源](https://github.com/Richasy/WFA_Lexicon)
 2. [OCR使用的API](https://ai.baidu.com)
 3. [WM物品价格来源](http://wfa.richasy.cn)
 4. [JSON.ahk](https://github.com/cocobelgica/AutoHotkey-JSON)  
 
 感谢[Richasy](https://github.com/Richasy)对本项目开发的支持！
