from moviepy.editor import VideoFileClip,concatenate_videoclips

# 1.提取说好不哭mv中的音频存为mp3
video1 = VideoFileClip('周杰伦-说好不哭.mp4') # 括号中为待处理视频文件的路径
video1.audio.write_audiofile('周杰伦-说好不哭.mp3') # 将提取的音频保存为mp3文件

# 2.提取Lover mv中的音频存为mp3
video2 = VideoFileClip('Taylor Swift-Lover.mp4')
video2.audio.write_audiofile('Taylor Swift-Lover.mp3')

# 3.将说好不哭周董部分和阿信部分进行剪切。
    # subclip（）是按照括号中的时间，对视频进行截取
video1.subclip('00:00:10','00:02:03').write_videofile('说好不哭-周杰伦单唱.mp4')
video1.subclip('00:02:00','00:03:48').write_videofile('说好不哭-阿信单唱.mp4')

# 4.将说好不哭和lover合并到一个MV
video3 = concatenate_videoclips([video1, video2])
video3.write_videofile('说好不哭+Lover.mp4')