#coding:utf-8
__author__ = 'jianghu'

from PIL import Image
import os,sys
file = r'C:\Users\pc\Desktop\ty\pic\26.bmp'
filepath = r'C:\Users\pc\Desktop\ty\pic'
splitlfilepath = r'C:\Users\pc\Desktop\ty\char'
ocrpath= r'C:\Users\pc\Desktop\ty\split'
pic_size = (15, 15)
readnub = 0

def ready2(im):
    #由于新浪注册码的特殊形式，可以分离背景和前景。白色背景，黑色前景（设置为255）
    #im = im.convert('L')
    global readnub
    im.save(r'C:\Users\pc\Desktop\ty\read\01.bmp')
    newlist=[]
    for i in  list(im.getdata()):
        if i[0]>150:x =255
        else:x = 0
        if i[1]>150:y =255
        else:y = 0
        if i[2]>150:z =255
        else:z = 0
        if 255 in (x,y,z) and 0 in (x,y,z):
            x,y,z = 255,255,255
        newlist.append((x,y,z))

    newim = Image.new(im.mode,im.size)
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            newim.putpixel((x,y),newlist[y*im.size[0]+x])

    #newim.convert('L')
    #newim.convert('1')
    newim=newim.crop((1,1,newim.size[0],newim.size[1]))
    imim = newim.load()
    for i in xrange(newim.size[0]):
        for j in xrange(newim.size[1]):
            if not ltx(imim,i,j):
                newim.putpixel((i,j),(255,255,255))

    newim.save(r'C:\Users\pc\Desktop\ty\read\0'+str(readnub)+'.bmp')
    #print list(newim.getdata())
    #os.system(r'C:\Users\pc\Desktop\ty\read\0'+str(readnub)+'.bmp')
    readnub+=1
    return newim

def split_pic(im,pic_nmb=0):
    imim = im.load()
    WIDTH = im.size[0]
    HEIGHT = im.size[1]
    i = 0
    has_start = False
    chars = []
    while i < WIDTH:
        all_none = True
        for j in xrange(1,HEIGHT):
            if imim[i, j] == (0,0,0) and  ltx(imim,i,j):
                all_none = False
        if all_none:
            if has_start:
                end_x = i
                has_start = False
                char = im.crop((start_x, 0, end_x, HEIGHT))
                #char.save(r'C:\Users\pc\Desktop\split'+r'\0'+str(start_x)+'.jpg')

                charchar = char.load()
                width = end_x - start_x
                y1 = 0
                y2 = HEIGHT - 1
                all_none = True
                while all_none:
                    for ii in xrange(width):
                        if charchar[ii, y1] != (255,255,255):
                            all_none = False
                    y1 += 1
                all_none = True
                while all_none:
                    for ii in xrange(width):
                        if charchar[ii, y2] != (255,255,255):
                            all_none = False
                    y2 -= 1
                char = char.crop((0, y1 - 1, width, y2 + 2))
                if len(list(char.getdata()))<9:continue
                char = char.resize(pic_size) #将图片缩放到统一的大小
                #char.save(r'ty_'+str(pic_nmb)+'.bmp')
                pic_nmb+=1
                chars.append(char)
        else:
            if not has_start:
                start_x = i
                has_start = True
        i += 1
    return chars,pic_nmb

def train(): #训练：提取字模特征，存入txt文件，用于识别时的对比。
    list = []
    charmodel = open(r'tymodel.txt','w+')
    for filename in os.listdir(splitlfilepath):
        im = Image.open(splitlfilepath+r'\\'+filename)
        im_loaded = im.load()
        nstr = ''
        for x in range(im.size[0]):
            for y in range(im.size[1]):
                if im_loaded[x, y] == (255,255,255):
                    nstr += '0'
                else:
                    nstr += '1'
        if nstr in  list:
            continue
        else:
            list.append(nstr)
        char = filename[0]
        charmodel.write(nstr+':'+char+'\n')
    charmodel.close()
    return

def predict(imgpath):
    pattern = []
    res = ''
    char_model = open(r'tymodel.txt','r')
    for line in char_model.read().split('\n'):
        pattern.append(line.split(':'))
    char_model.close()
    del pattern[-1]
    im= Image.open(imgpath)
    im = im.convert()
    chars ,n= split_pic(ready2(im))
    for char in chars:
        res += what(char,pattern)
    return res

def what(im,pattern):
    imload = im.load()
    nstr = ''
    for x in xrange(im.size[0]): #生成目标图像的特征字符串
        for y in xrange(im.size[1]):
            if imload[x, y] == (255,255,255):
                nstr += '0'
            else:
                nstr += '1'
    minmin = im.size[0]*im.size[1]
    res = None
    for p in pattern:
        cur = 0
        for i in xrange(im.size[0]*im.size[1]):
            if nstr[i] != p[0][i]: #比对每一个像素，如果不相同，则增加差异值
                cur += 1
        if cur < minmin: #记录下差异值最小时所对应的字符
            minmin = cur
            res = p[1]
    return res

def ltx(arry,i,j):#判断是否孤立点
    pint = arry[i,j]
    try:
        lpint = arry[i-1,j]
        rpint = arry[i+1,j]
        upint = arry[i,j+1]
        dpint = arry[i,j-1]
        lupint = arry[i-1,j+1]
        ldpint = arry[i-1,j-1]
        rupint = arry[i+1,j+1]
        rdpint = arry[i+1,j-1]
        if pint in (lpint,rpint,upint,dpint,lupint,ldpint,rupint,rdpint):
            return True #不是孤立点
        else:
            return False
    except:
        return False

def split_pics():
    pic_nmb=0
    for file in os.listdir(filepath):
        if os.path.isdir(filepath+"\\"+file):continue
        print file
        im = Image.open(filepath+r'\\'+file)
        im = im.convert()
        newim = ready2(im)
        chars,pic_nmb = split_pic(newim,pic_nmb)
        #raw_input('next')
    return


if __name__=="__main__":
    im = Image.open(file)
    newim = ready2(im)
    chars,pic_nmb = split_pic(newim)
    arg = sys.argv
    #train()
    try:
        pic_path = arg[1]
        print predict(pic_path)
    except:
        exit(-1)