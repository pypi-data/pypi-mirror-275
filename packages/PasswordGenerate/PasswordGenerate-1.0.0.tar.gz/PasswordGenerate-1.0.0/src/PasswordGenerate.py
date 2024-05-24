import random
import string

def generate_password(length=12, include_lower=True, include_upper=True, include_digits=True, include_symbols=True):
  """
  パスワードを生成する関数

  引数:
    length (int): パスワードの長さ (デフォルト: 12)
    include_lower (bool): 小文字を含めるかどうか (デフォルト: True)
    include_upper (bool): 大文字を含めるかどうか (デフォルト: True)
    include_digits (bool): 数字を含めるかどうか (デフォルト: True)
    include_symbols (bool): 記号を含めるかどうか (デフォルト: True)

  返り値:
    str: 生成されたパスワード
  """
  characters = []
  if include_lower:
    characters.extend(string.ascii_lowercase)
  if include_upper:
    characters.extend(string.ascii_uppercase)
  if include_digits:
    characters.extend(string.digits)
  if include_symbols:
    characters.extend(string.punctuation)

  password = ''.join(random.choice(characters) for _ in range(length))
  return password

def main():
  """
  メイン関数
  """
  length = int(input("パスワードの長さを入力してください: "))
  include_lower = input("小文字を含めますか？ (y/n): ") == "y"
  include_upper = input("大文字を含めますか？ (y/n): ") == "y"
  include_digits = input("数字を含めますか？ (y/n): ") == "y"
  include_symbols = input("記号を含めますか？ (y/n): ") == "y"

  password = generate_password(length, include_lower, include_upper, include_digits, include_symbols)
  print("生成されたパスワード:", password)

if __name__ == "__main__":
  main()