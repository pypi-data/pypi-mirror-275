import speech_recognition as sr
from pydub import AudioSegment
import os

class AudioSearcher:
    def __init__(self, language='en-US'):
        self.language = language
        self.recognizer = sr.Recognizer()

    def _convert_audio_format(self, audio_file, target_format='wav'):
        audio = AudioSegment.from_file(audio_file)
        audio = audio.set_frame_rate(16000).set_channels(1)
        temp_file = 'temp_audio.' + target_format
        audio.export(temp_file, format=target_format)
        return temp_file

    def transcribe(self, audio_file):
        temp_file = self._convert_audio_format(audio_file)
        with sr.AudioFile(temp_file) as source:
            audio_data = self.recognizer.record(source)
        os.remove(temp_file)  # Clean up temporary file
        try:
            text = self.recognizer.recognize_google(audio_data, language=self.language)
            return text
        except sr.UnknownValueError:
            return "Could not understand audio"
        except sr.RequestError as e:
            return f"Could not request results; {e}"

    def search_keyword(self, text, keyword):
        occurrences = []
        start = 0
        while True:
            start = text.find(keyword, start)
            if start == -1: 
                break
            occurrences.append(start)
            start += len(keyword)
        return occurrences

# Example usage
if __name__ == "__main__":
    audio_file = "example_audio.mp3"  # Replace with your audio file
    keyword = "課題"  # Replace with the word you want to search for

    searcher = AudioSearcher(language='en-US')
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

