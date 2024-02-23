def get_video_folders(TEXT_FILE_PATH):
    f = open(TEXT_FILE_PATH, 'r')
    lines = f.readlines()
    video_folders = [line[:-1] if '\n' in line else line for line in lines]
    f.close()
    return video_folders


def get_video_numbers(TEXT_FILE_PATH):
    videos_number = sorted(list({folder_path.split('/')[-2] for folder_path in get_video_folders(TEXT_FILE_PATH)}))
    return videos_number

def get_clips(TEXT_FILE_PATH, video_number):
    clips = [clip for clip in get_video_folders(TEXT_FILE_PATH) if video_number in clip.split('/')[-2]]
    return clips


def get_clip_numbers(TEXT_FILE_PATH, video_number):
    clips_number = [clip_num.split('/')[-1].split('.')[0] for clip_num in get_clips(TEXT_FILE_PATH, video_number)]
    return clips_number


def check_index(selected_clip_info):
    if selected_clip_info[1]:
        index = ("SJ", "EY", "NK", "JY").index(selected_clip_info[1])
    else:
        index = None
    return index
