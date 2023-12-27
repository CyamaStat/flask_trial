# これはサンプルの Python スクリプトです。

# Shift+F10 を押して実行するか、ご自身のコードに置き換えてください。
# Shift を2回押す を押すと、クラス/ファイル/ツールウィンドウ/アクション/設定を検索します。

# インストールした「flask」モジュールをインポートする
from flask import Flask, render_template

# インスタンス化する
app = Flask(__name__)  # アンダースコア(_)をnameの左右にそれぞれ2つずつ書く


# ルーティング設定をする
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":  # 最後に記述する
    app.run(debug=True)

# PyCharm のヘルプは https://www.jetbrains.com/help/pycharm/ を参照してください
