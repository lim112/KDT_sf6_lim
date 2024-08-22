from flask import Flask, render_template
                            # 이름이 탬플릿인 이유 > #1
from flask import request
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

@app.route('/loop')
# 0819_4
def loop():
    item = ['a','b','c','d','e']
    return render_template('loop.html', items = item)
                                                        # items이 html로 전달된다
# 예외 처리를 한 경우
@app.route('/calc', methods = ['get', 'post'])
def calculate():
    if request.method == 'post':
        try:
            num = int(request.form['num'])
            # 폼에 입력된 글자는 문자이므로 숫자로 변경
        except ValueError:
            error_msg = '정수를 입력해주세요'
            return render_template('calculate.html', err_msg = error_msg)
        else:
            # 폼에 입력된 것은 문자이므로 숫자로 변환
            if num % 2 == 0:
                result = '짝수입니다'
            else:
                result = '홀수입니다'
            return render_template('calc_result_0819_8.html', result = result, num = num )
    else:
        # request.method == 'get'
        return render_template('calculate_0819_7.html')
if __name__ == '__main__':
    # app.run(debug=True)
    app.run()