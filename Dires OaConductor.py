import re #正则表达式
import os #操作系统模块
import urllib #进行SQLite数据库操作
from urllib import parse
from urllib import request


'''

Python版本 3.9.6 64-bit
最后编写时间 2021-10-30
作者 icloudsheep
平台 Visual Studio Code
工作室 Dires Studio

注 该源文件改编于 Dires NaConductor

'''

isOutputResultKeys = "" #默认为 T
isOutputResultKeysNum = "" #默认为 T
url = "" #默认值 http://114.55.147.180/contest.php
resultKeys = [] #收集通过了两轮匹配的所有结果

findFirstResults = re.compile(r'<a href=\'contest.php\?cid=\d\d\d\d\'>(.*?)</a></td><td>') #正则表达式 用于一次提取
findSecondResults = re.compile(r'.*?计算机21-4/5/6.*?') #二次提取

#注：计算机21-4/5/6 为特定值，仅针对特定班级

def iosafety(): #保障软件基本运行文件存在 如果不存在则创建并赋予默认值
    if os.path.exists("pyConfig.txt"):
        print()
    else:
        fileRepair_pyConfig = open("pyConfig.txt","w",encoding="utf-8")
        fileRepair_pyConfig.write(fileRepair_pyConfig_FileContext)
        fileRepair_pyConfig.close


def main():

    iosafety() #执行IO保护
    
    pyConfigReader = open("pyConfig.txt","r",encoding="utf-8") #读取pyConfig.txt来为软件进行基本配置
    outputInfo("文件打开: pyConfig.txt")
    config = [line.strip("\n") for line in pyConfigReader.readlines()]
    url = config[1]
    #isOutputResultKeys = config[7]
    #isOutputResultKeysNum = config[9]

    outputInfo("配置导入完成")
    pyConfigReader.close
    outputInfo("文件关闭: pyConfig.txt")

    getData(url) #开始网页操作
    outputInfo("方法调用: getData(url)")


def getData(baseurl):

    pyConfigReader = open("pyConfig.txt","r",encoding="utf-8") #读取pyConfig.txt来为软件进行基本配置
    outputInfo("文件打开: pyConfig.txt")
    config = [line.strip("\n") for line in pyConfigReader.readlines()]
    #url = config[1]
    isOutputResultKeys = config[7]
    isOutputResultKeysNum = config[9]

    rawHtml = askurl(baseurl) #网页初始源代码
    #print(rawHtml)
    outputInfo("代码获取完成")

    firstResultsKeys = re.findall(findFirstResults,rawHtml) 
    for firstResultsKey in firstResultsKeys:
        if re.match(findSecondResults,firstResultsKey):
            print(firstResultsKey)
            resultKeys.append(firstResultsKey)
    outputInfo("完成两轮匹配")

    if isOutputResultKeys == "T": #是否输出结果为文件
        resultKeysWriter = open("resultKeys.txt","w",encoding="utf-8")
        outputInfo("文件打开: resultKeys.txt")
        for resultKey in resultKeys:
            resultKeysWriter.write(resultKey + "\n")
            resultKeysWriter.close
        outputInfo("文件关闭: resultKeys.txt")
    
    if isOutputResultKeysNum == "T": #是否输出结果数量为文件
        resultKeysNumWriter = open("resultKeysNum.txt","w",encoding="utf-8")
        outputInfo("文件打开: resultKeysNum.txt")
        resultKeysNumWriter.write((str)(resultKeys.__len__()))
        outputInfo("文件关闭: resultKeysNum.txt")

def outputInfo(info): #打印 输出信息
    outputInfoWriter = open("outputInfo.txt","a")
    outputInfoWriter.write(info + "\n\n")
    outputInfoWriter.close


def askurl(url): 
    head = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73"}
    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except Exception as error:
        print(error)
    return html


fileRepair_pyConfig_FileContext = "url:\nhttp://114.55.147.180/contest.php\n第一次筛选正则表达式 ( 无法直接更改 ) :\nr'<a href='contest.php?cid=\d\d\d\d\'>(.*?)</a></td><td>'\n第二次筛选正则表达式 ( 无法直接更改 ):\nr'.*?计算机21-4/5/6.*?'\n是否输出结果为文件 ( resultKeys.txt ) ( T or F ):\nT\n是否输出结果数量为文件 ( resultKeysNum.txt ) ( T or F ):\nT\n\n\n备注\n无法直接更改项请移步 Python 源代码变量区自行更改 ( findFirstResults & findSecondResults )。\n此代码没有人性化，只有最基础的实现，T 和 F 注意大小写。\n:)"

main() #运行程序