# pyai
### 打造一个在线的人脸识别系统
## 在线体验 http://pyai.lookcos.cn/

### 使用方法
0.完整的克隆本项目，
1.下载百度SDK，解压至项目根目录保证setup.py和项目的cb.py在同一目录，
2.执行 python setup.py install 以安装百度SDK
3.安装flask  #### pip install flask
4.执行 python cb.py 即可

## 目录结构：

│  baidu_aip.py 调用百度人脸识别

│  cb.py Flask 主页，引导页！

├─static  静态文件存放

│ ------     favicon.ico 

│ ------      filedrag.js 

│ ------     jquery.min.js

│ ------      style.css 

└─templates 模板文件

| ------ ------   index.html  主页模板

|------ ------     res.html  结果页模板

|------ ------     tz.html   跳转页面模板

#### 百度人脸识别SDK下载  http://ai.baidu.com/sdk#bfr  
#### 下载后执行 python setup.py install 即可。 
### 保证cb.py与SDK在同一目录下。

## 相关参考文献即代码托管等：
#### Python SDK文档  http://ai.baidu.com/docs#/Face-Python-SDK/top

#### Flask中文文档  http://dormousehole.readthedocs.io/en/latest/ 

#### 项目地址：https://github.com/LookCos/pyai 

![avatar](https://raw.githubusercontent.com/LookCos/pyai/master/%E6%95%88%E6%9E%9C%E5%9B%BE/1.png)
![avatar](https://raw.githubusercontent.com/LookCos/pyai/master/%E6%95%88%E6%9E%9C%E5%9B%BE/2.png)
![avatar](https://raw.githubusercontent.com/LookCos/pyai/master/%E6%95%88%E6%9E%9C%E5%9B%BE/2.png)
![avatar](https://raw.githubusercontent.com/LookCos/pyai/master/%E6%95%88%E6%9E%9C%E5%9B%BE/3.png)
![avatar](https://raw.githubusercontent.com/LookCos/pyai/master/%E6%95%88%E6%9E%9C%E5%9B%BE/4.png)
![avatar](https://raw.githubusercontent.com/LookCos/pyai/master/%E6%95%88%E6%9E%9C%E5%9B%BE/5.png)
![avatar](https://raw.githubusercontent.com/LookCos/pyai/master/%E6%95%88%E6%9E%9C%E5%9B%BE/6.png)
![avatar](https://raw.githubusercontent.com/LookCos/pyai/master/%E6%95%88%E6%9E%9C%E5%9B%BE/7.png)
