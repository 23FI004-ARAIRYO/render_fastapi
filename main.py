from typing import Optional

from fastapi import FastAPI

from fastapi.responses import HTMLResponse #インポート

import random  # randomライブラリを追加

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉",
        "中吉",
        "小吉",
        "吉",
        "半吉",
        "末吉",
        "末小吉",
        "凶",
        "小凶",
        "大凶"
    ]

    return {"result" : omikuji_list[random.randrange(10)]}

@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
<<<<<<< HEAD
            <title>りょうのホームページ</title>
            <style>
                body {
                    text-align: center;
                    padding: 20px;
                }

                h1 {
                    font-size: 2.5em;
                    font-weight: bold;
                    background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);
                    margin-bottom: 10px;
                }

                pre {
                    font-size: 1.2em;
                }

                table {
                    margin: 30px;
                    border-collapse: collapse;
                    width: 50%;
                }

                table, th, td {
                    border: 10px grove #ff00aa;
                }

                th, td {
                    padding: 10px;
                    background-color: #ffffff;
                }
            </style>
=======
            <title>りょうのホームページ</title>
>>>>>>> 768e10fc282ca26f12c7023d4cee0eb986e01167
        </head>
        <body>
            <h1>ようこそ　りょう　のホームページへ！</h1>
            <pre>
            ＿人人人人人人人人人人人人人人人人人人人＿
            ＞　　　ゆっくりしていってね！！！　　　＜
            ￣^Ｙ^Ｙ^Ｙ^Ｙ^Ｙ^Ｙ^Ｙ^Ｙ^Ｙ^Ｙ^Ｙ^Ｙ^￣
            </pre>
            <table>
                <tr>
                    <th>項目</th>
                    <th>内容</th>
                </tr>
                <tr>
                    <td>名前</td>
                    <td>荒井 涼</td>
                </tr>
                <tr>
                    <td>生年月日</td>
                    <td>2004年10月4日</td>
                </tr>
                <tr>
                    <td>血液型</td>
                    <td>O型</td>
                </tr>
                <tr>
                    <td>趣味</td>
                    <td>ゲーム、アニメ、パチンコ・スロット</td>
                </tr>
            </table>
            <p>このページではおみくじを引けるよ</p>
            <h1>ようこそ　りょう　のホームページへ！</h1>
            <pre>
            ＿人人人人人人人人人人人人人人人＿
            ＞　　　ゆっくりしていってね！！！　　　＜
            ￣^Ｙ^Ｙ^Ｙ^Ｙ^Ｙ^Ｙ^Ｙ^Ｙ^Ｙ^Ｙ^Ｙ^Ｙ^Ｙ^Ｙ^￣
            </pre>
            <table>
                <tr>
                    <th>項目</th>
                    <th>内容</th>
                </tr>
                <tr>
                    <td>名前</td>
                    <td>荒井 涼</td>
                </tr>
                <tr>
                    <td>生年月日</td>
                    <td>2004年10月4日</td>
                </tr>
                <tr>
                    <td>血液型</td>
                    <td>O型</td>
                </tr>
                <tr>
                    <td>趣味</td>
                    <td>ゲーム、アニメ、パチンコ・スロット</td>
                </tr>
            </table>
            <p>このページではおみくじを引けるよ</p>
            <a href="/omikuji">おみくじを引く</a>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/present")
async def give_present(present):
    return {"response": f"サーバです。メリークリスマス！ {present}ありがとう。お返しはキャンディーです。"}  # f文字列というPythonの機能を使っている