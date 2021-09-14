# 引数に渡したディレクトリに入っている動画ファイルを順々に再生するPythonコード
# 再生はファイル名順に行う
# OpenCVを使って再生し，GPU支援も受けられる
import cv2
import os
import sys
import glob

# 引数：動画ファイル(.mp4)が入っているディレクトリパス
def cv_video_player(video_dir):
    ext_filter = "*.mp4"
    video_list = sorted(glob.glob(os.path.join(video_dir, ext_filter)))
    play_videos(video_list)

    ext_filter = "*.m4v"
    video_list = sorted(glob.glob(os.path.join(video_dir, ext_filter)))
    play_videos(video_list)

    return 0

def play_videos(video_list):
    for video_path in video_list:
        cap = cv2.VideoCapture(video_path)
        if cap.isOpened()==False:
            print('Failed to open {0}'.format(video_path))

        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret == True:
                # Full Screenで表示するための処理
                cv2.namedWindow("Video", cv2.WINDOW_NORMAL)
                cv2.setWindowProperty("Video", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                cv2.imshow("Video", frame)
                if cv2.waitKey(25) & 0xFF == ord('q'): 
                    sys.exit()
            else:
                break

        cap.release()
        cv2.destroyWindow("Video")
#        cv2.destroyAllWindows()
    return 0

if __name__ == '__main__':
    args = sys.argv
    dir_path = args[1]
    cv_video_player(dir_path)