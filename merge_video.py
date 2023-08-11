import subprocess
def crop_Left_Right(left_video_path , right_video_path, output_video_path):
     # 使用FFmpeg库进行视频拼接
     cmd = f'ffmpeg -i {left_video_path} -i {right_video_path} -filter_complex "[0:v]pad=iw*2:ih[bg];[bg][1:v]overlay=w" {output_video_path}'

     # 运行FFmpeg命令
     subprocess.call(cmd, shell=True)
if __name__ == '__main__':
    crop_Left_Right('/content/Double_Talker/input_video_input_audio/1L_1.mp4', '/content/Double_Talker/ls_video/1R.mp4', '/content/Double_Talker/output/ouput_1.mp4')
    crop_Left_Right('/content/Double_Talker/ls_video/2L.mp4', '/content/Double_Talker/input_video_input_audio/2R_2.mp4', '/content/Double_Talker/output/ouput_2.mp4')
    crop_Left_Right('/content/Double_Talker/input_video_input_audio/3L_3.mp4', '/content/Double_Talker/ls_video/3R.mp4', '/content/Double_Talker/output/ouput_3.mp4')
    crop_Left_Right('/content/Double_Talker/ls_video/4L.mp4', '/content/Double_Talker/input_video_input_audio/4R_4.mp4', '/content/Double_Talker/output/ouput_4.mp4')
    crop_Left_Right('/content/Double_Talker/input_video_input_audio/5L_5.mp4', '/content/Double_Talker/ls_video/5R.mp4', '/content/Double_Talker/output/ouput_5.mp4')
    crop_Left_Right('/content/Double_Talker/ls_video/6L.mp4', '/content/Double_Talker/input_video_input_audio/6R_6.mp4', '/content/Double_Talker/output/ouput_6.mp4')
    crop_Left_Right('/content/Double_Talker/input_video_input_audio/7L_7.mp4', '/content/Double_Talker/7s_video/7R.mp4', '/content/Double_Talker/output/ouput_7.mp4')
    crop_Left_Right('/content/Double_Talker/ls_video/8L.mp4', '/content/Double_Talker/input_video_input_audio/8R_8.mp4', '/content/Double_Talker/output/ouput_8.mp4')
    crop_Left_Right('/content/Double_Talker/input_video_input_audio/9L_9.mp4', '/content/Double_Talker/ls_video/9R.mp4', '/content/Double_Talker/output/ouput_9.mp4')
    crop_Left_Right('/content/Double_Talker/ls_video/10L.mp4', '/content/Double_Talker/input_video_input_audio/10R_10.mp4', '/content/Double_Talker/output/ouput_10.mp4')