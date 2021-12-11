import os
import shutil
import re


def copyFiles(src, dst):
    source_path = os.path.abspath(src)
    target_path = os.path.abspath(dst)

    if not os.path.exists(target_path):
        # 如果目标路径不存在原文件夹的话就创建
        os.makedirs(target_path)

    if os.path.exists(source_path):
        # 如果目标路径存在原文件夹的话就先删除
        shutil.rmtree(target_path)

    shutil.copytree(source_path, target_path)


def replace(fileName):
    replaced = ""
    codes = 0
    
    fileData = open(fileName).read().replace("\n\n\n", "\n").split("\n")
    
    for line in fileData:

        if "<img src=" in line and "../" not in line:
            tempPath = "/".join(re.findall('src="(.*?)"', line)[0].split('/')[:-2])
            if tempPath != "":
                line = line.replace(tempPath + "/", "")

            if "style=" in line:
                line = line.replace(re.findall('style=".*?"', line)[0], "width='700px'")

        if "```" in line:
            if codes == 0:
                codes = 1
            else:
                codes = 0
            replaced += line + "\n"
            continue
    
        if codes == 0:
            replaced += line.replace("	", "&emsp;") + "&emsp;  \n"
        else:
            replaced += line + "\n"
    
    with open(fileName, "w") as f:
        f.write(replaced)


# 不会遍历包含 “ . ” 的文件夹
def replaceDFS(path):
    try:
        files = list(os.walk(path))[0]
        for f in sorted(files[2] + files[1]):
            if ".md" in f:
                # print(path + "/" + f)
                replace(path + "/" + f)
            if '.' not in f:
                replaceDFS(path + "/" + f)

    except:
        print(path)

def FormatGithubBlogs(srcPath, dstPath):
    copyFiles(srcPath, dstPath)
    replaceDFS(dstPath)


FormatGithubBlogs('/home/lyp/文档/Books/Typora笔记/Original', '/home/lyp/文档/Books/Typora笔记/Formatted')
