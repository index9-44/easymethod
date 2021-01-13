# -*- coding: utf-8 -*-
import os,time,subprocess

def getCurrentTime(dirPath):
    """
    根据时间戳，创建指定输出文件
    :param dirPath:
    :return:
    """
    if os.path.exists(dirPath+time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))):
        print("error:此文件夹已经存在，请检查后，自行删除此时间戳下的文件夹")
    else:
        print("不存在")
        os.makedirs(dirPath+time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))
        print("创建 {} 成功".format(dirPath+time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))))
    print(time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))


def getPercent(doubleNum):
    """
    把小数转化为百分数
    :param doubleNum: double类型参数
    :return: 如：97.25%
    """
    return "%.2f%%" % (doubleNum * 100)

def getFiles(Path):
    """
    传入指定的路径，打印路径下面的所有文件
    :param Path: 路径
    :return:
    """
    for i in os.listdir(Path):
        print(i)


def getFatherPath(path):
    """
    获取指定路径下面文件夹的父路径
    :param path: 文件路径
    :return:
    """
    print(os.path.dirname(path))


def getFatherPath(path):
    """
    相关api
    :param path: 文件路径
    :return:
    """
    print(os.path.dirname(path))

    # 当前文件的路径
    # pwd = os.getcwd()
    # 当前文件的父路径
    father_path = os.path.abspath(os.path.dirname(path) + os.path.sep + ".")
    # 当前文件的前两级目录
    grader_father = os.path.abspath(os.path.dirname(path) + os.path.sep + "..")

    # print(pwd)
    print(father_path)
    print(grader_father)


def getAndroidLogcat():
    """
    实时获取安卓手机的日志
    :return:
    """
    order="adb logcat -v time"
    pi = subprocess.Popen(order, shell=True, stdout=subprocess.PIPE)
    for i in iter(pi.stdout.readline, 'b'):
        print(i)

