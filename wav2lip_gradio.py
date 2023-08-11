import gradio as gr
import os
import subprocess

def process_video(audio_file, video_file, output_file):
    # Run the wav2lip inference command
    command = f'python inference.py --checkpoint_path checkpoints/wav2lip_gan.pth --face {video_file} --audio {audio_file} --outfile {output_file}'
    subprocess.run(command, shell=True)

def baseNameofPath(srcP:str):
    baseP = os.path.basename(srcP)
    return os.path.splitext(baseP)[0]

def setRstVidDir(audP, vidP, svDir=None):
    audName =baseNameofPath(audP)
    vidName =baseNameofPath(vidP)
    rstVidP = f"{vidName}_{audName}.mp4"
    if svDir is None:
        svDir = os.path.dirname(audName)
    rstVidP = os.path.join(svDir, rstVidP)
    return rstVidP

def wav2lip(audio, video,  svDir=None):
    # Save the uploaded files
    audio_file = os.path.abspath(audio)
    video_file = os.path.abspath(video)
    rstVidP = setRstVidDir(audio_file, video_file, svDir)
    # Run the wav2lip inference
    process_video(audio_file, video_file, rstVidP)
    # Return the output video as bytes
    return rstVidP

def pileProc(audioDir:str, videoDir:str, uiProgress=gr.Progress()):
    assert os.path.isdir(audioDir), f"{audioDir} doesn't exist!"
    assert os.path.isdir(videoDir), f"{videoDir} doesn't exist!"
    uiProgress(0, desc="Starting")
    audioList = [os.path.join(audioDir, x) for x in sorted(os.listdir(audioDir)) if os.path.isfile(os.path.join(audioDir, x))]
    videoList = [os.path.join(videoDir, x) for x in sorted(os.listdir(videoDir)) if os.path.isfile(os.path.join(videoDir, x))]
    tmpDir = os.path.dirname(audioDir)

    vidName =baseNameofPath(videoDir)
    audName =baseNameofPath(audioDir)
    rstVidName = f"{vidName}_{audName}"
    rstVidDir = os.path.join(tmpDir, rstVidName)
    os.makedirs(rstVidDir, exist_ok=True)

    uiProgress(0, desc="Starting")
    for iaud, ivid in uiProgress.tqdm(zip(audioList, videoList)):
        wav2lip(iaud, ivid, rstVidDir)
    return rstVidDir



with gr.Blocks(title="wav2lip Inference") as iface:
    gr.Markdown("Upload an audio and video file to generate a lip-synced video.")


    with gr.Tab("改嘴型"):
        with gr.Row():
            with gr.Column():
                gr.Markdown("## 输入:")
                audio_input=gr.Audio(label="输入音频(.mp3)", type="filepath", format="mp3")
                video_input=gr.Video(label="输入视频(.mp4)", type="filepath", format="mp4")
            with gr.Column():
                gr.Markdown("## 输出:")
                video_output=gr.Video(label="输出视频(.mp4)", format="mp4")
        gen_button1= gr.Button("开始转化")
    with gr.Tab("批处理"):
        with gr.Row():
            with gr.Column():
                gr.Markdown("## 输入:")
                audio_input_dir= gr.Textbox(label="audio directory", info="包含原始音频的文件夹路径")
                video_input_dir= gr.Textbox(label="video directory", info="包含原始视频的文件夹路径")
            with gr.Column():
                gr.Markdown("## 输出:")
                video_output_dir= gr.Textbox(label="result video directory", info="包含结果视频的文件夹路径")
        gen_button2= gr.Button("开始转化")






    gen_button1.click(wav2lip, inputs=[audio_input, video_input], outputs=video_output, api_name="voice2video")
    gen_button2.click(pileProc, inputs=[audio_input_dir, video_input_dir], outputs=video_output_dir)

iface.queue(concurrency_count=2)
iface.launch(show_api=False, show_error=True, debug = False, share = True)