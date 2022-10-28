from posixpath import abspath
import cv2
from pyzbar.pyzbar import decode, ZBarSymbol
import pyqrcode
import os
#----------------{\n}(改行)は基本的にinputは先頭に。
#-------------------------
def main():
    while True:
        try:
            print("\n If you quit right now,Please press [Contrl + C] at the same time!")
            print("qr make or read?\n")
            choose = str(input("enter make(m) or read(r) >>"))

            if "r" in choose:
                ##----------読み取りの時----------##
                # -----------------------------------------------------------
                # initial
                # -----------------------------------------------------------
                font = cv2.FONT_HERSHEY_SIMPLEX
                url = str(input("\n絶対パス>>"))
                new_url = url.strip('""')
                print(new_url)
                """"""
                url_abstract = os.path.relpath(new_url)
                FILE_PNG_AB = url_abstract
                
                #絶対パスを入力後、相対パスに移動
                #絶対パスから相対パスへ変換
                # -----------------------------------------------------------
                # function_qr_dec
                # -----------------------------------------------------------
                def function_qrdec_pyzbar(img_bgr):

                    # QRコードデコード
                    value = decode(img_bgr, symbols=[ZBarSymbol.QRCODE])
                    #print(value)
                    if value:
                        for qrcode in value:

                            # QRコード座標取得
                            x, y, w, h = qrcode.rect

                            # QRコードデータ
                            dec_inf = qrcode.data.decode('utf-8')
                            print(f'\ndec:{dec_inf}')
                            img_bgr = cv2.putText(img_bgr, dec_inf, (x, y - 6), font, .3, (255, 0, 0), 1, cv2.LINE_AA)

                            # バウンディングボックス
                            cv2.rectangle(img_bgr, (x, y), (x + w, y + h), (0, 255, 0), 2)

                        #qcv2.imshow('image', img_bgr)
                        cv2.waitKey(0)

                # ----------------------------------------------------------
                # sample program
                # -----------------------------------------------------------
                img_BGR = cv2.imread(FILE_PNG_AB, cv2.IMREAD_COLOR)
                function_qrdec_pyzbar(img_BGR)
                finish_y_or_n = str(input('\nfinish y or n?>>'))
                if finish_y_or_n == "y":
                    print("\nThis is the end.")
                    break
            
            if "m" in choose:
                ##----------制作の時----------##
                url = str(input("\nenter url>>"))
                b = pyqrcode.QRCode(url,error='M')

                name = str(input("\nfile name>>"))
                while True:
                    print("\nPlease select an extension!")
                    choose_extension = str(input("\npng or jpg or gif>>"))
                    if choose_extension == "png":
                        file_name = name+'.'+choose_extension
                        print(f"\nSaved it as {file_name}.\n")
                        #abspath = str(input("保存先(仮)>>"))
                        #cv2.imwrite(abspath,file_name)
                        b.png(file_name,scale=6)
                        break

                    if choose_extension == "jpg":
                        file_name = name+'.'+choose_extension
                        print(f"\nSaved it as {file_name}.\n")
                        b.png(file_name,scale=6)
                        break

                    if choose_extension == "gif":
                        file_name = name+'.'+choose_extension
                        print(f"\nSaved it as {file_name}.\n")
                        b.png(file_name,scale=6)
                        break
                    else:
                        print("Please one more!")
                
                finish_y_or_n = str(input('finish y or n?>>'))
                if finish_y_or_n == "y":
                    print("\nThis is the end.")
                    break        

            else:
                print("Please type it again!\n")
        
        except TypeError:
            print("入力された文字が違います")
            print("もう一度やり直してください")
            main()

if __name__ == "__main__":
    main()