# Audio Searcher

このコードは音声ファイル内の言葉を検索するためのものです。  
例えば授業や会議等で「課題のことについてだけ聞き返したいなっ」という時にこれを使うと見つけられちゃいます⭐️  
機能的にはGoogleの音声認識サービスを使ってテキストに変換しています

## How to use

下記は私の環境（apple M1,Python 3.9.10）で実際に動かしたコードです^^*

```sh
from audio_searcher.audio_search import AudioSearcher
##階層は自分で調節してね！！

if __name__ == "__main__":
    audio_file = "sample_audio.mp3"  # 音声ファイルへのパスを指定してね
    keyword = "見て"  # 検索したいキーワードを指定してね

    searcher = AudioSearcher(language='ja-JP')  # 使用する言語を指定します
    transcribed_text = searcher.transcribe(audio_file)
    
    if "Could not" not in transcribed_text:
        print("Transcribed Text:", transcribed_text)
        occurrences = searcher.search_keyword(transcribed_text, keyword)
        if occurrences:
            print(f"Keyword '{keyword}' found at positions: {occurrences}")
        else:
            print(f"Keyword '{keyword}' not found in the text.")
    else:
        print(transcribed_text)
```

## Installation

使ってみてね  
You can install the package using pip:

```sh
pip install audio_searcher

