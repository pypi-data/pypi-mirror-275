import ctypes

# 定义一个结构体，用于字体信息的设置
class CONSOLE_FONT_INFOEX(ctypes.Structure):
    _fields_ = [("cbSize", ctypes.c_ulong),
                ("nFont", ctypes.c_ulong),
                ("dwFontSize", ctypes.c_int),
                ("FontFamily", ctypes.c_uint),
                ("FontWeight", ctypes.c_uint),
                ("FaceName", ctypes.c_wchar * 32)]

# 获取标准输出的句柄
STD_OUTPUT_HANDLE = -11
handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

# 创建一个CONSOLE_FONT_INFOEX实例
font = CONSOLE_FONT_INFOEX()
font.cbSize = ctypes.sizeof(CONSOLE_FONT_INFOEX)
font.nFont = 12
font.dwFontSize = 18  # 字体大小
font.FontFamily = 54
font.FontWeight = 400
font.FaceName = "Consolas"

# 设置新的字体信息
ctypes.windll.kernel32.SetCurrentConsoleFontEx(
    handle, ctypes.c_long(False), ctypes.pointer(font))
