import pandas as pd

def load_csv(file_path):
    """CSVファイルを読み込む

    Args:
        file_path (str): CSVファイルのパス

    Returns:
        pd.DataFrame: 読み込んだデータ
    """
    return pd.read_csv(file_path)