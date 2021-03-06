from flask import Flask,url_for,render_template

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
@app.route('/')
def index():
    return  render_template('index.html',name=name,movies=movies)

@app.route('/home')
def home():
    return 'Hello,FcSprite!' \
           '你好,幻彩雪碧!'\
            '<h1>Hello Flask!</h1><img src="http://helloflask.com/totoro.gif">'
name = '幻彩雪碧'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
        ]

if __name__ == '__main__':
    # print(app.url_map)
    app.run()