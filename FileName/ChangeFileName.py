import re
import os

path = '.' + os.sep
vedio_ext = ['.mp4','.mkv','.flv','.avi','.wmv']
ass_ext = '.ass'

def getFileList(t_path):
    f_list = os.listdir(t_path)
    t_list = []
    for i in f_list:
        if os.path.splitext(i)[1] == ass_ext:
            t_list.append(i)
    return t_list

def getFileName(t_path):
    f_list = os.listdir(t_path)
    for i in f_list:
        for j in vedio_ext:
            if os.path.splitext(i)[1] == j:
                name = re.sub(r'(?<=\[)[0-9]+(?=\])','$$--$$',os.path.splitext(i)[0]) #视频名格式
                return name + ass_ext
            
if __name__ == '__main__':
    f_list = getFileList(path)
    name = getFileName(path)
    for i in f_list:
        index = re.findall(r'(?<=\[)[0-9]+(?=\])',i) #字幕名格式
        oldname = path + i
        index = re.findall(r'(?<=\[)[0-9]+(?=\])',i) #字幕名格式
        if len(index) == 0:
            continue
        newname = path + re.sub(r'(?<=\[)\$\$--\$\$(?=\])', index[-1], name) #视频名格式
        print('old:',oldname,'=====>',"new:",newname,'\n')
        os.rename(oldname,newname)
