# Application to Determine the Number of Terms Inside a Square Root
任意の数字を入力することでその数字のルート内の項を求めることができる。
"You can determine the terms inside the square root of any given number by inputting the number."

使用方法 usage rules↓↓
```python
python3 keisannkadai1.py
```
## コード

以下のPythonコードを使用してください。
Use the Python code below.

#keisannkadai1.py↓↓
```python
import math

def calculate_number_of_terms(number):
    square_root = math.sqrt(number)
    integer_part = int(square_root)
    decimal_part = square_root - integer_part
    return integer_part, decimal_part

def main():
    print("√を外して中の数何条になるかを計算します。")
    number = float(input("数値を入力してください: "))
    # √を外して中の数何条になるかを計算する
    integer_part, decimal_part = calculate_number_of_terms(number)
    # 小数点以下の桁数を表示する
    decimal_places = len(str(decimal_part)) - 2
    print(f"√{number} を外して中の数は {integer_part}+{decimal_part:.{decimal_places}f} になります。")

if __name__ == "__main__":
    main()

