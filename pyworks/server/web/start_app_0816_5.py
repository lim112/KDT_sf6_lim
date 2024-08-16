from flask import Flask, render_template
                            # 이름이 탬플릿인 이유 > #1
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
                            #1 같은 폴더내가 아니지만 render_template을 활용해
                            # template 이름인 파일을 불러올 수 있음
    # return '메인 페이지 입니다'
@app.route('/season')
def get_season():
    season = '여름'
    seasons = ['봄', '여름','가을','겨울']
    return render_template('season.html',
                           season = season,
                           seasons = seasons)
                            # season.html로 시즌이 여름인것 보내기
if __name__ == '__main__':
    # app.run(debug=True)
    app.run()