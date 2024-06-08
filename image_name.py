import os


def batch_rename_images(folder_path, new_name_pattern):
    """
    批量重命名图片文件。

    :param folder_path: 图片文件所在文件夹路径
    :param new_name_pattern: 新的文件名模式，例如 "image_{}.jpg"
    """
    # 获取文件夹中的所有文件
    files = os.listdir(folder_path)
    # 仅保留图片文件（可以根据需要扩展）
    image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    for index, filename in enumerate(image_files):
        # 构建新的文件名
        new_name = new_name_pattern.format(index + 1)
        # 获取文件的完整路径
        src = os.path.join(folder_path, filename)
        dst = os.path.join(folder_path, new_name)
        # 重命名文件
        os.rename(src, dst)
        print(f'Renamed {src} to {dst}')


# 使用示例
folder_path = r'E:\dataset\mydata\用于gan的布匹数据\原图'  # 替换为你的图片文件夹路径
new_name_pattern = 'image_{}.jpg'  # 替换为你想要的文件名模式

batch_rename_images(folder_path, new_name_pattern)
