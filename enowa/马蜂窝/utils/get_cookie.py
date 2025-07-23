import subprocess
import time
import requests
import os
import signal
import threading

def print_node_logs(process):
    def _read(pipe):
        for line in iter(pipe.readline, b''):
            print("[node]", line.decode().strip())
    threading.Thread(target=_read, args=(process.stdout,), daemon=True).start()
    threading.Thread(target=_read, args=(process.stderr,), daemon=True).start()

def get_w_tsfp_cookie(js_path='param_server.js', port=3000, timeout=60):
    """
    启动 Node.js 环境，监听 cookie，提取 w_tsfp 值。
    :param js_path: 启动的 JS 文件路径
    :param port: 服务监听端口
    :param timeout: 等待最大秒数
    :return: w_tsfp 字符串
    """
    node_process = subprocess.Popen(
        ['node', '/Users/liyongqi/PycharmProjects/spider/嗯哦哇/马蜂窝/static/env3.js'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        preexec_fn=os.setsid
    )
    print_node_logs(node_process)
    print(f"Node.js 服务已启动，监听端口 {port}，等待参数 w_tsfp...")

    try:
        for i in range(timeout):
            try:
                resp = requests.get(f'http://localhost:{port}/get')
                if resp.status_code == 200:
                    data = resp.json()
                    if data['success']:
                        print("成功获取 w_tsfp:", data['value'])
                        return data['value']
            except Exception as e:
                print(f"第{i+1}次尝试连接失败: {e}")
            time.sleep(1)

        raise TimeoutError("超时未获取到 w_tsfp 参数")
    finally:
        print("关闭 Node.js 服务...")
        os.killpg(os.getpgid(node_process.pid), signal.SIGTERM)