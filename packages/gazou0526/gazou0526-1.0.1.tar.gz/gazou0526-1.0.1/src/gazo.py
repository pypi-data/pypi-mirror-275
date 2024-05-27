from PIL import Image
import os

def resize_image(input_path, output_path, width, height):
    try:
        img = Image.open(input_path)
        resized_img = img.resize((width, height))
        resized_img.save(output_path)
        print("画像のリサイズが完了しました。")
    except Exception as e:
        print("エラーが発生しました:", e)

def convert_encoding(input_path, output_path, input_encoding, output_encoding):
    try:
        with open(input_path, 'r', encoding=input_encoding) as file:
            text = file.read()
        with open(output_path, 'w', encoding=output_encoding) as file:
            file.write(text)
        print("テキストファイルのエンコーディング変換が完了しました。")
    except Exception as e:
        print("エラーが発生しました:", e)

if __name__ == "__main__":
    # 画像のリサイズ
    input_image_path = input("画像ファイルのパスを入力してください: ")
    output_image_path = input("出力ファイル名を入力してください: ")
    width = int(input("リサイズ後の幅を入力してください: "))
    height = int(input("リサイズ後の高さを入力してください: "))
    resize_image(input_image_path, output_image_path, width, height)

    # テキストファイルのエンコーディング変換
    input_text_path = input("テキストファイルのパスを入力してください: ")
    output_text_path = "output_text_converted.txt"
    input_encoding = "utf-8"
    output_encoding = "shift-jis"
    convert_encoding(input_text_path, output_text_path, input_encoding, output_encoding)
