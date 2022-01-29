import os
import pathlib

from PIL import Image
import zipfile
import os
########Unzipping

def unzip(files):
    for x in backups:
        with zipfile.ZipFile(x, 'r') as myfile:
            myfile.extractall(x[0: -4])

##### comparing
filelist = [file for file in os.listdir('C:/Users/KUV3LR/Desktop/unzip test/20211214_15_55_dai_pp5_Explmd/Explmd') if file.endswith('.png')]
filelist2 = [file for file in os.listdir('C:/Users/KUV3LR/Desktop/unzip test/20211214_18_06_dai_pp5_Explmd/Explmd') if file.endswith('.png')]
print("11111",filelist)
print("22222",filelist2)
format(list)


s = [s for s in filelist if s in filelist2]
print("images compared",s)

for s in filelist:
    for s1 in filelist2:
        if s == s1:
            print("success")
            myfolder = 'C:/Users/KUV3LR/Desktop/unzip test/Vikas'
            if os.path.isdir(myfolder):
                print("Exists")

            else:
                print("Doesn't exists")
                os.mkdir(myfolder)
            print ('merge')
            break
        else:
            print ('i am back')
			
			
			########Merging/Combining
			
			
			
			
			im1 = Image.open('C:\Users\KUV3LR\PycharmProjects\pythonProject1\\Analysis_ExplMD_Sim_TCycle-testcase_explmd_0001_Fwd_S.png')
im2 = Image.open('C:\Users\KUV3LR\PycharmProjects\pythonProject1\\Analysis_ExplMD_Sim_TCycle-testcase_explmd_0001_Fwd_time.png')
#print ('hello')

#im1= im1.resize((1280,1440))
#im1.show()


def get_concat_h(im1, im2):
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst

def get_concat_v(im1, im2):
    dst = Image.new('RGB', (im1.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst

   