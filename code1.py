"""
audio_recorder.py

マイクから指定秒数録音し、WAVファイルとして保存するモジュール。
他モジュールから呼び出して利用することを想定しています。

使用例:
    from audio_recorder import record_audio

    file_path = record_audio(duration=10)
    print(f"録音ファイル: {file_path}")
"""


import ffmpeg
import time

# 録音時間（秒）
duration = 10
# 出力ファイル名
output_file = 'python-audio-output.wav'

"""
    指定した時間マイクから録音し、WAVファイルに保存します。

    Args:
        duration (int): 録音時間（秒）。デフォルトは10秒。
        output_dir (str): 録音ファイルの保存先ディレクトリ。
        filename (str): 保存ファイル名。

    Returns:
        str: 保存された録音ファイルのパス。

    Raises:
        Exception: ffmpeg実行またはファイル保存でのエラー。
    """

try:
    print(f"{duration}秒間、マイクからの録音を開始します...")
    # FFmpegコマンドを実行
    # -f <デバイス入力形式>: OSに応じたデバイス入力形式を指定
    #   - Windows: 'dshow' または 'gdigrab'
    #   - macOS: 'avfoundation'
    #   - Linux: 'alsa'
    # -i <入力デバイス名>: デバイス名を指定
    (
        ffmpeg
        .input(':0', format='avfoundation', t=duration) # macOSの例
        .output(output_file, acodec='pcm_s16le', ar='44100', ac=1)
        .run(overwrite_output=True)
    )
    print(f"録音が完了しました。{output_file}に保存されました。")

except ffmpeg.Error as e:
    print(f"エラーが発生しました: {e.stderr.decode()}")
except Exception as e:
    print(f"予期せぬエラー: {e}")