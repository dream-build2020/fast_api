def my_callback(result):
    print("正在使用回调函数：", result)


def perform_callback(callback):
    result = 10 + 20

    # 调用回调函数
    callback(result)


perform_callback(my_callback)
