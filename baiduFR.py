from aip import AipFace


# 开始人脸识别
class BaiduFR:
    """ 你的 APPID AK SK """
    def __init__(self):
        self.APP_ID = '10344784'
        self.API_KEY = 'ntBxeNDRR7ClOpyAKNEWVsgI'
        self.SECRET_KEY = 'I4VXri68eo06EmO0SCCwkXHvszNPhQSq'



    # 读取图片
    def get_file_content(self,filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    def fr_main(self):
        aipFace = AipFace(self.APP_ID, self.API_KEY, self.SECRET_KEY)
        result = aipFace.identifyUser('group1', self.get_file_content('01.png'))

        print(result)
        scores = result['result'][0]['scores'][0]
        if scores >= 80:
            print('认证成功')