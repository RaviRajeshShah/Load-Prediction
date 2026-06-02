from flask import Flask , render_template , request
import pickle

app = Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route('/' , methods=['GET','POST'])
def home():
    if request.method=='GET':
        return render_template('index.html')

    elif request.method=='POST':
        v1=int(request.form['inp1'])
        v2=int(request.form['inp2'])
        v3=int(request.form['inp3'])
        v4=int(request.form['inp4'])
        v5=int(request.form['inp5'])
        v6=request.form['inp6']
        if v6=='Full-time':
            v6=0
        elif v6=='Part-time':
            v6=1
        elif v6=='Self-employed':
            v6=2
        else:
            v6=3
        v7=request.form['inp7']
        if v7=='Divorced':
            v7=0
        elif v7=='Married':
            v7=1
        elif v7=='Single':
            v7=2
        else:
            v7=3

        v8=int(request.form['inp8'])

        res=model.predict([[v1,v2,v3,v4,v5,v6,v7,v8]])

        if res[0]==0:
            res='NO'
        else:
            res='YES'

        return render_template('result.html',res1=res)

app.run(debug=True)
