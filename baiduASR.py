from aip import AipSpeech


class BaiduASR:
    def __init__(self):
        self.APP_ID = '10344784'
        self.API_KEY = 'ntBxeNDRR7ClOpyAKNEWVsgI'
        self.SECRET_KEY = 'I4VXri68eo06EmO0SCCwkXHvszNPhQSq'

    # 读取文件
    def get_file_content(self, filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    def main_asr(self):
        aipSpeech = AipSpeech(self.APP_ID, self.API_KEY, self.SECRET_KEY)
        # 识别本地文件
        # 目前支持的格式较少，原始 PCM 的录音参数必须符合 8k/16k 采样率、16bit 位深、单声道，支持的格式有：pcm（不压缩）、wav（不压缩，pcm编码）、amr（压缩格式）。
        result = aipSpeech.asr(self.get_file_content('voice.wav'), 'wav', 16000, {'lan': 'zh', })
        print(result)
        print(result['result'][0])
        return result['result'][0]

if __name__ == "__main__":
    asr = BaiduASR()
    asr.main_asr()