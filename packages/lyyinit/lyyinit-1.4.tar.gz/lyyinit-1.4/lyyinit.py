import os,sys

import ctypes
from ctypes import wintypes

import psutil
# 加载 user32.dll
user32 = ctypes.WinDLL('user32.dll')
kernel32 = ctypes.WinDLL('kernel32.dll')
from datetime import datetime,time as dtime
import psutil


    # 定义 EnumWindows 回调函数类型
EnumWindowsProcType = ctypes.WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM)

def get_hwnd_by_title(title):
    """
    好像并不能模糊匹配
    """
    def find_window_by_process_name(process_name):
        # 通过进程名获取进程ID
        process_id = get_process_id_by_name(process_name)
        if process_id is None:
            return None, None

        # 定义回调函数
        def EnumWindowsProc(hwnd, top_level):
            nonlocal found_hwnd
            if hwnd == 0:
                return True
            pid = wintypes.DWORD()
            user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
            if pid.value == process_id:
                length = user32.GetWindowTextLengthW(hwnd)
                if length > 0:
                    window_text = ctypes.create_unicode_buffer('\x00' * (length + 1))
                    user32.GetWindowTextW(hwnd, window_text, length + 1)
                    # 检查窗口文本是否包含进程名，以确认是否为所查找的进程的窗口
                    if process_name in window_text.value.lower():
                        found_hwnd = hwnd
                        return False  # 找到后不再继续枚举
            return True

        # 使用 EnumWindows 枚举所有顶级窗口，并检查其进程ID
        found_hwnd = None
        enum_windows_callback = EnumWindowsProcType(EnumWindowsProc)
        user32.EnumWindows(enum_windows_callback, 0)

        return found_hwnd, process_name
    
def get_process_id_by_name(process_name):
    handle = user32.CreateToolhelp32Snapshot(wintypes.DWORD(0x02), 0)
    pe32 = ctypes.wintypes.PROCESSENTRY32()
    pe32.dwSize = ctypes.sizeof(pe32)
    if not user32.Process32First(handle, ctypes.byref(pe32)):
        return None
    while True:
        if process_name.lower() == pe32.szExeFile.lower():
            return pe32.th32ProcessID
        if not user32.Process32Next(handle, ctypes.byref(pe32)):
            break
    user32.CloseHandle(handle)
    return None



def get_process_hwnds_by_name(process_name):
    # 获取当前正在运行的进程列表
    process = None
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            # 检查进程的名称是否匹配
            if proc.info['name'].lower() == process_name.lower():
                process = proc
                break
        except psutil.NoSuchProcess:
            continue

    # 如果没有找到匹配的进程，返回 None
    if process is None:
        return None

    # 获取进程ID
    process_id = process.pid

    # 存储找到的窗口句柄
    process_hwnds = []

    # 加载 user32.dll
    user32 = ctypes.WinDLL('user32')

    # 定义 EnumWindows 回调函数类型
    EnumWindowsProcType = ctypes.WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM)

    # 定义回调函数
    def EnumWindowsProc(hwnd, lParam):
        pid = wintypes.DWORD()
        user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
        if pid.value == process_id:
            process_hwnds.append(hwnd)
        return True

    # 设置回调函数
    enum_windows_callback = EnumWindowsProcType(EnumWindowsProc)

    # 使用 EnumWindows 枚举所有顶级窗口，并检查其进程ID
    user32.EnumWindows(enum_windows_callback, None)

    return process_hwnds



# 定义回调函数类型
EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, wintypes.HWND, wintypes.LPARAM)

# 定义需要的Windows API函数
user32 = ctypes.windll.user32
user32.EnumWindows.argtypes = [EnumWindowsProc, wintypes.LPARAM]
user32.IsWindowVisible.argtypes = [wintypes.HWND]
user32.GetWindowTextLengthW.argtypes = [wintypes.HWND]
user32.GetWindowTextW.argtypes = [wintypes.HWND, wintypes.LPWSTR, ctypes.c_int]

# 回调函数，用于枚举窗口
def foreach_window(hwnd, lParam):
    if user32.IsWindowVisible(hwnd):
        length = user32.GetWindowTextLengthW(hwnd)
        if length > 0:
            buffer = ctypes.create_unicode_buffer(length + 1)
            user32.GetWindowTextW(hwnd, buffer, length + 1)
            window_title = buffer.value
            hwnds.append((hwnd, window_title))
    return True

def get_window_title_by_pid(pid):
    def callback(hwnd, lParam):
        _, window_pid = ctypes.wintypes.DWORD(), ctypes.wintypes.DWORD()
        ctypes.windll.user32.GetWindowThreadProcessId(hwnd, ctypes.byref(window_pid))
        if window_pid.value == pid:
            length = user32.GetWindowTextLengthW(hwnd)
            if length > 0:
                buffer = ctypes.create_unicode_buffer(length + 1)
                user32.GetWindowTextW(hwnd, buffer, length + 1)
                titles.append(buffer.value)
        return True

    hwnds = []
    titles = []
    user32.EnumWindows(EnumWindowsProc(callback), 0)
    return titles

def get_window_title_by_exename(exe_name, title_keyword):
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == exe_name:
            print(f"进程ID: {proc.info['pid']}")
            titles = get_window_title_by_pid(proc.info['pid'])
            for title in titles:
                if title_keyword in title:
                    print(f"窗口标题: [{title}]")
                    return title
    return None
                
def get_process_from_title_pattern(window_title_pattern):
    """
    Finds the process ID and executable path of the window with the given title pattern.
    :param window_title_pattern: regex pattern of the window title.
    :return: A tuple containing the HWND and executable path of the window.
    """
    # 定义回调函数类型
    
    # 定义回调函数
    def EnumWindowsProc(hwnd, top_level):
        nonlocal found_process
        if hwnd == 0:
            return True
        window_text = ""
        if user32.GetWindowTextLengthW(hwnd) > 0:
            buffer = ctypes.create_unicode_buffer(''.join(['\x00'] * 512))
            user32.GetWindowTextW(hwnd, buffer, 512)
            window_text = buffer.value
        if window_title_pattern in window_text:
            pid = wintypes.DWORD(0)
            user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
            if pid.value:
                handle = kernel32.OpenProcess(0x400 | 0x10, False, pid.value)
                if handle:
                    exe_name = ctypes.create_unicode_buffer("\x00" * 260)
                    length = wintypes.DWORD(260)
                    if kernel32.QueryFullProcessImageNameW(handle, 0, exe_name, ctypes.byref(length)):
                        found_process = (hwnd, exe_name.value)
                        kernel32.CloseHandle(handle)
                        return False  # 找到后不再继续枚举
        return True

    # 设置回调函数
    callback_function = EnumWindowsProcType(EnumWindowsProc)

    # 初始化存储找到的进程信息
    found_process = (None, None)

    # 使用 ctypes 调用 EnumWindows 函数
    user32.EnumWindows(callback_function, 0)

    # 返回找到的窗口句柄和进程名
    return found_process
    
def is_window_responding(hwnd, try_again=True):
    """    #正常为True表示有响应
        # 加载 user32.dll
        # 定义 IsHungAppWindow 函数的原型
    """
    prototype_IsHungAppWindow = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.c_void_p)
    IsHungAppWindow = prototype_IsHungAppWindow(('IsHungAppWindow', user32))

    # 获取窗口句柄（HWND），这里需要您提供正确的窗口句柄
    # 调用 IsHungAppWindow 函数
    no_response = IsHungAppWindow(hwnd)

    # 如果 no_response 为 True，则表示窗口无响应
    if no_response:
        #print("The window is not responding.")
        if try_again:
            import time; time.sleep(10)
            result = is_window_responding(hwnd,try_again=False)
        else:
            result = False
        return result
    else:
        #print("The window is responding.")
        return True
    

    
def dynamic_function_call(function_name):
    """
    根据提供的函数名调用对应的函数。

    :param function_name: 要调用的函数的名称
    """
    # 检查函数名是否在当前全局命名空间中
    if function_name in globals():
        # 调用对应的函数
        globals()[function_name]()
    else:
        print(f"未找到名为 {function_name} 的函数。")


        
def is_rest_time():
    "休息时间返回真"
    now = datetime.now()
    weekday = now.weekday()
    current_time = now.time()

    # 定义工作时间的开始和结束时间
    work_start = dtime(8, 1)  # 早上8:01分
    work_end = dtime(23, 1)   # 晚上23:01分

    # 检查当前时间是否在工作时间之外
    if weekday < 5 and (current_time >= work_start and current_time < work_end):
        # 在工作日的8:01分到23:01分之间，不是休息时间
        return False
    else:
        # 在工作日的23:01分到次日8:01分之间，或者是周末，是休息时间
        return True
    
def is_busy_time():
    "上午开盘时间返回真"
    now = datetime.now()
    weekday = now.weekday()
    current_time = now.time()

    # 定义工作时间的开始和结束时间
    work_start = dtime(8, 30)  # 早上8:01分
    work_end = dtime(12, 1)   # 晚上23:01分

    # 检查当前时间是否在工作时间之外
    if weekday < 5 and (current_time >= work_start and current_time < work_end):
        # 在工作日的8:01分到23:01分之间，不是休息时间
        return True
    else:
        # 在工作日的23:01分到次日8:01分之间，或者是周末，是休息时间
        return False


def disable_quick_edit_mode():
    """关闭快速编辑模式，避免鼠标终端界面导致程序暂停"""
    if os.name == "nt":
        stdin_handle = ctypes.windll.kernel32.GetStdHandle(-10)
        mode = ctypes.c_ulong()
        ctypes.windll.kernel32.GetConsoleMode(stdin_handle, ctypes.byref(mode))
        ENABLE_QUICK_EDIT_MODE = 0x0040
        ENABLE_INSERT_MODE = 0x0020
        new_mode = mode.value & ~(ENABLE_QUICK_EDIT_MODE | ENABLE_INSERT_MODE)
        ctypes.windll.kernel32.SetConsoleMode(stdin_handle, new_mode)



def get_screen_width_height():
    user32 = ctypes.windll.user32
    screen_width, screen_height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    return screen_width, screen_height

def get_geometry_dynamic(fulltext=None,rate_width=0.15, rate_height=0.6, rate_x=0.5,rate_y=0.3):
    """"""
    screen_width, screen_height = get_screen_width_height()
    # 创建窗口的几何布局
    if fulltext:
        # 如果是以逗号分隔的字串包含有4个值，则将配置值拆分为子字符串列表
        
        values = [x.strip() for x in fulltext.split(",")]
        # 将子字符串转换为浮点数
        values = [float(value) for value in values]
        rate_width, rate_height, rate_x, rate_y = values

    geometry = "%dx%d+%d+%d" % (screen_width * rate_width, screen_height * rate_height, screen_width * rate_x, screen_height * rate_y)
    return geometry

def print_dict_with_child(data, indent=0):
    """
    递归打印字典中的键和值，带有缩进。
    
    :param data: 要打印的字典数据。
    :param indent: 当前的缩进级别。
    """
    if isinstance(data, dict):
        for key, value in data.items():
            print('  ' * indent + str(key) + ':', end=' ')
            if isinstance(value, (dict, list)):
                print()  # 打印一个换行符
                print_dict_with_child(value, indent + 1)  # 递归调用
            else:
                print(value)  # 打印值
    elif isinstance(data, list):
        print('  ' * indent + '[', end=' ')
        for item in data:
            print('  ' * (indent + 1) + str(item), end=', ' if not isinstance(item, dict) else '')
            if isinstance(item, dict):
                print_dict_with_child(item, indent + 1)
            print('  ' * indent + ']')
    else:
        print(data)

if __name__ == '__main__':
    print("# 获取所有正在运行的进程信息")
    get_window_title_by_exename("KingTrader.exe","预警 - ")
