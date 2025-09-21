import os
import shutil

# 獲取腳本所在的目錄
script_directory = os.path.dirname(os.path.abspath(__file__))

# 定義 Downloads 資料夾的路徑
downloads_folder = os.path.join(script_directory, "Downloads")

# 如果 Downloads 資料夾不存在，則建立
if not os.path.exists(downloads_folder):
    os.makedirs(downloads_folder)

# 定義要建立的檔案名稱
files_to_create = [
    "Scripting課程大綱.pdf",
    "期中報告草稿.docx",
    "cat_meme.jpg",
    "lofi_music.mp3",
    "screenshot_2025.png",
    "final_project.zip"
]

# 在 Downloads 資料夾中建立檔案
for file_name in files_to_create:
    file_path = os.path.join(downloads_folder, file_name)
    # 如果檔案不存在，則建立空白檔案
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            pass

# 定義分類資料夾及其對應的副檔名
categories = {
    "Documents": [".pdf", ".docx", ".txt"],
    "Images": [".jpg", ".png", ".gif"],
    "Music": [".mp3", ".wav"],
    "Others": []  # 其他未分類的檔案
}

# 在 Downloads 資料夾內建立分類資料夾
for category in categories.keys():
    category_folder = os.path.join(downloads_folder, category)
    if not os.path.exists(category_folder):
        os.makedirs(category_folder)

# 將檔案移動到相應的分類資料夾
for file_name in files_to_create:
    file_path = os.path.join(downloads_folder, file_name)
    file_extension = os.path.splitext(file_name)[1].lower()  # 取得副檔名

    # 找到對應的分類資料夾
    destination_folder = None
    for category, extensions in categories.items():
        if file_extension in extensions:
            destination_folder = os.path.join(downloads_folder, category)
            break
    if destination_folder is None:
        # 如果沒有匹配的分類，移動到 Others 資料夾
        destination_folder = os.path.join(downloads_folder, "Others")

    # 移動檔案
    shutil.move(file_path, os.path.join(destination_folder, file_name))

print(f"檔案已分類並移動到 {downloads_folder} 中的相應資料夾。")
