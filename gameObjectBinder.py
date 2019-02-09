#! /usr/lical/bin/python
import os
import sys
import yaml


def get_function_name(filename):
    # remove meta extension
    fullname = os.path.splitext(filename)[0]
    # remove origin extenson
    fullname = os.path.splitext(fullname)[0]
    # remove origin extenson
    # change rest dot to _
    fullname = fullname.replace('.', '_')
    # change - to __
    fullname = fullname.replace('-', "__")
    return fullname


def save_file(folder_name, file_list, guid_list):
    # create file name by folder
    real_folder = os.getcwd() + '\\' + folder_name + '\\' + folder_name + '.txt'
    f = open(real_folder, "w+")
    # write file_list into

    for filename in file_list:
        f.write('public ' + fileTypeName + ' ' + filename + ';\n')
    # write guid_list into
    f.write('\n')

    for i in range(0, len(file_list)):
        filename = file_list[i]
        guid = guid_list[i]
        f.write('  ' + filename+':' +
                ' {fileID: 21300000,'+' guid: '+guid + ', type: 3}\n')

    f.close()


def do_folder(folder_name):
    folder = os.getcwd() + '\\' + folder_name
    file_list = []
    guid_list = []
    for curfile in os.listdir(folder):
        if(curfile.endswith('meta')):
            finalFile = os.getcwd() + '\\' + folder_name + '\\' + curfile
            f = open(finalFile)
            va = yaml.load(f)
            file_list.append(get_function_name(curfile))
            guid_list.append(va['guid'])
    save_file(folder_name, file_list, guid_list)


fileTypeName = ''
if __name__ == '__main__':
    if(len(sys.argv) > 2):
        folder_name = sys.argv[1]
        fileTypeName = sys.argv[2]
        do_folder(folder_name)
    else:
        print('need folder name and type')
