import cv2
import os
# 左边视频遮罩
def VideoCroppingLeft(input_video_path, out_video_path):
    # if not os.path.exists(input_video_path):
    #     print('输入的视频文件不存在')
    video_read_cap = cv2.VideoCapture(input_video_path)
    input_video_width = int(video_read_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    input_video_height = int(video_read_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # input_video_fps = 30
    input_video_fps = int(video_read_cap.get(cv2.CAP_PROP_FPS))
    input_video_fourcc = int(cv2.VideoWriter_fourcc('M', 'P', '4', 'V'))
    out_video_width = int(input_video_width/2)
    out_video_height = input_video_height
    out_video_size = (int(out_video_width), int(out_video_height))
    video_write_cap = cv2.VideoWriter(out_video_path, input_video_fourcc, input_video_fps, out_video_size)
    while video_read_cap.isOpened():
        result, frame = video_read_cap.read()
        if not result:
            break
        # 设置裁剪范围  参数1 是高度的范围，参数2是宽度的范围
        # 左边部分
        target = frame[0:int(input_video_height), 0:int(out_video_width)]
        # 右边部分
        # target = frame[0:int(input_video_height), int(out_video_width):int(input_video_width)]
        video_write_cap.write(target)
        # cv2.imshow('target', target)
        cv2.waitKey(10)
    video_read_cap.release()
    video_write_cap.release()
    cv2.destroyAllWindows()

# 右边视频遮罩
def VideoCroppingRight(input_video_path, out_video_path):
    # if not os.path.exists(input_video_path):
    #     print('输入的视频文件不存在')
    video_read_cap = cv2.VideoCapture(input_video_path)
    input_video_width = int(video_read_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    input_video_height = int(video_read_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # input_video_fps = 30
    input_video_fps = int(video_read_cap.get(cv2.CAP_PROP_FPS))
    input_video_fourcc = int(cv2.VideoWriter_fourcc('M', 'P', '4', 'V'))
    out_video_width = int(input_video_width/2)
    out_video_height = input_video_height
    out_video_size = (int(out_video_width), int(out_video_height))
    video_write_cap = cv2.VideoWriter(out_video_path, input_video_fourcc, input_video_fps, out_video_size)
    while video_read_cap.isOpened():
        result, frame = video_read_cap.read()
        if not result:
            break
        # 设置裁剪范围  参数1 是高度的范围，参数2是宽度的范围
        # 左边部分
        # target = frame[0:int(input_video_height), 0:int(out_video_width)]
        # 右边部分
        target = frame[0:int(input_video_height), int(out_video_width):int(input_video_width)]
        video_write_cap.write(target)
        # cv2.imshow('target', target)
        cv2.waitKey(10)

    video_read_cap.release()
    video_write_cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
   VideoCroppingLeft('/content/Double_Talker/temp_video/1.mp4', '/content/Double_Talker/input_video/1L.mp4')
   VideoCroppingRight('/content/Double_Talker/temp_video/1.mp4', '/content/Double_Talker/ls_video/1R.mp4')
   VideoCroppingLeft('/content/Double_Talker/temp_video/2.mp4', '/content/Double_Talker/ls_video/2L.mp4')
   VideoCroppingRight('/content/Double_Talker/temp_video/2.mp4', '/content/Double_Talker/input_video/2R.mp4')
   VideoCroppingLeft('/content/Double_Talker/temp_video/3.mp4', '/content/Double_Talker/input_video/3L.mp4')
   VideoCroppingRight('/content/Double_Talker/temp_video/3.mp4', '/content/Double_Talker/ls_video/3R.mp4')
   VideoCroppingLeft('/content/Double_Talker/temp_video/4.mp4', '/content/Double_Talker/ls_video/4L.mp4')
   VideoCroppingRight('/content/Double_Talker/temp_video/4.mp4', '/content/Double_Talker/input_video/4R.mp4')
   VideoCroppingLeft('/content/Double_Talker/temp_video/5.mp4', '/content/Double_Talker/input_video/5L.mp4')
   VideoCroppingRight('/content/Double_Talker/temp_video/5.mp4', '/content/Double_Talker/ls_video/5R.mp4')
   VideoCroppingLeft('/content/Double_Talker/temp_video/6.mp4', '/content/Double_Talker/ls_video/6L.mp4')
   VideoCroppingRight('/content/Double_Talker/temp_video/6.mp4', '/content/Double_Talker/input_video/6R.mp4')
   VideoCroppingLeft('/content/Double_Talker/temp_video/7.mp4', '/content/Double_Talker/input_video/7L.mp4')
   VideoCroppingRight('/content/Double_Talker/temp_video/7.mp4', '/content/Double_Talker/ls_video/7R.mp4')
   VideoCroppingLeft('/content/Double_Talker/temp_video/8.mp4', '/content/Double_Talker/ls_video/8L.mp4')
   VideoCroppingRight('/content/Double_Talker/temp_video/8.mp4', '/content/Double_Talker/input_video/8R.mp4')
   VideoCroppingLeft('/content/Double_Talker/temp_video/9.mp4', '/content/Double_Talker/input_video/9L.mp4')
   VideoCroppingRight('/content/Double_Talker/temp_video/9.mp4', '/content/Double_Talker/ls_video/9R.mp4')
   VideoCroppingLeft('/content/Double_Talker/temp_video/10.mp4', '/content/Double_Talker/ls_video/10L.mp4')
   VideoCroppingRight('/content/Double_Talker/temp_video/10.mp4', '/content/Double_Talker/input_video/10R.mp4')