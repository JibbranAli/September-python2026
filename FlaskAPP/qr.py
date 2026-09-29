from flask import Flask, request

import qrcode
app= Flask(__name__)

@app.route("/qr")
def qr():
    url = request.args.get("url")
    img = qrcode.make(url)
    img.save("QR.png")
    return "QR CODE GENERATED SUCCEFULLY "

app.run(debug=True)