import pytest
import pandas as pd
from io import StringIO
from csv_summary.summary import summarize_csv

def test_summarize_csv(monkeypatch, capsys):
    # テスト用のCSVデータを作成
    test_csv = """A,B,C
1,4,7
2,5,8
3,6,9
"""
    # StringIOを使ってテスト用のデータフレームを作成
    test_data = StringIO(test_csv)
    df = pd.read_csv(test_data)

    # pandas.read_csvをモックしてテストデータを返すようにする
    def mock_read_csv(file_path):
        return df

    monkeypatch.setattr(pd, "read_csv", mock_read_csv)

    # summarize_csv関数をテスト実行
    summarize_csv("dummy_path.csv")

    # 標準出力をキャプチャ
    captured = capsys.readouterr()

    # 期待される出力を作成
    expected_output = """              A         B         C
count  3.000000  3.000000  3.000000
mean   2.000000  5.000000  8.000000
std    1.000000  1.000000  1.000000
min    1.000000  4.000000  7.000000
25%    1.500000  4.500000  7.500000
50%    2.000000  5.000000  8.000000
75%    2.500000  5.500000  8.500000
max    3.000000  6.000000  9.000000
"""

    # 期待される出力とキャプチャされた出力を比較
    assert captured.out == expected_output

if __name__ == "__main__":
    pytest.main()
