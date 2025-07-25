import os
import subprocess
import pickle
import yaml
import hashlib
import tempfile
import flask
from flask import Flask, request
import urllib.request

app = Flask(__name__)

# --- 1. OSコマンドインジェクション ---
def command_injection(user_input):
    subprocess.run("ls " + user_input, shell=True)  # CWE-78

# --- 2. Pickleによる任意コード実行 ---
def unsafe_pickle_load(file_path):
    with open(file_path, "rb") as f:
        return pickle.load(f)  # CWE-502

# --- 3. ハードコーディングされたパスワード ---
def hardcoded_password():
    password = "P@ssw0rd123"  # CWE-798
    return password

# --- 4. ワールド書き込み可能なファイル作成 ---
def insecure_file_creation(filename):
    os.chmod(filename, 0o777)  # CWE-732

# --- 5. evalによるコード実行 ---
def insecure_eval(user_code):
    eval(user_code)  # CWE-94

# --- 6. execによるコード実行 ---
def insecure_exec(user_code):
    exec(user_code)  # CWE-94

# --- 7. yaml.loadの安全でない読み込み ---
def insecure_yaml_load(file_path):
    with open(file_path, "r") as f:
        return yaml.load(f, Loader=yaml.Loader)  # CWE-20 (安全でないデシリアライザ)

# --- 8. 弱いハッシュ関数 ---
def weak_hash(data):
    return hashlib.md5(data.encode()).hexdigest()  # CWE-327

# --- 9. Flaskのdebugモード ---
@app.route("/debug")
def debug_route():
    # Flask debug=True は危険と判定される
    app.run(debug=True)  # CWE-489

# --- 10. SSRF (サーバサイドリクエストフォージェリ) ---
def ssrf_example(url):
    return urllib.request.urlopen(url).read()  # CWE-918

# --- 11. テンポラリファイルの不適切利用 ---
def insecure_tempfile():
    tmp = tempfile.mktemp()  # CWE-377
    with open(tmp, "w") as f:
        f.write("test")
    return tmp

# --- 12. subprocessでユーザ入力を直接渡す ---
def subprocess_popen(user_input):
    subprocess.Popen(user_input, shell=True)  # CWE-78

# --- 13. os.system の直接実行 ---
def os_system_call(user_input):
    os.system("echo " + user_input)  # CWE-78

# --- 14. ディレクトリトラバーサル ---
def directory_traversal(filename):
    with open("/var/data/" + filename, "r") as f:
        return f.read()  # CWE-22

# --- 15. ハードコーディングされたAPIキー ---
API_KEY = "12345-ABCDE-SECRET"  # CWE-798


if __name__ == "__main__":
    command_injection("; echo Pwned")
    unsafe_pickle_load("malicious.pkl")
    print(hardcoded_password())
    insecure_file_creation("test.txt")
    insecure_eval("print('Hello from eval')")
    insecure_exec("print('Hello from exec')")
    insecure_yaml_load("data.yaml")
    print(weak_hash("password"))
    ssrf_example("http://example.com")
    print(insecure_tempfile())
    subprocess_popen("ls")
    os_system_call("Hello")
    directory_traversal("../../etc/passwd")
