import requests

# 文件保存位置
path = "/home/zeaslity/Pictures/abc.jpg"
# 网络图片位置
url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_" \
      "10000&sec=1526817837884&di=3db769aa15e5e539b55311c77f3d2188&imgtype=0&" \
      "src=http%3A%2F%2Fimage227-c.poco.cn%2Fmypoco%2Fmyphoto%2F20140726%2F18%2F17471643120140726184901049.jpg" \
      "%3F1024x683_120"
r = requests.get(url)
print(r.status_code)

with open(path, 'wb') as f:
    # 写入二进制的内容
    f.write(r.content)

f.close()
