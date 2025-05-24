import tkinter as tk
from tkinter import ttk

# Bảng ánh xạ Unicode tổ hợp -> Unicode dựng sẵn
CHAR_MAP = {
    # Nguyên âm
    'a\u0300': 'à', 'a\u0301': 'á', 'a\u0303': 'ã', 'a\u0309': 'ả', 'a\u0323': 'ạ',
    'â': 'â', 'a\u0302\u0300': 'ầ', 'a\u0302\u0301': 'ấ', 'a\u0302\u0303': 'ẫ', 'a\u0302\u0309': 'ẩ', 'a\u0302\u0323': 'ậ',
    'ă': 'ă', 'ă\u0300': 'ằ', 'ă\u0301': 'ắ', 'ă\u0303': 'ẵ', 'ă\u0309': 'ẳ', 'ă\u0323': 'ặ',
    
    'e\u0300': 'è', 'e\u0301': 'é', 'e\u0303': 'ẽ', 'e\u0309': 'ẻ', 'e\u0323': 'ẹ',
    'ê': 'ê', 'ê\u0300': 'ề', 'ê\u0301': 'ế', 'ê\u0303': 'ễ', 'ê\u0309': 'ể', 'ê\u0323': 'ệ',
    
    'i\u0300': 'ì', 'i\u0301': 'í', 'i\u0303': 'ĩ', 'i\u0309': 'ỉ', 'i\u0323': 'ị',
    
    'o\u0300': 'ò', 'o\u0301': 'ó', 'o\u0303': 'õ', 'o\u0309': 'ỏ', 'o\u0323': 'ọ',
    'ô': 'ô', 'ô\u0300': 'ồ', 'ô\u0301': 'ố', 'ô\u0303': 'ỗ', 'ô\u0309': 'ổ', 'ô\u0323': 'ộ',
    'ơ': 'ơ', 'ơ\u0300': 'ờ', 'ơ\u0301': 'ớ', 'ơ\u0303': 'ỡ', 'ơ\u0309': 'ở', 'ơ\u0323': 'ợ',
    
    'u\u0300': 'ù', 'u\u0301': 'ú', 'u\u0303': 'ũ', 'u\u0309': 'ủ', 'u\u0323': 'ụ',
    'ư': 'ư', 'ư\u0300': 'ừ', 'ư\u0301': 'ứ', 'ư\u0303': 'ữ', 'ư\u0309': 'ử', 'ư\u0323': 'ự',
    
    'y\u0300': 'ỳ', 'y\u0301': 'ý', 'y\u0303': 'ỹ', 'y\u0309': 'ỷ', 'y\u0323': 'ỵ',
    
    # Chữ hoa
    'A\u0300': 'À', 'A\u0301': 'Á', 'A\u0303': 'Ã', 'A\u0309': 'Ả', 'A\u0323': 'Ạ',
    'Â': 'Â', 'Â\u0300': 'Ầ', 'Â\u0301': 'Ấ', 'Â\u0303': 'Ẫ', 'Â\u0309': 'Ẩ', 'Â\u0323': 'Ậ',
    'Ă': 'Ă', 'Ă\u0300': 'Ằ', 'Ă\u0301': 'Ắ', 'Ă\u0303': 'Ẵ', 'Ă\u0309': 'Ẳ', 'Ă\u0323': 'Ặ',
    
    'Đ': 'Đ',
}

def convert_text():
    input_text = txt_input.get("1.0", "end-1c")
    output_text = input_text
    
    # Thay thế từng ký tự theo ánh xạ
    for combo, precomposed in CHAR_MAP.items():
        output_text = output_text.replace(combo, precomposed)
    
    txt_output.delete("1.0", "end")
    txt_output.insert("1.0", output_text)

# Giao diện
root = tk.Tk()
root.title("Công cụ chuyển Unicode Tiếng Việt - VNTools")

frame = ttk.Frame(root, padding=10)
frame.grid()

# Ô nhập liệu
ttk.Label(frame, text="Nhập văn bản cần chuyển đổi:").grid(column=0, row=0, sticky=tk.W)
txt_input = tk.Text(frame, width=60, height=10)
txt_input.grid(column=0, row=1)

# Nút chuyển đổi
btn_convert = ttk.Button(frame, text="Chuyển đổi", command=convert_text)
btn_convert.grid(column=0, row=2, pady=5)

# Ô kết quả
ttk.Label(frame, text="Kết quả:").grid(column=0, row=3, sticky=tk.W)
txt_output = tk.Text(frame, width=60, height=10)
txt_output.grid(column=0, row=4)

root.mainloop()