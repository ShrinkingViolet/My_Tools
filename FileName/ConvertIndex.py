import os
import re
import string
import shutil
digit = {'一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9}

def _trans(s):
    num = 0
    if s:
        idx_q, idx_b, idx_s = s.find('千'), s.find('百'), s.find('十')
        if idx_q != -1:
            num += digit[s[idx_q - 1:idx_q]] * 1000
        if idx_b != -1:
            num += digit[s[idx_b - 1:idx_b]] * 100
        if idx_s != -1:
            # 十前忽略一的处理
            num += digit.get(s[idx_s - 1:idx_s], 1) * 10
        if s[-1] in digit:
            num += digit[s[-1]]
    num = str(num)
    if len(num) == 1:
            num = '0' + num
    return num

def trans(chn):
    chn = chn.replace('零', '')
    idx_y, idx_w = chn.rfind('亿'), chn.rfind('万')
    if idx_w < idx_y:
        idx_w = -1
    num_y, num_w = 100000000, 10000
    if idx_y != -1 and idx_w != -1:
        return trans(chn[:idx_y]) * num_y + _trans(chn[idx_y + 1:idx_w]) * num_w + _trans(chn[idx_w + 1:])
    elif idx_y != -1:
        return trans(chn[:idx_y]) * num_y + _trans(chn[idx_y + 1:])
    elif idx_w != -1:
        return _trans(chn[:idx_w]) * num_w + _trans(chn[idx_w + 1:])
    return _trans(chn)


ext = '.' + 'epub'
path = '.' + os.sep

def getFileName(t_path):
    f_list = os.listdir(t_path)
    t_list = []
    for i in f_list:
        if os.path.splitext(i)[1] == ext:
            t_list.append(i)
    return t_list

##(?<=第).*?(?=卷)
##第.*?卷
if __name__ == '__main__':
    f_list = getFileName(path)
    for i in f_list:
        oldname = path + i
        name_list = re.findall(r'^.*?(?=_)',i)
        if len(name_list) == 0:
            continue
        name = name_list[0]
        if os.path.isdir(path+name+os.sep) == 0:
            os.mkdir(name)
        index = re.findall(r'(?<=第).*(?=卷)',i)
        if len(index) == 0:
            continue
        num_index = re.findall(r'(?<=第)[1-9\.]*(?=卷)',i)
        if len(num_index) == 0:
            num = trans(index[-1])
        else :
            num = num_index[-1]
        # newname = path + re.sub(r'第.*?卷', num, i)
        newname = path + name + os.sep + name + '_' + num + ext
        print('old:',oldname,'=====>',"new:",newname,'\n')
        # os.rename(oldname,newname)
        shutil.move(oldname,newname)
        
