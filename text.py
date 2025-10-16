import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

# --- 메뉴 커맨드 함수 ---

def new_file():
    """텍스트 영역을 지워 새 파일을 준비합니다."""
    if messagebox.askokcancel("새 파일", "작성 중인 내용을 저장하지 않고 새 파일을 만드시겠습니까?"):
        text_area.delete(1.0, tk.END)
        window.title("제목 없음 - 메모장")

def open_file():
    """파일을 열어 내용을 표시합니다."""
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("텍스트 문서", "*.txt"), ("모든 파일", "*.*")]
    )
    if not file_path:
        return
    try:
        with open(file_path, "r", encoding="utf-8") as input_file:
            text = input_file.read()
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, text)
        window.title(f"{file_path} - 메모장")
    except Exception as e:
        messagebox.showerror("오류", f"파일을 열 수 없습니다:\n{e}")

def save_file():
    """현재 내용을 파일로 저장합니다."""
    file_path = filedialog.asksaveasfilename(
        initialfile="제목 없음.txt",
        defaultextension=".txt",
        filetypes=[("텍스트 문서", "*.txt"), ("모den 파일", "*.*")]
    )
    if not file_path:
        return
    try:
        with open(file_path, "w", encoding="utf-8") as output_file:
            text = text_area.get(1.0, tk.END)
            output_file.write(text)
        window.title(f"{file_path} - 메모장")
    except Exception as e:
        messagebox.showerror("오류", f"파일을 저장할 수 없습니다:\n{e}")

def exit_app():
    """애플리케이션을 종료합니다."""
    if messagebox.askokcancel("종료", "메모장을 종료하시겠습니까?"):
        window.destroy()

# --- GUI 설정 ---

# 1. 메인 윈도우 생성
window = tk.Tk()
window.title("제목 없음 - 메모장")
window.geometry("800x600")

# 2. 메뉴바 생성
menu_bar = tk.Menu(window)

# 3. '파일' 메뉴 생성
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="새로 만들기", command=new_file)
file_menu.add_command(label="열기", command=open_file)
file_menu.add_command(label="저장", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="끝내기", command=exit_app)

# 메뉴바에 '파일' 메뉴 추가 및 윈도우에 설정
menu_bar.add_cascade(label="파일", menu=file_menu)
window.config(menu=menu_bar)

# 4. 텍스트 입력 영역 및 스크롤바 생성
# scrolledtext를 사용하면 스크롤바가 자동으로 연결됩니다.
text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, undo=True)
text_area.pack(expand=True, fill="both")

# 5. 윈도우 종료 프로토콜 설정 및 메인 루프 시작
window.protocol("WM_DELETE_WINDOW", exit_app)
window.mainloop()
