import pickle
import tempfile

# --- 3. 任意コード実行 ---
def unsafe_pickle(data):
    return pickle.loads(data)


# --- 4. ハードコードされた秘密情報 ---
API_KEY = "12345-SECRET-KEY"


# --- 5. 安全でない一時ファイル ---
def insecure_temp_file():
    tmp = tempfile.mktemp()
    with open(tmp, "w") as f:
        f.write("temp data")
    return tmp


# --- テスト用の関数呼び出し ---
if __name__ == "__main__":
    print(insecure_temp_file())
