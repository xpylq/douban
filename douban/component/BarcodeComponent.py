# # -*- coding: utf-8 -*-
# import hprose
# import time
# import hashlib
# import zbar
#
#
#
# def decode_qr(img_url):
#     client = hprose.HttpClient('http://hprose.wwei.cn/qrcode.html')
#     api_id = 'qr217676'
#     api_key = '20170914163494'
#     timestamp = int(time.time())
#     version = '1.1'
#     md5 = hashlib.md5()
#     md5.update(api_key + str(timestamp) + img_url)
#     signature = md5.hexdigest()
#     result = client.qrdecode(api_id, signature, timestamp, img_url, '', version)
#     print result
#     print result['msg']
#
#
# def decode():
#     # 创建图片扫描对象
#     scanner = zbar.ImageScanner()
#     # 设置对象属性
#     scanner.parse_config('enable')
#     # 打开含有二维码的图片
#     img = Image.open('/Users/youzhihao/Downloads/image/群1.jpg').convert('L')
#     # 获取图片的尺寸
#     width, height = img.size
#     # 建立zbar图片对象并扫描转换为字节信息
#     qrCode = zbar.Image(width, height, 'Y800', img.tobytes())
#     scanner.scan(qrCode)
#     data = ''
#     for s in qrCode:
#         data += s.data
#     # 删除图片对象
#     del img
#     # 输出解码结果
#     print data
#
# if __name__ == '__main__':
#     img_url = "https://img1.doubanio.com/view/group_topic/llarge/public/p77784909.webp"
#     decode_qr(img_url)
#     # decode()
