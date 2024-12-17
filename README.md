<<<<<<< HEAD
# TraceRecoder
多轨迹个性化显示的web应用
=======
# mapRecorder
GPX运动轨迹程序，效果图如下：

![效果图](https://pic.imgdb.cn/item/67619b2fd0e0a243d4e58bbd.png)


## 环境配置
1. 安装python，确保有python运行环境

2. 安装python flask
`pip install flask`
3. 根据指令运行
* export FLASK_APP=app.py
* export FLASK_ENV=development
* python -m flask run --debug
4. 安装缺失的函数库 pip install 包名，最终执行成功

## 使用方式
1. gpx轨迹导出：
- 网页版登录行者，手动导出
- 如果记录过多，可参考[github项目](https://github.com/DaThabe/XingzheExport)，运行程序批量下载
- 除了行者轨迹，也可根据自身情况导出户外轨迹

2. 将导出的数据移动到项目文件夹下的`./static`

3. 执行程序，打开网页url：`localhost:5000`

4. 直接点击`SELECT`，表示选择全部轨迹

5. 等待执行完毕，生成`result.html`文件，点击查看

## 效果展示：

![效果图](https://pic.imgdb.cn/item/67619b2fd0e0a243d4e58bbd.png)

## 项目说明
1. 本项目出于个人兴趣，不可用于商业盈利；
2. 主要参考项目: [tz_flask_20230311_route](https://github.com/tztechno/tz_flask_20230311_route)，一个单轨迹网页地图展示的项目，在其基础上优化了地图显示效果，并设置多轨迹热度展示。
3. 其他参考项目：
    - [XingzheExport](https://github.com/DaThabe/XingzheExport)：行者网页端gpx文件批量下载
>>>>>>> b90d9f9 (多轨迹合并展示效果-初版)
