from flask import Flask, render_template, request

app=Flask("Web")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login/request" ,methods=["GET","POST"])
def validlogin():
    starship=["Enterprise","Kelvin","Franklin","Endurance"]
    if request.method=="GET":
        return render_template("submitform.html")
    else:
        email=request.form.get("email")
        passw=request.form.get("key")
        uname=email.rstrip("@huebrint.com")
        uname=uname.capitalize()
        s="moc.tnirbeuh@"
        i=-1
        n=0
        while i>-14 and n<13:
            if email[i]==s[n]:
                pass
            else:
                return render_template("tryagain.html",wrong="Email")
                break
            i=i-1
            n=n+1
        else:
            if passw=="dictatorule":
                return render_template("correct.html",User=uname,Starship=starship)
            else:
                return render_template("tryagain.html",wrong="Password")
