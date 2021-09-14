import os
import sys
import glob
import cv2
import cv_video_slide as cvs

playlist_file = 'playlist.txt'
video_dir_name = 'video'

def loopPlay():
    # 動画切り替え時にPC画面が見えないように目隠し用のウィンドウを表示しておく
    cv2.namedWindow("Backwall", cv2.WINDOW_NORMAL)
    cv2.setWindowProperty("Backwall", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    while True:
        # プレイリストファイルを開く
        try:
            play_list_txt = open(playlist_file, 'r', encoding='UTF-8')
        except:
            print('ERROR: Could NOT Open playlist file.')
            return 0

        # プレイリストファイルを読み込む
        try:
            play_list = play_list_txt.readlines()
        except:
            print('ERROR: Could NOT Read playlist file.')
            return 0
        play_list_txt.close()

        # 動画の入っているディレクトリパスを取得する
        video_dir_path = os.path.join(os.getcwd(), video_dir_name)

        # プレイリストファイルに従って動画再生リストを生成する
        video_list = []
        for line in play_list:
            file_name = line.rstrip('\r\n')
            if len(file_name) < 1:
                continue
            else:
                file_path = os.path.join(video_dir_path, file_name)
                video_list.append(file_path)
            
        cvs.play_videos(video_list)
    
    cv2.destroyAllWindows()

    return 0

if __name__ == '__main__':
    loopPlay()