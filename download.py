import cv2
import urllib.request
import numpy as np
import time
def make_image(image_url,numbering):
    print(str(i)+" dowloading...")
    # URLの画像情報をロード
    resp = urllib.request.urlopen(image_url)

    # OpenCVで読み込めるよう画像のメモリバッファ再構築
    image = np.asarray(bytearray(resp.read()), dtype=np.uint8)

    # メモリバッファより画像読み込み
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    # 新たな画像として書き出す
    first_number = 0 #連番一つ目のファイルの番号
    cv2.imwrite("aragaki"+str(numbering+first_number)+".jpg", image)

url_list = ['https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRfNkamOjU0aVQYltk8C_PpTpJ7tcUCDUgirszrLK2bqGy_ci7K',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTbWcCfpDBcIbAYuOdsPJEnPWB2BVux0BGbuqIaTCCgbsjbiH-APg',
            'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTQkPUzqyBMqKC3oMAM-XTVLxNbPr8225G6nMZcJ5GscpwsYZ3a',
            'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRA43QNta5wQZRKLgM0tYL1T168pPEFTBFOvxOJdeeV2SsMog1MbA',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdagOp2xWc2FuDCWhPJW5BZhlJe3qE2vkPKMMbDUXVGD9gpkUV3Q',
            'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTfVGSy80SKmW6cggRjSZvF5Zp4OHLuva91et9v0D8CiNscBvNKUA',
            'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSXGo-WW1u8TxBPTpnX7PMnq_V_4gE5z40IhSEC-B9gKPyX0HPP',
            'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTn9nJxTKymr6nX8XUb8gBomSoUC67iBWfaZxbnoeGKoH_AwPnX1g',
            'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQW10AVl9AHve5c8ussXUQBP-JJ0t94ypq3m2i0S7ERHifn5N04',
            'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTf7z2iFoP_YanTJrTIBmf2HfXVT-R2cJH2BEFyhkyePWpNOo4',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRpVOLR5gEffU1Tcl-a5y2lfuHFHke79xXb_kKPRbHniqCvyCMtZA',
            'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcR6FTQ58-1qONhfxKk0_uA6LL-M2VTNtL6AISHCPEj1Ed0VqHd_',
            'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRRnzPDRqkcG-eHoY52CezDGaR6ZbxCr30KMzo2YdVBNwB4s3ET',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRWToyt06GGJv7LfayJ3S437tC4sfbkXxghDPUq6OaHt_1SDjF8Ow',
            'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRKuRlALqVsr3n2Cxci7ttD3h92xTn90Ui4HFy4-DOoEmrVpUWe',
            'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTVHc63zV_zi-XW_vLWjv30szeVklu2k21-DxVhetNJmvDejDWH7g',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRJGIEYED-Py1Bq5BnxGY70YAH99W0ybP4ORpbGp_Il2BO7yKMKqw',
            'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRe82ilW73GcVUDTTx0NyVVNDm6TExM0ZfyLnezxqioTyYd2PfciA',
            'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSmqKDL84R4l6ZpF799qR8-SrTGNaTQNmJVvf7_uwD4BmckASSF',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQPQvLHxRyOeeeEGiiZW1ZTYLskGu8tAnRp5sCzddP_GByDjvOs-A',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRNicQTjrfkojku5YUK29P5tGNlRLgfcma3CkSQCIfAi0T0JBlZ',
            'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcSn4ABbxgyOpYSwA4rHYHSxuK64gUxH2KKDh0kH3-CdJW42Dvf4',
            'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTOQw_uLZxQQUjzldTHbRauX2Z7IMhIadCSNYGejGTyT6jiwsbWGA',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTUMF4jtCxoEs-RfK8McF7DL4k8ni08M7Oaa4lO9TmYPjoFcXhx',
            'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTKW1_cp_x4morjHi9nyn37ucob5cV8wojBV-om1c1iTJ3uV-Ya',
            'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTCdOh4d3o94-MG1UhrdIyrm85Cj4dYdP9TEaeL4vbCQy05J0WZ',
            'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcSjJzv_wN_SVUVeQlm8YCh8d3RNmtC5WWML6YsP3-ynr7ByZSYb',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSp2xs9DWi11yG8fpqH3CrzKHTKRDZnUGRP2tt4IyV677ImxXMoyw',
            'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRKH4RXYSlRdqv4Nl8pbRtHqVUNlWjEoMvWZe7sF3Od4bJsbouS',
            'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTxXYoN6nW7rqb60VfKIwRO-aQJUM52gyL_HUBGipJ_KeNmYZKA',
            'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcS7Fti4EM3Eoe3pcMlMeKwdja4qSBY6QCL6wcBjAN9UhzDgcZLD',
            'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRAfaptMNqcW3YjN5rAtLknXi8MW2cLkkpD-xdsBoCTjVXX5qQW',
            'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRmT9pVMVVtgBD86-tkuKbL63lrGUrGO60xHW2T_F6sLVQXRjBM',
            'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRIcljY8ps31uy8lB0n9QkNZN_gAarI74xXo3m16XOWtn4MSPcC',
            'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcSdIQdrTIlzCOZtVH6rgKc6lj6RZo6znKp01r8trjgaZUp97rPauSeNV8o',
            'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQKL3d5x130vWyDnC28V3uzvtL4QcecE7FrkDEDQtkBHDFcMKhD',
            'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRve2ATmVFRFmtFbf0RAb-OjlzJ9xrJHmki-LeAxniUWca4gtmbQQ',
            'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcS9CKIOnRBai5QQoMo9_MHlqKDHCf7I8-i6bqpVGS-3qlqG-1ft2g',
            'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcR2c16i2S_cCgJCL4VpFNn8DjwgHRtLG5HDmmVRwB-F8tZKu75oDQ',
            'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRCgsb3LdnbTGCIRrK4y0GI6Af-4G5rPGmRLbgsqA9M6bd0WYEw',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSGbH1LSsiWrPiBZc_5HCAO3Uyr2b9vjTHYRNEJ9_6140kUkvVB',
            'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRUn5ReAOaAsXnPbgACvaZ4a39MxoPt8HHKyhOYNse3dNgp4Mj-rA',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSJDO_J55h3zE-kOqs0h6bE_xzdB6mstDqi0hgLLVDDj6G6SBRGSQ',
            'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcR88RvcwnHViCXChZxduKTEX5qgot9jOKb6IKgfi0DbfUReAIuj',
            'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTntAGcQkHJZGCwwUDIJauUoraHQjsepjpRiCalsrpTDOkrGX0ZUw',
            'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQ4F4w4STHK_XGEWct8HD1aMYjkxdQOrVJ4k1Qb6knQS7caGStRig',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRT4cPrcfNapeZKaG_ClX4ahkdU6q6Y8Dv8fOm327xJGZAUfdpf',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTIg5f1RXOc0yRt1BZv9pWDHWNZeiTZMHayl2Bg9Nthzr5R1ikc',
            'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQEeyRq_wy5TeuBS0M5Y_jQpVs3EvkcRPXxYnZ1K93sAsl2FpkGKg',
            'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRDw2_Nt8MTt2X7mX0xdFk_oG8jkawDGvTM527CfaKB48yZ26GO',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQRwo_w8adwORR_P1UXHkU98P6t8vkP_yzJObOaX3Aw0f2x8MgkEg',
            'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRMYHSmRQxev0Pmq5nHTD9e_vyKFKZtU4pEkHJo6MIw22lvVPL6',
            'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTlrLfQIsBzySQ76hdRo8LLZWCnf5ibO9TIa5Ib_zqFFlN1LY8X',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTg_99oNGAB37kkgHtNwzaG1H7VyI07vE4jpVfk_e-g3mg21vwTAA',
            'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcT9eSrX80JXLQu7XPgSYpu-sk8Bd8ILV2uV55SPK5ySVP0U__KZaw',
            'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTKgoqk-XdasM3VpZvLvtC3wlbfu7mnYUx65R-r243iEUmxakLMxw',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcToPALg_fYF8hGM4CV350mkV0c2qRwRolswYHWsBmQj6eIUUCZMxg',
            'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcT8EvnkgBwK1TvF8Cp34iXBfCbswa9R5P6pVefWNDAKHHNtCRHF',
            'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSvJq_P6BRXm2-oue9nIASGBuWqd8X4HbR-OO4q0YeY7WaF-2NWgQ',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS-v4NWlJzyFJIeu5VHyjVjFp1-54xzVsmF44e4hDIIaxjKPqGe',
            'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSIkboMmsVOJXcNV2ok1OcY6tbe9SjBWXUiAZjw6aHF8Fy1Ocpl8w',
            'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcSzcJNbPxZ9iE3PyoMm_7h-ODiw8lUSdOKwDU8x-dElv_CwmAzG',
            'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcSF_eO_80uGnLiXDtn_sjy9elkVKkhoP7pvXyLByih9ajgyl467zw',
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTFFG1RudTbhA7r1gWRYRa_kkHGbkl6q0tUrm2cxMpJkPoVyCdNlA',
            'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTMn9ZBHEZ1Ror7WgYOnzFEp_Onyl4CrEBuGzJDReE0r3pJ38YDeA']
for i in range(0,len(url_list)):
    make_image(url_list[i],i)
    time.sleep(2)
