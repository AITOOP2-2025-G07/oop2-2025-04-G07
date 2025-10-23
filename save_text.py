"""
save_text.py
文字起こし結果をテキストファイルとして保存します（上書きしない）。
"""

import os
from datetime import datetime

def save_transcription(text: str, output_dir: str = "transcriptions") -> str:
    """
    文字起こし結果を日付付きファイルとして保存する関数。

    Args:
        text (str): 文字起こしされた文字列
        output_dir (str): 保存先ディレクトリ（デフォルト: "transcriptions"）

    Returns:
        str: 保存されたファイルのパス
    """
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"text_{timestamp}.txt"
    filepath = os.path.join(output_dir, filename)

    # 同じ名前がある場合は上書きしないように番号を付ける
    counter = 1
    while os.path.exists(filepath):
        filename = f"text_{timestamp}_{counter}.txt"
        filepath = os.path.join(output_dir, filename)
        counter += 1

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"保存完了: {filepath}")
    return filepath


if __name__ == "__main__":
    # 動作確認用
    sample_text = "これは文字起こし結果のテストです。"
    save_transcription(sample_text)
