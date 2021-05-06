import os
old_ext = '.' + 'epub'
new_ext = '.' + 'html'
path = '.' + os.sep

def getFileName(t_path):
    f_list = os.listdir(t_path)
    t_list = []
    for i in f_list:
        if os.path.splitext(i)[1] == old_ext:
            t_list.append(i)
    return t_list

if __name__ == '__main__':
    f_list = getFileName(path)
    for i in f_list:
        oldname = path + i
        name = os.path.splitext(i)[0]
        newname = path + name + new_ext
        print('old:',oldname,'=====>',"new:",newname,'\n')
        os.rename(oldname,newname)