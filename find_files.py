import os
def getFiles(dir, suffix): # 查找根目录，文件后缀 
    res = []
    for root, _, files in os.walk(dir):  # =>当前根,根下目录,目录下的文件
        for filename in files:
            _, suf = os.path.splitext(filename) # =>文件名,文件后缀
            if suf == suffix:
                res.append(os.path.join(root, filename)) # =>吧一串字符串组合成路径
    return res
#下面是测试代码：
#for file in getFiles("D:\\c_data\\video", '.mp4'):  # =>查找以.py结尾的文件
#    print(file)