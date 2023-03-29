import os

from cv2 import VideoCapture

# pyinstaller -F -c -i time.png video_time.py
# from moviepy.video.io.VideoFileClip import VideoFileClip

# 常见视频种类
video_type = ["avi", "wmv", "mpeg", "mp4", "m4v", "mov", "flv", "rmvb"]
# 视频绝对路径列表
video_path_list = []
# 视频相对路径列表
relative_path_list = []
# 获取视频所在路径列表
# son_path_list = []
# 视频时长列表
time_list = []


# 读取目标路径
def folder_path():
    folder = input("请输入目标路径：")
    return folder


# 获取视频绝对路径列表
def get_file_path(folder, video_path_list, video_type):
    """
    遍历文件夹中的文件，将符合要求的视频文件路径添加到视频路径列表中

    :param folder: 待遍历的文件夹路径
    :param video_path_list: 用于存储视频文件路径的列表
    :param video_type: 限制文件类型的列表
    :return:
    """
    for path, dirs, filename in os.walk(folder):
        for file in filename:
            if file.split(".")[-1] in video_type:
                video_path_list.append(path + "\\" + file)


# 获取视频相对路径列表
def get_relative_path(video_path_list, folder_name, relative_path_list):
    """
    给定视频路径列表，目标文件夹名称，以及相对路径列表，计算出每个视频文件相对于目标文件夹的路径并添加到相对路径列表中
    :param video_path_list: [包含一系列视频文件路径的列表]
    :param folder_name: [目标文件夹名称]
    :param relative_path_list: [用于存储每个视频文件相对于目标文件夹的路径的列表]
    :return:
    """
    delete_num = len(folder_name)
    for i in video_path_list:
        relative_path_list.append(i[delete_num + 1:])


# 获取视频所在路径列表
def son_path(video_path_list, son_path_list):
    """
    此函数获取两个列表，video_path_list和 son_path_list，并返回video_path_list中每个文件路径的所有子目录列表。
    :param video_path_list: 文件路径的列表。
    :param son_path_list: 一个空列表，将包含每个文件路径的子目录。
    :return: video_path_list中每个文件路径所有子目录列表。
    """
    for path in video_path_list:
        fragment = path.split("\\")[:-1]
        division = ""
        for cl in fragment:
            division = division + cl + "\\"
        son_path_list.append(division)


# 使用opencv通过路径获取单个视频时长
def testing(file):
    """
    计算给定视频文件的播放时长
    :param file: 视频文件的路径
    :return: 视频的播放时长，单位为分钟
    """
    cap = VideoCapture(file)
    if cap.isOpened():
        rate = cap.get(5)
        FrameNumber = cap.get(7)
        duration = round(FrameNumber / rate / 60, 3)
        return duration


# 使用moviepy通过路径获取单个视频时长
# def get_duration(filepath):
#     """
#     获取视频文件的时长（单位：分钟）
#     :param filepath: 视频文件的路径
#     :return: 视频文件的时长（单位：分钟）
#     """
#     video = VideoFileClip(filepath)
#     duration = video.duration / 60
#     video.close()
#     return duration


# 获取视频时长列表以及总时间
def add_time(video_path_list, time_list):
    """
    该函数计算所有视频的时间总和，并将其精确到三位小数。最后，函数将 whole_time 精确到三位小数并将其作为函数的输出返回
    :param video_path_list: 视频路径列表，里面是一个视频的完整路径
    :param time_list: 视频时长列表，用于往里面存放读取到的视频时长，
    :return: 返回一个精确到三位小数的视频总时长
    """
    whole_time = 0.0
    init_time_list = []
    for path_name in video_path_list:
        init_time_list.append(testing(path_name))
        # init_time_list.append(get_duration(path_name))
    for time in init_time_list:
        if isinstance(time, float):
            time = round(time, 2)
            time_list.append(time)
            whole_time = whole_time + time
    whole_time = round(whole_time, 3)
    return whole_time


# 输出视频信息
def print_information(whole_time, time_list):
    """
    作用是将包含视频的时间和数量信息的字符串打印到标准输出，并且返回该字符串。
    :param whole_time: 表示视频列表所有元素的加和，即视频的总播放时长
    :param time_list: 表示包含所有视频时间的列表
    :return: 视频长度信息，以及视频数量的文本内容
    """
    n_videos = len(time_list)  # 视频数量
    max_time = max(time_list)  # 最长时间
    min_time = min(time_list)  # 最短时间
    total_time_minutes = whole_time  # 总时长（单位：分钟）
    total_time_hours = round(whole_time / 60, 2)  # 总时长（单位：小时，保留两位小数）

    information = f"最长时长：{max_time}分钟\n" \
                  f"最短时长：{min_time}分钟\n" \
                  f"视频数量：{n_videos}个\n" \
                  f"总时长：{total_time_minutes}分钟\n" \
                  f"总时长：{total_time_hours}小时\n\n\n"
    print(information)  # 打印信息
    return information


# 导出视频信息文件
def export_txt(folder, dict, information):
    """
    将视频文件的标题、时长等信息写入指定文件夹下的 txt 文件中
    :param folder: 目标文件夹的路径
    :param dict: 包含视频文件名称及其对应时长的字典
    :param information: 要写入文件开头的信息
    :return: None
    """
    export_path = folder + "\\video_time.txt"
    with open(export_path, "w") as f:
        f.write(information)
        f.write("  ------------------------------------------------------------------\n")
        for k, v in dict.items():
            # 将非法字符替换为空格
            name = k.replace(u'\xa0', u'')
            time = pad_string(str(v))
            # 将视频名称和时间写入文件，并使用 f-string 使字符串更加清晰易读
            string = f"    time:{time}    {name}\n"
            # 根据输入的字符串计算得到分割线长度
            parting_line = generate_separator(string)
            f.write(f"{string}  --------------{parting_line}\n")


# 当长度不足10时，在字符串后面增加空格到长度达到10位
def pad_string(input_str):
    """
    将输入字符串后面添加空格，直至输入字符串长度为 7
    :param input_str: 输入字符串
    :return: 添加空格后的字符串，长度为 7
    """
    length = len(input_str)
    if length < 7:
        spaces = " " * (7 - length)
        input_str += spaces
    return input_str


def generate_separator(string):
    """
    根据输入字符串返回一个和输入字符串等长的分隔线字符串
    :param string: 输入字符串
    :return: 和输入字符串等长的分隔线字符串
    """
    length = len(string)
    separator = "-" * length
    return separator


# 单层目录视频时长获取
def one_time_or_path(folder):
    """
    获取folder文件下面所有视频文件，读取时长，并在该目录下创建一个文本文件用于保存时长。\n
    适合用于单层目录
    :param folder: 获取视频时长的目标文件夹
    :return:
    """
    video_path_list = []
    relative_path_list = []
    time_list = []
    # 获取 folder 文件夹下所有指定类型的视频文件，并将它们的绝对路径存入 video_path_list 列表中
    get_file_path(folder, video_path_list, video_type)
    # 将 video_path_list 中各视频文件的绝对路径转换为相对
    get_relative_path(video_path_list, folder, relative_path_list)
    # 计算 video_path_list 中各视频文件的总时长，并将每个视频文件的时长存入 time_list 列表中
    whole_time = add_time(video_path_list, time_list)
    # 输出视频信息
    information = print_information(whole_time, time_list)
    # # 将 relative_path_list 和 time_list 使用 zip 函数打包成一个字典，并将其赋值给 dicta 变量
    dicta = dict(zip(relative_path_list, time_list))
    # 将 dicta 和 information 作为参数，将这些信息保存到指定文件夹下的一个txt文件中。
    export_txt(folder, dicta, information)

    return information


# 多层目录视频时长获取
def many_time_or_path(folder, son_path_list=None):
    if son_path_list is None:
        son_path_list = []
    get_file_path(folder, video_path_list, video_type)
    son_path_list.append(folder)
    son_path(video_path_list, son_path_list)
    son_path_list = list(set(son_path_list))
    for i in son_path_list:
        print(i)
        one_time_or_path(i)


# 程序入口
if __name__ == "__main__":
    folder = folder_path()
    # folder = "D:\Python爬虫全套课程"
    many_time_or_path(folder)
