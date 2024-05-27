import io
import soundfile as sf
from google.cloud import speech_v1p1beta1 as speech

def transcribe_audio(audio_file_path):
    # 音声ファイルのサンプルレートを読み取る
    data, sample_rate = sf.read(audio_file_path)
    
    # 音声ファイルをバイナリモードで読み込む
    with io.open(audio_file_path, "rb") as audio_file:
        content = audio_file.read()

    # Google Cloud Speech-to-Textのクライアントを作成
    client = speech.SpeechClient()

    # 音声ファイルを認識してテキストに変換
    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=sample_rate,
        language_code="ja-JP",
    )

    response = client.recognize(config=config, audio=audio)

    # 変換されたテキストを取得
    transcripts = []
    for result in response.results:
        transcripts.append(result.alternatives[0].transcript)

    return transcripts

# テスト用の音声ファイルのパス
audio_file_path = "./test.wav"

# 音声をテキストに変換する
transcribed_text = transcribe_audio(audio_file_path)
print("Transcribed Text:")
for text in transcribed_text:
    print(text)

