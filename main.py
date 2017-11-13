from mic_1 import Audio


def main():
    audio = Audio()

    audio.start()

    while True:
        try:
            try:
                print('\n')
                input('单击[Enter]建，然后发起对话\n')
            except SyntaxError:
                pass
            # 唤醒态提示音

        except KeyboardInterrupt:
            break


    audio.stop()
    print('audio stoped')


if __name__ == '__main__':
    main()
