import os
import speech_recognition as sr
from pydub.silence import split_on_silence
from pydub import AudioSegment


def audio_to_txt(audio_file_path):
    message = None
    audio_file = sr.AudioFile(audio_file_path)
    r = sr.Recognizer()  # Speech recognition
    with audio_file as audio_f:
        audio = r.record(audio_f)
    try:
        message = r.recognize_google(audio)
        print(message)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio_list")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return message


if __name__ == '__main__':
    for i in range(1, 101):
        dir_name = 'audio_segment/'+str(i)
        os.makedirs(dir_name, exist_ok=True)

    for i in range(1, 101):
        audio_file_path = 'audio/' + str(i) + '.wav'
        audio = AudioSegment.from_wav(audio_file_path)

        word_audio_list = split_on_silence(audio, min_silence_len=500, silence_thresh=-100)

        for j, word_audio in enumerate(word_audio_list):
            out_file_path = 'audio_segment/' + str(i) + '/' + str(i) + '_' + str(j) + '.wav'
            word_audio.export(out_file_path, format="wav")

        txt_name = 'txt/' + str(i) + '.txt'
        with open(txt_name, 'w') as f:
            for j, file in enumerate(os.listdir('audio_segment/' + str(i))):
                file_path = 'audio_segment/' + str(i) + '/' + str(i) + '_' + str(j) + '.wav'
                message = audio_to_txt(file_path)
                if message is None:
                    f.write('???'+txt_name)
                    f.write('\n')
                else:
                    f.write(message)
                    f.write('\n')
