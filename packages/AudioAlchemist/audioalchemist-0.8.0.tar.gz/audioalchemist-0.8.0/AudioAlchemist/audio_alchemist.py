import pydub
import glob
import os
# import pandas as pd

class AudioAlchemist:
    def __init__(self, input_folder, output_folder, input_extension, output_extension):
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.input_extension = input_extension
        self.output_extension = output_extension

    def process_files_index(self):
        filelist = glob.glob(self.input_folder)
        i = 0
        # Each file is read and a serial number is added and output
        for file in filelist:
            source_audio = pydub.AudioSegment.from_file(file, self.input_extension)
            # Output the result
            output_file = self.output_folder + str(i) +"."+ self.output_extension
            source_audio.export(output_file, format=self.output_extension)
            i += 1
        print("Processing completed")
    # Create an instance of the AudioAlchemist class and call the process_files method

    def process_files_namekeep(self):
        # globパターンを修正して、フォルダ内のすべてのファイルを取得
        filelist = glob.glob(self.input_folder)
        for file in filelist:
            # os.path.splitextを使用してファイル名と拡張子を分離
            filename = os.path.splitext(os.path.basename(file))[0]
            source_audio = pydub.AudioSegment.from_file(file, format=self.input_extension)
            # 変換前のファイル名を保持して出力ファイル名を生成
            output_file = os.path.join(self.output_folder, filename + '.' + self.output_extension)
            source_audio.export(output_file, format=self.output_extension)
        print("Processing completed")

# # フォルダパスを設定
# input_folder = 'C:/Users/hikar/ds/data/melody/*.wav'
# output_folder = 'C:/Users/hikar/ds/data/melody/'
# input_extension = "wav"
# output_extension = "mp3"

# audio_alchemist = AudioAlchemist(input_folder, output_folder, input_extension, output_extension)
# audio_alchemist.process_files_index()

# # 変換処理を実行
# AudioAlchemist(input_folder, output_folder, input_extension, output_extension)
