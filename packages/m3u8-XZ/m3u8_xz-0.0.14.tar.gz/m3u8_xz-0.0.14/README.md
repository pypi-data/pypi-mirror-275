# m3u8-XZ

This is a simple package,it can download video by m3u8.

    pip install m3u8-xz
    
if you have installed old version

    pip install m3u8-xz --upgrade

####version 0.0.14 增加了中断后继续下载的功能
    
####version 0.0.13 增加了使用线程池请求的方法和启动方式

####version 0.0.12 捕获了一些可能发生的错误
    
####version 0.0.11 增加可选参数decryptKey，decryptKeyFunc
针对一些不是根据uri的结果直接解密的情况
    
####version 0.0.10 修复了上个版本的重大问题
    
####version 0.0.9 加入 _run_thread_ 启动方法,会在子线程执行

####version 0.0.8 修复一些小问题

####version 0.0.7 加入可选参数：

_headers_：可自定义头部
_path_：可自定义保存文件的绝对路径，
_logger_：可选择是否打印输出，
_print_callback_：打印回调，可通过**kwargs接收指定参数

####version 0.0.3 修复一些小问题

####version 0.0.2 support aes-128 decode,support read local m3u8 file
    
    from m3u8_XZ import m3u8
    # use m3u8 url 通过url
    obj = m3u8(url='https://example.com/index.m3u8', folder='test')
    # use local file 通过本地文件
    # m3u8(m3u8_file='fileName.m3u8', folder='test')
    # 异步启动方式 old
    # obj.run()
    # 2024年5月23日 新增启动方式
    obj.run(thread_num=20)
    

