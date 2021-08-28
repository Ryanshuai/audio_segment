import os
from pydub.silence import split_on_silence, detect_nonsilent
from pydub import AudioSegment


if __name__ == '__main__':
    for i in range(1, 101):
        dir_name = 'audio_segment/'+str(i)
        os.makedirs(dir_name, exist_ok=True)

    for i in range(84, 85):
        audio_file_path = 'audio/' + str(i) + '.wav'
        audio = AudioSegment.from_wav(audio_file_path)
        not_silence_ranges = detect_nonsilent(audio, min_silence_len=700, silence_thresh=-100)

        # for start_i, end_i in not_silence_ranges:
        #     print(end_i-start_i)

        end_d = 0
        for counter, (start_i, end_i) in enumerate(not_silence_ranges):
            if counter > 7:
                break
            if end_i - start_i > 2500:
                end_d = end_i

        sentence_audio = audio[0:end_d]

        new = AudioSegment.empty()
        new += sentence_audio
        # new += AudioSegment.silent(duration=500)

        out_file_path = 'sentence/' + str(i) + '.wav'
        new.export(out_file_path, format="wav")
        print(out_file_path)

