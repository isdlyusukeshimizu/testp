from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def portfolio():
    return render_template('portfolio.html')

#取り組み内容を表示するページ
@app.route('/torikumi')
def torikumi():
    return render_template('torikumi.html')

#Docker勉強会の内容を表示するページ
@app.route('/docker_lec')
def docker_lec():
    return render_template('docker_lec.html')

#画像ファイルをmediaフォルダから取得
@app.route('/media/<path:filename>')
def media_files(filename):
    file_path = safe_join('media', filename)
    if not os.path.isfile(file_path):
        abort(404)  # ファイルが存在しない場合は404エラーを返す
    return send_from_directory('media', filename)

if __name__ == '__main__':
    app.run(debug=True)
