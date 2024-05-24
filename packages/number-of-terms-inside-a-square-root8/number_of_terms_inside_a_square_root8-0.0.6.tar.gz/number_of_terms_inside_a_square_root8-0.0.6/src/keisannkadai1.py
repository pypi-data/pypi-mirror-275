import math

def calculate_number_of_terms(number):
    """
    指定された数値の平方根の小数部分を含めて返します。
    """
    square_root = math.sqrt(number)
    integer_part = int(square_root)
    decimal_part = square_root - integer_part
    return integer_part, decimal_part

def main():
    print("√を外して中の数が何条になるかを計算します。")
    number = float(input("数値を入力してください: "))
    
    # √を外して中の数が何条になるかを計算する
    integer_part, decimal_part = calculate_number_of_terms(number)
    
    # 小数点以下の桁数を表示する
    decimal_places = len(str(decimal_part)) - 2
    
    print(f"√{number} を外して中の数は {integer_part}+{decimal_part:.{decimal_places}f} になります。")

if __name__ == "__main__":
    main()
