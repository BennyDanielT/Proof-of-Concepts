from moviepy.editor import VideoFileClip

clip=VideoFileClip("PATH_TO_VIDEO")
clip.write_gif("GIF_TITLE",fps=10) #Frames Per Second