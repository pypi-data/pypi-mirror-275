def convert_to_tokyo_domes_M2(area):
    # 東京ドームの面積（平方メートル）
    tokyo_dome_area_m2 = 46755
    # サッカーコートの面積（平方メートル）
    soccer_field_area_m2 = 7140
    # 入力された面積を東京ドーム何個分かに変換
    num_tokyo_domes = area / tokyo_dome_area_m2
    # 入力された面積をサッカーコート何個分かに変換
    num_soccer_fields = area / soccer_field_area_m2
    
    return num_tokyo_domes, num_soccer_fields

def convert_to_tokyo_domes_ha(area):
    # 東京ドームの面積（ha）
    tokyo_dome_area_ha = 4.6
    # サッカーコートの面積（ha）
    soccer_field_area_ha = 0.714
    # 入力された面積を東京ドーム何個分かに変換
    num_tokyo_domes = area / tokyo_dome_area_ha
    # 入力された面積をサッカーコート何個分かに変換
    num_soccer_fields = area / soccer_field_area_ha
    
    return num_tokyo_domes, num_soccer_fields

# 面積の単位を選ぶ
input_area = input("M2 or ha ？: ")

# 面積を計算

if input_area == "M2":
    input_area_M2 = float(input("面積を入力してください（平方メートル）: "))
    result = convert_to_tokyo_domes_M2(input_area_M2)
elif input_area == "ha":
    input_area_ha = float(input("面積を入力してください（ヘクタール）: "))
    result = convert_to_tokyo_domes_ha(input_area_ha)


# 変換結果を表示
# result = convert_to_tokyo_domes(input_area)
print(f"入力された面積は東京ドーム {result[0]:.2f} 個分です。")
print(f"入力された面積はサッカーコート {result[1]:.2f} 個分です。")

def main():
    pass

if __name__ == "__main__":
    main()


