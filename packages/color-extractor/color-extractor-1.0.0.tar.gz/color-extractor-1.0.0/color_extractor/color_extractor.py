#########################################################################################

# no.2 メインカラーの割合も表示
import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from scipy.spatial.distance import pdist, squareform
import itertools

# サンプル画像のパス
image_path_1 = "./pink_and_lightblue.jpeg"
image_path_2 = "./red_and_blue.png"
image_path_3 = "./warms.jpeg"
image_path_4 = "./vermeer.jpeg"

# サンプル画像のパス
image_path = image_path_1
min_distance = 10
num_colors = 2

def extract_main_colors(image_path, num_colors, min_distance, min_ratio=0.01):
    """
    画像中のメインカラーをクラスタリングを用いて抽出する。

    Args:
        image_path (str): 画像のファイルパス
        num_colors (int): 抽出するメインカラーの数

    Returns:
        tuple: メインカラーのリスト（BGR形式）と各色の割合リスト
    """
    # 画像の読み込み
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image not found at path: {image_path}")

    # 画像をBGRからRGBに変換
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # 画像のピクセルをリシェイプ
    pixels = image.reshape((-1, 3))

    # K-meansクラスタリングの実行
    kmeans = KMeans(n_clusters=num_colors, random_state=42)
    kmeans.fit(pixels)
    
    # クラスタセンター（メインカラー）を取得
    all_colors = kmeans.cluster_centers_.astype(int)

    # 各クラスタの割合を計算
    labels, counts = np.unique(kmeans.labels_, return_counts=True)
    total_pixels = pixels.shape[0]
    all_ratios = counts / total_pixels

    # クラスタの中心間の距離を計算
    distances = pdist(all_colors, metric='euclidean')
    distance_matrix = squareform(distances)

    # クラスタの統合
    merged_colors = []
    merged_ratios = []
    skip = set()
    for i in range(len(all_colors)):
        if i in skip:
            continue
        color_sum = all_colors[i] * all_ratios[i]
        ratio_sum = all_ratios[i]
        for j in range(i + 1, len(all_colors)):
            if j in skip:
                continue
            if np.any(np.abs(all_colors[i] - all_colors[j]) < min_distance):
                color_sum += all_colors[j] * all_ratios[j]
                ratio_sum += all_ratios[j]
                skip.add(j)
        merged_colors.append((color_sum / ratio_sum).astype(int))
        merged_ratios.append(ratio_sum)

    # 割合がmin_ratio以上のメインカラーのみ抽出
    main_colors = []
    color_ratios = []
    for color, ratio in zip(merged_colors, merged_ratios):
        if ratio >= min_ratio:
            main_colors.append(color)
            color_ratios.append(ratio)

    return main_colors, color_ratios

def neutral_color(colors):
    """
    色のリストから各色の中間色を計算する。

    Args:
        colors (list): RGB形式のカラーリスト

    Returns:
        list: 中間色のリスト（RGB形式）
    """
    if len(colors) <= 1:
        return []

    # RGBをHSVに変換
    hsv_colors = rgb_to_hsv(colors)
    
    # 2色の組み合わせを生成し、中間色を計算
    intermediate_colors_hsv = []
    for color1, color2 in itertools.combinations(hsv_colors, 2):
        intermediate_color = [(c1 + c2) // 2 for c1, c2 in zip(color1, color2)]
        intermediate_colors_hsv.append(intermediate_color)

    # 中間色をRGBに変換
    intermediate_colors_rgb = hsv_to_rgb(intermediate_colors_hsv)

    return intermediate_colors_rgb

def rgb_to_hsv(rgb_colors):
    """
    RGBカラーをHSVカラーに変換する。

    Args:
        rgb_colors (list): RGB形式のカラーリスト

    Returns:
        list: HSV形式のカラーリスト
    """
    # numpy配列に変換
    rgb_colors = np.array(rgb_colors, dtype=np.uint8).reshape(-1, 1, 3)
    # RGBからHSVに変換
    hsv_colors = cv2.cvtColor(rgb_colors, cv2.COLOR_RGB2HSV)
    # 変換した結果をリストに変換して返す
    return hsv_colors.reshape(-1, 3).tolist()

def hsv_to_rgb(hsv_colors):
    """
    HSVカラーをRGBカラーに変換する。

    Args:
        hsv_colors (list): HSV形式のカラーリスト

    Returns:
        list: RGB形式のカラーリスト
    """
    # numpy配列に変換
    hsv_colors = np.array(hsv_colors, dtype=np.uint8).reshape(-1, 1, 3)
    # HSVからRGBに変換
    rgb_colors = cv2.cvtColor(hsv_colors, cv2.COLOR_HSV2RGB)
    # 変換した結果をリストに変換して返す
    return rgb_colors.reshape(-1, 3).tolist()


def color_in_list(color, color_list):
    """
    色がリストに含まれているかをチェックする。

    Args:
        color (list): チェックする色（RGB形式）
        color_list (list): チェック対象の色リスト（RGB形式）

    Returns:
        bool: 色がリストに含まれているかどうか
    """
    return any(np.array_equal(color, c) for c in color_list)


def plot_colors(colors, ratios, color_space='RGB', title='Colors'):
    """
    色のプロットを表示する。

    Args:
        colors (list): 色のリスト（RGBまたはHSV形式）
        ratios (list): 色の割合リスト
        color_space (str): 色空間（'RGB' または 'HSV'）
        title (str): プロットのタイトル
    """
    # プロットの設定
    num_colors = len(colors)
    num_rows = 1
    if num_colors > 5:
        num_rows = 2
    plt.figure(figsize=(12, 2*num_rows))
    plt.axis('off')

    # Main colors plot
    for i, (color, ratio) in enumerate(zip(colors[:5], ratios[:5])):
        if color_space == 'HSV':
            color = cv2.cvtColor(np.uint8([[color]]), cv2.COLOR_HSV2RGB)[0][0]
        if num_rows == 2:
            plt.subplot(2, num_colors, i + 1)
        else:
            plt.subplot(1, num_colors, i + 1)
        plt.imshow([[np.array(color) / 255]])
        plt.title(f"{ratio:.2%}", fontsize=12)
        plt.axis('off')

    # Intermediate colors plot
    if num_rows == 2 and len(colors) > 5:
        for i, (color, ratio) in enumerate(zip(colors[5:], ratios[5:]), 1):
            plt.subplot(2, num_colors, i + 5)
            plt.imshow([[np.array(color) / 255]])
            plt.title(f"{ratio:.2%}", fontsize=12)
            plt.axis('off')

    plt.suptitle(title)
    plt.show()

  

# メインカラーと割合の抽出
main_colors_rgb, color_ratios = extract_main_colors(image_path, num_colors, min_distance)

# 中間色を生成
generated_colors = []
if len(main_colors_rgb) <= 5:
    generated_colors = neutral_color(main_colors_rgb)
    main_colors_rgb.extend(generated_colors)

# 割合を均等にする（単純に表示用）
if len(main_colors_rgb) > len(color_ratios):
    color_ratios.extend([1.0 / len(main_colors_rgb)] * (len(main_colors_rgb) - len(color_ratios)))

# # RGBからHSVに変換
main_colors_hsv = rgb_to_hsv(main_colors_rgb)

# メインカラーと割合の抽出
main_colors_rgb, color_ratios = extract_main_colors(image_path, num_colors, min_distance)

# 生成された中間色の表示
generated_colors = neutral_color(main_colors_rgb)

# # メインカラーの表示（RGB）
print("RGB Colors:")
plot_colors(main_colors_rgb, color_ratios, color_space='RGB', title='Main Colors (RGB)')

# メインカラーの表示（HSV）
print("HSV Colors:")
plot_colors(main_colors_hsv, color_ratios, color_space='HSV', title='Main Colors (HSV)')

# 分離された中間色とメインカラー
main_colors_rgb_final = main_colors_rgb[:num_colors]
color_ratios_final = color_ratios[:num_colors]
if generated_colors:
    generated_color_ratios = [1.0 / len(generated_colors)] * len(generated_colors)
    print("Generated Neutral Colors (RGB):")
    plot_colors(generated_colors, generated_color_ratios, color_space='RGB', title='Generated Neutral Colors (RGB)')

# メインカラーと割合の出力（RGB）
print("Main Colors in RGB and their Ratios:")
for i, (color, ratio) in enumerate(zip(main_colors_rgb_final, color_ratios_final), 1):
    print(f"Main Color {i} (RGB): {color}, Ratio: {ratio:.2%}")

# メインカラーと割合の出力（HSV）
main_colors_hsv = rgb_to_hsv(main_colors_rgb_final)
print("Main Colors in HSV and their Ratios:")
for i, (color, ratio) in enumerate(zip(main_colors_hsv, color_ratios_final), 1):
    print(f"Main Color {i} (HSV): {color}, Ratio: {ratio:.2%}")