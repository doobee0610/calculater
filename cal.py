import tkinter as tk
from tkinter import scrolledtext

# --- GUI 설정 ---

# 1. 메인 윈도우 생성
window = tk.Tk()
window.title("메모장")
window.geometry("800x600")

# 2. 텍스트 입력 영역 및 스크롤바 생성
# scrolledtext를 사용하면 스크롤바가 자동으로 연결됩니다.
text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, undo=True)
text_area.pack(expand=True, fill="both")

# 3. 메인 루프 시작
window.mainloop()
