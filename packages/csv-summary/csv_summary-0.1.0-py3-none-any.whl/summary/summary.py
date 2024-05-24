import pandas as pd
import os

def summarize_csv(file_path):
    """
    指定したCSVファイルの統計情報を表示し、レポートを生成する関数。

    Parameters:
        file_path (str): CSVファイルのパス。
    """
    if not os.path.exists(file_path):
        print(f"Error: {file_path} が存在しません。")
        return

    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print(f"Error: CSVファイルの読み込みに失敗しました。{e}")
        return

    report = {}

    # 各カラムの統計情報
    report['description'] = df.describe(include='all')

    # 欠損値の確認
    report['missing_values'] = df.isnull().sum()

    # カテゴリカルデータの頻度分布
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns
    report['categorical_summary'] = {col: df[col].value_counts() for col in categorical_cols}

    report_file = 'summary_report.txt'
    with open(report_file, 'w') as f:
        for key, value in report.items():
            f.write(f"{key}:\n{value}\n\n")

    print(f"レポートが {report_file} に保存されました。")
