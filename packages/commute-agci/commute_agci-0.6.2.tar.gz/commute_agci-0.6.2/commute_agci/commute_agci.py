import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager
from datetime import datetime
import geopy.distance  # 地理空間分析用のインポート

class GasChromatographyAnalysis:
    
    def __init__(self):
        # 日本語フォントを設定
        self.font_path = '/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc'  # macOSの標準日本語フォントパス
        self.font_prop = font_manager.FontProperties(fname=self.font_path)
        plt.rcParams['font.family'] = self.font_prop.get_name()

    def record_commute(self, start_time, end_time, mode_of_transport='car', origin_coords=None, destination_coords=None, file_path='commute_data.csv'):
        """
        通勤時間と距離をCSVファイルに記録し、移動手段も記録します。

        Args:
            start_time (str): 開始時間 (HH:MM形式).
            end_time (str): 終了時間 (HH:MM形式).
            mode_of_transport (str, optional): 移動手段 (車、自転車、バスなど)。デフォルトは 'car' です。
            origin_coords (tuple, optional): 出発地の座標 (緯度, 経度)。デフォルトはNoneです。
            destination_coords (tuple, optional): 目的地の座標 (緯度, 経度)。デフォルトはNoneです。
            file_path (str, optional): データを保存するCSVファイルへのパス。デフォルトは 'commute_data.csv' です。
        """

        # 通勤時間を計算
        start = datetime.strptime(start_time, '%H:%M')
        end = datetime.strptime(end_time, '%H:%M')
        duration = (end - start).seconds / 60  # 分に変換

        # 距離を計算
        if origin_coords and destination_coords:
            distance = geopy.distance.distance(origin_coords, destination_coords).km
        else:
            distance = None

        # 移動手段を含むデータレコード
        try:
            data = pd.read_csv(file_path)
        except FileNotFoundError:
            data = pd.DataFrame(columns=['開始時間', '終了時間', '時間', '移動手段', '距離'])
        
        new_data = pd.DataFrame([[start_time, end_time, duration, mode_of_transport, distance]],
                                columns=['開始時間', '終了時間', '時間', '移動手段', '距離'])
        
        data = pd.concat([data, new_data])
        data.to_csv(file_path, index=False)

    def analyze_commute(self, file_path='commute_data.csv', group_by='移動手段'):
        """
        記録された通勤時間を分析し、グループ化と潜在的な地理空間分析を行います。

        Args:
            file_path (str, optional): データを保存するCSVファイルへのパス。デフォルトは 'commute_data.csv' です。
            group_by (str, optional): データをグループ化するフィールド ('移動手段' など)。デフォルトは '移動手段' です。

        Returns:
            tuple: 平均通勤時間と分析されたデータを含むタプル.
        """

        data = pd.read_csv(file_path)
        data['時間'] = pd.to_numeric(data['時間'], errors='coerce')  # 時間列を数値に変換
        avg_duration = data['時間'].mean()

        # 移動手段またはその他の関連フィールドでグループ化
        grouped_data = data.groupby(group_by).agg({'時間': 'mean'}).reset_index()  # グループごとの平均時間計算

        return avg_duration, grouped_data

    def plot_commute(self, data, output_path='commute_analysis.png', x_axis='移動手段', y_axis='時間', title='通勤時間分析'):
        """
        カスタマイズ可能なオプションで通勤データをプロットします。

        Args:
            data (pandas.DataFrame): プロットするデータ。
            output_path (str, optional): プロット画像を保存するパス。デフォルトは 'commute_analysis.png' です。
            x_axis (str, optional): X軸に使用するフィールド。デフォルトは '開始時間' です。
            y_axis (str, optional): Y軸に使用するフィールド。デフォルトは '時間' です。
            title (str, optional): プロットのタイトル。デフォルトは '通勤時間分析' です。
        """

        plt.figure(figsize=(10, 6))
        plt.plot(data[x_axis], data[y_axis], marker='o', linestyle='-')
        plt.xlabel(x_axis)
        plt.ylabel(y_axis)
        plt.title(title)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(output_path)
        plt.close()

    def analyze_commute_distance(self, file_path='commute_data.csv', origin='自宅', destination='職場'):
        """
        外部APIまたはユーザー入力を使用して通勤距離を分析します。

        **注:** この機能には、地理空間APIに接続するか、ユーザーに始点と終点の座標を尋ねるための追加実装が必要です。

        Args:
            file_path (str, optional): データを保存するCSVファイルへのパス。デフォルトは 'commute_data.csv' です。
            origin (str, optional): 開始地点 (例: '自宅')。デフォルトは '自宅' です。
            destination (str, optional): 終点 (例: '職場')。デフォルトは '職場' です。
        """

        data = pd.read_csv(file_path)

        # 距離計算用のロジックを実装
        # 1. ユーザーに始点と終点の座標を入力させる
        # 2. 始点と終点の座標をAPIから取得する (例: Google Maps Distance Matrix API)

        # 例: ユーザー入力による座標取得
        origin_coords = input("始点の座標を入力 (緯度, 経度): ")
        destination_coords = input("終点の座標を入力 (緯度, 経度): ")

        # 距離計算
        distance = geopy.distance.distance((origin_coords), (destination_coords)).km

        # データフレームに距離を追加
        data['距離'] = distance

        # 距離に基づいた分析
        avg_distance_by_mode = data.groupby('移動手段')['距離'].mean()

        # 結果の表示
        print(f"平均通勤距離: {data['距離'].mean():.2f} km")
        print(f"移動手段ごとの平均通勤距離:")
        print(avg_distance_by_mode)

def main():
    """
    通勤データの記録、分析、プロットを行うメイン関数。
    """
    analysis = GasChromatographyAnalysis()

    # 例: 記録データ
    analysis.record_commute('08:00', '08:45', 'car')
    analysis.record_commute('09:00', '09:50', 'bike')

    # 分析
    avg_duration, grouped_data = analysis.analyze_commute()
    print(f"平均通勤時間: {avg_duration:.2f} 分")
    print(f"移動手段ごとの平均通勤時間:")
    print(grouped_data)

    # プロット
    analysis.plot_commute(data=grouped_data, x_axis='移動手段', y_axis='時間', title='移動手段ごとの平均通勤時間')

    # 距離分析 (コメントアウトされている部分を実装する必要があります)
    # analysis.analyze_commute_distance()

if __name__ == '__main__':
    main()
