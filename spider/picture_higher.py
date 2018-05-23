import requests
import os
"""
更加自动化的方式获取图片

"""
url = "https://timgsa.baidu.com/timg?image&quality=8" \
      "0&size=b9999_10000&sec=1526817837884&di=3db769aa15e5e539b55311c77f3d2188&imgtype=" \
      "0&src=http%3A%2F%2Fimage227-c.poco.cn%2F" \
      "mypoco%2Fmyphoto%2F20140726%2F18%2F17471643120140726184901049.jpg%3F1024x683_120"
root = "/home/zeaslity/Pictures/"
path = root + url.split('/')[-1]

try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件保存失败")

except:
    print("爬取失败")
