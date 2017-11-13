import pyaudio
import queue

class Audio:
    '''
    录音类，使用pyaudio
    '''
    def __init__(self, rate=16000, frames_size=None, channels=None, device_index=None):
        '''
        录音类初始化
        :param rate:采样率
        :param frames_size:数据帧大小
        :param channels:通道数
        :param device_index:录音设备id
        '''
        self.sample_rate = rate
        self.frames_size = frames_size if frames_size else rate / 100
        self.channels = channels if channels else 1

        self.pyaudio_instance = pyaudio.PyAudio()

        self.stream = self.pyaudio_instance.open(
            start=False,
            format=pyaudio.paInt16,
            input_device_index=device_index,
            channels=self.channels,
            rate=int(self.sample_rate),
            frames_per_buffer=int(self.frames_size),
            stream_callback=self.__callback,
            input=True
        )

        self.sinks = []

    def start(self):
        '''
        开始录音
        :return:
        '''
        self.stream.start_stream()

    def stop(self):
        '''
        结束录音
        :return:
        '''
        self.stream.stop_stream()

    def __callback(self, in_data, frame_count, time_info, status):
        '''
        录音数据(pmc)回调
        :param in_data:录音数据
        :param frame_count:
        :param time_info:
        :param status:
        :return:
        '''
        for sink in self.sinks:
            sink.put(in_data)

        return None, pyaudio.paContinue





class SpeechRecognizer(object):

    def __init__(self):
        '''
        类初始化
        :param dueros:DuerOS核心实现模块实例
        '''

        self.listening = False
        self.audio_queue = queue.Queue()

    def put(self, audio):
        """
        语音pcm输入
        :param audio: S16_LE format, sample rate 16000 bps audio data
        :return: None
        """
        if self.listening:
            self.audio_queue.put(audio)


    def record(self, timeout=10000):
        time_elapsed = 0
        while self.listening or time_elapsed >= timeout:
            try:
                chunk = self.audio_queue.get(timeout=1.0)
            except queue.Empty:
                break

            yield chunk
            time_elapsed += 10  # 10 ms chunk

        self.listening = False