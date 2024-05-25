import librosa
import pandas as pd
import glob

def extract_mfcc_features(folder_path, output_csv, extension):
    # 音声ファイルのパスを取得
    audio_files = glob.glob(folder_path + "/*." + extension)

    # MFCC特徴量を格納するリスト
    mfcc_data = []

    # 全ての音声ファイルに対してMFCC特徴量を抽出
    for file in audio_files:
        # 音声ファイルを読み込み
        y, sr = librosa.load(file, sr=None)

        # MFCC特徴量を抽出
        mfcc = librosa.feature.mfcc(y=y, sr=sr)

        # MFCC特徴量を平均化
        avg_mfcc = mfcc.mean(axis=1)  # 時間軸に沿って平均を取る

        # MFCC特徴量をリストに追加
        mfcc_data.append(avg_mfcc)

    # MFCC特徴量をDataFrameに変換
    df = pd.DataFrame(data=mfcc_data)

    # CSVファイルに保存
    df.to_csv(output_csv, index=False)

# フォルダーのパスと出力CSVファイル名を指定してMFCC特徴量を抽出
# extension = "mp3"
# folder_path = "/Users/nenesuga/dstokuron/src/music"
# output_csv = "/Users/nenesuga/dstokuron/src/res/audio_v2.csv"
# extract_mfcc_features(folder_path, output_csv, extension)
