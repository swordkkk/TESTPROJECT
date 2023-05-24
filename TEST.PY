import os
import tkinter
import tkinter.messagebox

print("請輸入起始日期")
STARTDAY=str(input())
print("請輸入結束日期")
ENDDAY=str(input())


folders = ['01', '02','03', '04','05', '06','07']
subfolders = {'01': [STARTDAY+'-'+ENDDAY+'表1-1'], '02': [STARTDAY+'-'+ENDDAY+'表1-2'], '03': [STARTDAY+'-'+ENDDAY+'表1-3'], '04': [STARTDAY+'-'+ENDDAY+'表1-4'], '05': [STARTDAY+'-'+ENDDAY+'表1-5']}

for folder in folders:
    try:
        os.mkdir(folder)
        print(f'建立 {folder} 資料夾成功')
    except FileExistsError:
        print(f'{folder} 資料夾已存在')
        
    if folder in subfolders:
        for subfolder in subfolders[folder]:
            subfolder_path = os.path.join(folder, subfolder)
            try:
                os.mkdir(subfolder_path)
                print(f'建立 {subfolder_path} 資料夾成功')
            except FileExistsError:
                print(f'{subfolder_path} 資料夾已存在')
