import os
import re
import string
common_used_numerals_tmp ={'零':0, '一':1, '二':2, '两':2, '三':3, '四':4, '五':5, '六':6, '七':7, '八':8, '九':9, '十':10, '百':100, '千':1000, '万':10000, '亿':100000000}
def ch2int(uchar):
    sep_char = re.split(r'亿|万',uchar)
    total_sum = 0
    for i,sc in enumerate(sep_char):
        split_num = sc.replace('千', '1000').replace('百', '100').replace('十', '10')
        int_series = re.split(r'(\d{1,})', split_num)
        int_series.append("")
        int_series = ["".join(i) for i in zip(int_series[0::2],int_series[1::2])]
        int_series = ['零' if i == '' else i for i in int_series]
        num = 0
        for ix, it in enumerate(int_series):
            it = re.sub('零', '', it) if it != '零' else it
            ##print("level 2:{}{}".format(ix,it))
            temp = common_used_numerals_tmp[it[0]]*int(it[1:]) if len(it)>1 else common_used_numerals_tmp[it[0]]
            num += temp
        total_sum += num * (10 ** (4*(len(sep_char) - i - 1)))
        total_sum = str(total_sum)
        if len(total_sum) == 1:
            total_sum = '0' + total_sum
    return total_sum

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
        index = re.findall(r'(?<=第).*?(?=卷)',i)
        if len(index) == 0:
            continue
        num = ch2int(index[-1])
        newname = path + re.sub(r'第.*?卷', num, i)
        print('old:',oldname,'=====>',"new:",newname,'\n')
        os.rename(oldname,newname)
