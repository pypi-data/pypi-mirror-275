def normalize_data(data):
    """データを正規化する

    Args:
        data (list): データのリスト

    Returns:
        list: 正規化されたデータ
    """
    min_val = min(data)
    max_val = max(data)
    return [(x - min_val) / (max_val - min_val) for x in data]