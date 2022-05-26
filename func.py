import time

def daylylog(msg):
    try:
        file_handle=open('daylylog.txt',mode='a')
        file_handle.writelines([time.strftime("%Y/%m/%d %H:%M:%S"),msg,'\n'])
        file_handle.close()
        print(time.strftime("%Y/%m/%d")+" "+msg)
    except Exception as e:
        print("daylylog有错误:", e)

