from flask import Flask,url_for

app = Flask(__name__)

# @app.route('/')
# def hello():
#     return 'hello'
#
# @app.route('/user/<name>')
# def user_page(name):
#     return 'User:%s'% name
#
# @app.route('/test')
# def test_url_for():
# # 下面是一些调用示例（请在命令行窗口查看输出的 URL）：
#     print(url_for('hello'))
#     print(url_for('test_url_for',num=2))
#     print(url_for('user_page',name='fcsprite'))
#     return 'Test page'
#


@app.route('/home')
def index():
    return 'Hello,FcSprite!' \
           '你好,幻彩雪碧!'\
            '<h1>Hello Flask!</h1><img src="http://helloflask.com/totoro.gif">'
if __name__ == '__main__':
    # print(app.url_map)
    app.run()