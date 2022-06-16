import os
import time
import threading
import tkinter
import tkinter.ttk as ttk
from tkinter import filedialog
from tkinter import messagebox
from pytube import YouTube
from pytube import Channel
from pytube import Playlist
from moviepy.editor import VideoFileClip
from moviepy.video.io.VideoFileClip import VideoFileClip


def clear():
    clear_materials = [ch_label,url_label,dlPath_label,url_box,dlPath_box,dlPath_shosan,jikkou_button,jikkou_ikkatu_button,vid_title_label,vid_des_label,tango_label,tango_box,jikkou_tango_button,hiduke_box,hiduke_label,hiduke_select,jikkou_hiduke_button,pl_label,jikkou_pl_button,currentDL,jikkou_bunkatu_button,bunkatu_label,bunkatu_mode,keisan_bunkatu_button,keisan_bunkatu_label,bunkatu_jikkou_label,gif_end_label,gif_kaisi_label,gif_end_select,gif_kaisi_select,gif_sakusei_button,gif_fps_label,fps_entry,renketu_file_label,renketu_file_entry]
    for material in clear_materials:
        material.place_forget()


def DLlabel_place():
    dlPath_label.place(x=10,y=40)
    dlPath_box.place(x=80,y=40)
    dlPath_shosan.place(x=425,y=40)
    url_box.place(x=80,y=70)
    

def submit():
    selected = mode_combobox.get()
    if selected.startswith("1"):
        clear()
        DLlabel_place()
        url_label.place(x=10,y=70)
        jikkou_button.place(x=425,y=70)
    elif selected.startswith("2"):
        clear()
        DLlabel_place()
        ch_label.place(x=10,y=70)
        jikkou_ikkatu_button.place(x=425,y=70)
    elif selected.startswith("3"):
        clear()
        DLlabel_place()
        ch_label.place(x=10,y=70)
        tango_label.place(x=10,y=100)
        tango_box.place(x=80,y=100)
        jikkou_tango_button.place(x=425,y=84)
    elif selected.startswith("4"):
        clear()
        DLlabel_place()
        ch_label.place(x=10,y=70)
        hiduke_label.place(x=10,y=100)
        hiduke_box.place(x=80,y=100)
        hiduke_select.place(x=330,y=100)
        jikkou_hiduke_button.place(x=425,y=84)
    elif selected.startswith("5"):
        clear()
        DLlabel_place()
        pl_label.place(x=10,y=70)
        jikkou_pl_button.place(x=425,y=70)
    elif selected.startswith("6"):
        clear()
        DLlabel_place()
        ch_label.place(x=10,y=70)
        bunkatu_label.place(x=225,y=100)
        bunkatu_mode.place(x=80,y=100)
        jikkou_bunkatu_button.place(x=425,y=160)
        bunkatu_mode.current(4)
        keisan_bunkatu_label.place(x=250,y=130)
        keisan_bunkatu_button.place(x=425,y=130)
        bunkatu_jikkou_label.place(x=250,y=160)
    elif selected.startswith("7"):
        clear()
        DLlabel_place()
        url_label.place(x=10,y=70)
        gif_kaisi_label.place(x=10,y=100)
        gif_kaisi_select.place(x=100,y=100)
        gif_end_label.place(x=200,y=100)
        gif_end_select.place(x=290,y=100)
        gif_kaisi_select.insert(tkinter.END,"00:00")
        gif_end_select.insert(tkinter.END,"00:00")
        gif_sakusei_button.place(x=425,y=130)
        gif_fps_label.place(x=400,y=100)
        fps_entry.place(x=430,y=100)
        fps_entry.current(3)
    else:
        baka = messagebox.askyesno("はい?w","エラーっすｗ\n普通の使い方してたらこのエラー出ないっすよww")
        if baka == True:
            pass
        elif baka == False:
            baka2 = messagebox.askretrycancel("は？","なに反抗しちゃってるのwwwwww")
            if baka2 == True:
                baka3 = messagebox.askretrycancel("おい粗大ゴミ","いい加減諦めたら？wwwwwwww")
                n = 0
                while baka3 == True:
                    if n < 20:
                        baka3 = messagebox.askretrycancel("おい粗大ゴミ","いい加減諦めたら？wwwwwwww")
                        n += 1
                    elif n == 20:
                        baka3 = False
                        messagebox.showinfo("分かったよ...","俺の負けだ....")
                        n += 1
                    else:
                        pass
            elif baka2 == False:
                pass
        else:
            pass
    

def sanshou():
    path = filedialog.askdirectory()
    dlPath_box.delete(0,tkinter.END)
    split = path.split("/Users")[1]
    dlPath = "C:/Users" + split
    dlPath_box.insert(0,dlPath)
    

def simpleDL(vid,i):
    dlPath = f"C:/Users/{username}/Downloads" if dlPath_box.get() == "" else dlPath_box.get()
    ext = extBLN.get()
    if ext == False:
        vid.streams.filter(progressive=True,file_extension="mp4").first().download(output_path=dlPath)
    else:
        vid.streams.filter(only_audio=True)[0].download(output_path=dlPath)
        title = vid.title.translate(str.maketrans("","",r'\\/:*?"<>|.~#;\','))
        os.rename(f"{dlPath}/{title}.mp4",f"{dlPath}/{title}.mp3")
    app.title(f"{title}{i}個のダウンロード完了")
    print(f"{vid.title}  のダウンロード完了")
    

def single_download():
    try:
        currentDL.place_forget()
    except Exception:
        pass
    url = url_box.get()
    if url.startswith("https://youtu.be/") or url.startswith("https://www.youtube.com/watch?v="):
        vid = YouTube(url)
        publishDay = str(vid.publish_date).split(" ")[0]
        currentDL = tkinter.Label(text=f"タイトル「{vid.title}\n投稿者:{vid.author}  視聴回数:{vid.views}  投稿日:{publishDay}",background="silver")
        currentDL.place(x=10,y=110)
        ext = extBLN.get()
        dlPath = f"C:/Users/{username}/Downloads" if dlPath_box.get() == "" else dlPath_box.get()
        if ext == False:
            vid.streams.filter(progressive=True,file_extension="mp4").first().download(output_path=dlPath)
        else:
            vid.streams.filter(only_audio=True)[0].download(output_path=dlPath)
            title = vid.title.translate(str.maketrans("","",r'\\/:*?"<>|.~#;\','))
            os.rename(f"{dlPath}/{title}.mp4",f"{dlPath}/{title}.mp3")
        quit_ask()
    else:
        error("url")
        

def channel_bulk_download():
    try:
        currentDL.place_forget()
    except Exception:
        pass
    ch = url_box.get()
    dlPath = f"C:/Users/{username}/Downloads" if dlPath_box.get() == "" else dlPath_box.get()
    if ch.startswith("https://www.youtube.com/channel/") or ch.startswith("https://www.youtube.com/c/"):
        chan = Channel(ch)
        currentDL = tkinter.Label(text=f"動画一括ダウンロード中のチャンネル:{chan.channel_name}",background="silver")
        currentDL.place(x=10,y=110)
        ext = extBLN.get()
        dlPath = f"C:/Users/{username}/Downloads" if dlPath_box.get() == "" else dlPath_box.get()
        for i,vid in enumerate(chan.videos,1):
            if ext == False:
                vid.streams.filter(progressive=True,file_extension="mp4").first().download(output_path=dlPath)
            else:
                vid.streams.filter(only_audio=True)[0].download(output_path=dlPath)
                title = vid.title.translate(str.maketrans("","",r'\\/:*?"<>|.~#;\','))
                os.rename(f"{dlPath}/{title}.mp4",f"{dlPath}/{title}.mp3")
            print(f"{vid.title}  のダウンロード完了")
            app.title(f"{title}{i}個のダウンロード完了")
        quit_ask()
    else:
        error("url")
    
    
def channel_tango_download():
    try:
        currentDL.place_forget()
    except Exception:
        pass
    ch = url_box.get()
    if ch.startswith("https://www.youtube.com/channel/") or ch.startswith("https://www.youtube.com/c/"):
        chan = Channel(ch)
        currentDL = tkinter.Label(text=f"動画一括ダウンロード中のチャンネル:{chan.channel_name}",background="silver")
        currentDL.place(x=10,y=130)
        word = tango_box.get()
        ext = extBLN.get()
        dlPath = f"C:/Users/{username}/Downloads" if dlPath_box.get() == "" else dlPath_box.get()
        for i,vid in enumerate(chan.videos,1):
            if word in vid.title:
                if ext == False:
                    vid.streams.filter(progressive=True,file_extension="mp4").first().download(output_path=dlPath)
                else:
                    vid.streams.filter(only_audio=True)[0].download(output_path=dlPath)
                    title = vid.title.translate(str.maketrans("","",r'\\/:*?"<>|.~#;\','))
                    os.rename(f"{dlPath}/{title}.mp4",f"{dlPath}/{title}.mp3")
                print(f"{vid.title}  のダウンロード完了")
                app.title(f"{title}{i}個のダウンロード完了")
            else:
                i -= 1
        quit_ask()
    else:
        error("url")
        
        
def hiduke_download():
    try:
        currentDL.place_forget()
    except Exception:
        pass
    dlPath = f"C:/Users/{username}/Downloads" if dlPath_box.get() == "" else dlPath_box.get()
    ch = url_box.get()
    hiduke = hiduke_box.get()
    hiduke_BA = hiduke_select.get()
    hiduke_count = len(hiduke)
    cut_hiduke = hiduke.replace("/","")
    if ch.startswith("https://www.youtube.com/channel/") or ch.startswith("https://www.youtube.com/c/"):
        chan = Channel(ch)
        currentDL = tkinter.Label(text=f"動画一括ダウンロード中のチャンネル:{chan.channel_name}",background="silver")
        currentDL.place(x=10,y=130)
        if "/" in hiduke and hiduke_count == 10:
            if hiduke_BA == "当日":
                for i,vid in enumerate(chan.videos,1):
                    vid_day = str(vid.publish_date).replace("/","")
                    if cut_hiduke == vid_day:
                        simpleDL(vid,i)
                    else:
                        i -= 1
                quit_ask()
            elif hiduke_BA == "より前":
                for i,vid in enumerate(chan.videos,1):
                    if vid_day <= cut_hiduke:
                        simpleDL(vid,i)
                    else:
                        i -= 1
                quit_ask()
            elif hiduke_BA == "より後":
                for i,vid in enumerate(chan.videos,1):
                    if vid_day >= cut_hiduke:
                        simpleDL(vid,i)
                    else:
                        i -= 1
                quit_ask()
            else:
                lock.release()
        else:
            error("hiduke")
    else:
        error("url")
        
        
def playlist_download():
    try:
        currentDL.place_forget()
    except Exception:
        pass
    pl_url = url_box.get()
    try:
        if "list=" in pl_url:
            pl = Playlist(pl_url)
            currentDL = tkinter.Label(text=f"{pl.title}内の動画を一括ダウンロード中",background="silver")
            currentDL.place(x=10,y=110)
            for i,vid in enumerate(pl.videos,1):
                simpleDL(vid,i)
            quit_ask()
        else:
            error("url")
    except Exception as e:
        error("playlist")
        

def bunkatu_download(): #ループした回数=loopcount-1
    loopcount = 0
    count = bunkatu_mode.get() #10
    downloaded = 0
    ch = url_box.get()
    dlPath = f"C:/Users/{username}/Downloads" if dlPath_box.get() == "" else dlPath_box.get()
    chan = Channel(ch)
    """
    for videoCount,checkvid in enumerate(chan.videos,1):
        print("\r{0}".format(f"{videoCount}個の動画が見つかりました"),end="")
    print("\n")
    """
    videoCount = len(chan.videos)
    ask = True
    while videoCount >= downloaded and ask == True:
        end = (count*loopcount)+count-1 if loopcount != 0 else count-1 #9 || (10*1)+10-1 = 19 || (10*2)+10-1 = 29 || (10*3)+10-1 = 39
        start = end-count if loopcount != 0 else 0 #0  || 19-10 = 9 || 29-10 = 19 || 39-10 = 29
        for vid,l in enumerate(chan.videos[start:end],1): #0:9  || 9:19 || 19:29 |29:39
            simpleDL(vid,l)
        loopcount += 1
        ask = messagebox.askyesno("確認",f"「はい」を押すと次の{count}本をダウンロードします")
    messagebox.showinfo(f"全{videoCount}本の動画のダウンロードが完了しました")
    quit_ask()
            
            
def make_gif():
    try:
        currentDL.place_forget()
    except Exception:
        pass
    url = url_box.get()
    start = str(gif_kaisi_select.get())
    end = str(gif_end_select.get())
    if url.startswith("https://youtu.be/") or url.startswith("https://www.youtube.com/watch?v="):
        if ":" in start and ":" in end:
            vid = YouTube(url)
            dlPath = f"C:/Users/{username}/Downloads" if dlPath_box.get() == "" else dlPath_box.get()
            currentDL = tkinter.Label(text=f"{vid.title}\nからGIF作成中{start}~{end}",background="silver")
            currentDL.place(x=10,y=130)
            fps = int(fps_entry.get())
            if fps < 61:
                vid.streams.filter(progressive=True,file_extension="mp4").first().download(output_path=dlPath)
                title = vid.title.translate(str.maketrans("","",r'\\/:*?"<>|.~#;\','))
                vid_path = f"{dlPath}/{title}.mp4"
                save_path = f"{dlPath}/{title}.gif"
                start = int(start.split(":")[0]*60) + int(start.split(":")[1])
                end = int(end.split(":")[0]*60) + int(end.split(":")[1])
                clip = VideoFileClip(vid_path).subclip(start,end)
                clip = clip.resize(width=600)
                clip.write_gif(save_path,fps=fps)
                clip.close()
                finish = messagebox.askyesnocancel("GIF作成完了","GIF作成が完了しました。切り取り済みの元動画(.mp4)を消去しますか？\nはい(Y):動画を消去するが、ウィンドウは閉じない\nいいえ(N):動画は消去せず、ウィンドウは閉じない\nキャンセル:動画を消去し、ウィンドウも閉じる")
                if finish == True:
                    os.remove(vid_path)
                    lock.release()
                elif finish == False:
                    lock.release()
                else:
                    os.remove(vid_path)
                    app.quit()
            else:
                error("fps")
        else:
            error("time")
    else:
        error("url")


def get_length():
    ch = url_box.get()
    all_length = 0
    if ch.startswith("https://www.youtube.com/channel/") or ch.startswith("https://www.youtube.com/c/"):
        chan = Channel(ch)
        for l,vid in enumerate(chan.videos,1):
            print("\r{0}".format(f"{l}個の動画が見つかりました"),end="")
            time.sleep(0.01)
        time.sleep(1)
        for i,vid in enumerate(chan.videos,1):
            all_length = all_length + vid.length
            print("\r{0}".format(f"チャンネルの平均動画尺を取得中 {i}/{l}",end=""))
            time.sleep(0.01)
        all_length_h = all_length / 3600
        heikin = all_length / i
        heikin_h = heikin / 3600
        fileSize = 0.17 * heikin
        fileSize_ = str(fileSize).split(".")[0]
        messagebox.showinfo("取得完了",f"総動画時間:{all_length}秒({all_length_h})時間)\n平均動画尺:{heikin}秒({heikin_h}時間)\n推定平均動画容量:{fileSize_}mb")
    else:
        error("url")
    
        
    
def call_single_download():
    if lock.acquire(timeout=0):
        th = threading.Thread(target=single_download)
        th.start()
    else:
        messagebox.showerror("処理エラー","まだ他の処理を実行中です")
def call_bulk_download():
    if lock.acquire(timeout=0):
        th = threading.Thread(target=channel_bulk_download)
        th.start()
    else:
        messagebox.showerror("処理エラー","まだ他の処理を実行中です")
def call_tango_download():
    if lock.acquire(timeout=0):
        th = threading.Thread(target=channel_tango_download)
        th.start()
    else:
        messagebox.showerror("処理エラー","まだ他の処理を実行中です")
def call_pl_download():
    if lock.acquire(timeout=0):
        th = threading.Thread(target=playlist_download)
        th.start()
    else:
        messagebox.showerror("処理エラー","まだ他の処理を実行中です")
def call_hiduke_download():
    if lock.acquire(timeout=0):
        th = threading.Thread(target=hiduke_download)
        th.start()
    else:
        messagebox.showerror("処理エラー","まだ他の処理を実行中です")
def call_bunkatu_download():
    if lock.acquire(timeout=0):
        th = threading.Thread(target=bunkatu_download)
        th.start()
    else:
        messagebox.showerror("処理エラー","まだ他の処理を実行中です")
def call_length_get():
    if lock.acquire(timeout=0):
        th = threading.Thread(target=get_length)
        th.start()
    else:
        messagebox.showerror("処理エラー","まだ他の処理を実行中です")
def call_gif():
    if lock.acquire(timeout=0):
        th = threading.Thread(target=make_gif)
        th.start()
    else:
        messagebox.showerror("処理エラー","まだ他の処理を実行中です")


def error(type):
    if type == "url":
        messagebox.showerror("URLエラー","URLの形式が正しいか確認してください")
        lock.release()
    elif type == "hiduke":
        messagebox.showerror("日付エラー","日付は 2020/01/09 のような形式で入力してください\n※0が必要です")
        lock.release()
    elif type == "time":
        messagebox.showerror("開始/終了位置エラー","開始位置か終了位置の形式が間違っています")
        lock.release()
    elif type == "playlist":
        messagebox.showerror("Playlistエラー","プレイリストが非公開になっていないか確認してください\nプレイリストが限定公開か公開状態でないとダウンロードはできません")
        lock.release()
    elif type == "fps":
        messagebox.showerror("FPSエラー","fpsの形式が正しいか確認してください\nfpsの最大値は60です")
        lock.release()
    else:
        pass


def quit_ask():
    finish = messagebox.askyesno("ダウンロード完了","ダウンロードが完了しました。ウィンドウを閉じますか？")
    if finish == True:
        app.quit()
    else:
        app.title(title)
        lock.release()
    


lock = threading.Lock()
app = tkinter.Tk()
app.title("Youtubeﾀﾞｳﾝﾛｰﾀﾞ")
app.geometry("550x250")

mode_label = tkinter.Label(text="モード選択")
mode_combobox = ttk.Combobox(values=["1:urlを指定して一つの動画のみをダウンロード", "2:チャンネルを指定して全ての動画をダウンロード","3:タイトルに任意の文字が入っている動画のみダウンロード","4:任意の日付もしくはそれより前or後の動画のみダウンロード","5:プレイリストを指定して動画を一括ダウンロード","6:動画の一括ダウンロードを10~100本ごとに区切って行う","7:動画をダウンロードしGIFを作成"],width=50)
mode_combobox.current(0)
mode_submit = ttk.Button(text="決定",command=submit)
url_label = tkinter.Label(text="動画URL")
url_box = ttk.Entry(width=53)
ch_label = tkinter.Label(text="チャンネルURL")
tango_label = tkinter.Label(text="単語")
tango_box = ttk.Entry(width=53)
jikkou_tango_button = ttk.Button(text="実行",command=call_tango_download)
jikkou_button = ttk.Button(text="実行",command=call_single_download)
jikkou_ikkatu_button = ttk.Button(text="実行",command=call_bulk_download)
dlPath_label = tkinter.Label(text="保存場所")
dlPath_box = ttk.Entry(width=53)
dlPath_shosan = ttk.Button(text="参照",command=sanshou)
username = os.environ['USERNAME']
title = "Youtubeﾀﾞｳﾝﾛｰﾀﾞ  |  "
vid_title_label = tkinter.Label(text="")
vid_des_label = tkinter.Label(text="")
hiduke_label = tkinter.Label(text="日付")
hiduke_box = ttk.Entry(width=40)
hiduke_select = ttk.Combobox(values=["当日","より前","より後"],width=10)
hiduke_select.current(0)
jikkou_hiduke_button = ttk.Button(text="実行",command=call_hiduke_download)
pl_label = tkinter.Label(text="PlaylistURL")
jikkou_pl_button = ttk.Button(text="実行",command=call_pl_download)
extBLN = tkinter.BooleanVar()
extBLN.set(False)
check_ext_button = ttk.Checkbutton(text="mp3(音声のみ)でダウンロード",variable=extBLN)
currentDL = tkinter.Label(text="")
ding_ = tkinter.Label(text="")
bunkatu_mode = ttk.Combobox(values=["5","10","50","100","カスタム"])
bunkatu_label = tkinter.Label(text="本ずつ")
jikkou_bunkatu_button = ttk.Button(text="実行",command=call_bunkatu_download)
keisan_bunkatu_button = ttk.Button(text="取得",command=call_length_get)
keisan_bunkatu_label = tkinter.Label(text="平均動画尺を取得する-->")
bunkatu_jikkou_label = tkinter.Label(text="分割ダウンロード実行-->")
dlPath = f"C:/Users/{username}Downloads"
gif_kaisi_label = tkinter.Label(text="開始位置(分:秒)")
gif_end_label = tkinter.Label(text="終了位置(分:秒)")
gif_kaisi_select = ttk.Entry(width=15)
gif_end_select = ttk.Entry(width=15)
gif_sakusei_button = ttk.Button(text="作成",command=call_gif)
fps_entry = ttk.Combobox(values=["5","10","30","カスタム"],width=10)
gif_fps_label = tkinter.Label(text="fps")
renketu_file_label = tkinter.Label(text="保存名")
renketu_file_entry = ttk.Entry(width=53)
check_ext_button.place(x=5,y=228)
mode_label.place(x=10,y=10)
mode_combobox.place(x=80,y=10)
mode_submit.place(x=425,y=8)


app.mainloop()
