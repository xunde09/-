import os

for x in range(217000, 2171974):
    path = '9c7a4b3b%s.ts'%x
    try:
        with open(path,'rb') as f:
                with open('dy.mp4','ab') as F:
                    F.write(f.read())
                    print('写入完成')
                    if os.path.exists(path):
                        os.remove(path)
    except:
        pass
