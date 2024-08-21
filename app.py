import speech_recognition as sr

# 音声認識オブジェクトの初期化 
recognizer = sr.Recognizer()

# マイクからの音声を使用
with sr.Microphone() as source:
    print("話してください....")

    # マイクのノイズを調整
    recognizer.adjust_for_ambient_noise(source)

    # ユーザーの話す音声を記録
    audio = recognizer.listen(source)

    try:
        # Googleの音声認識APIを使用して音声をテキストに変換
        text = recognizer.recognize_google(audio, language="ja-JP")
        print("認識されたテキスト: " + text)
    except sr.RequestError as e:
        # APIからのエラー
        print("Google Speech Recognitionサービスからのエラー; {0}".format(e))
    except sr.UnknownValueError:
        # 音声認識不可
        print("音声が認識できませんでした")
