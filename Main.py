from flask import Flask, jsonify, request
app = Flask(__name__)

tasks = [
    {
        "id":1,
        "title":u"Raj",
        "description":u"7829301832",
        "done":False
    },
    {
        "id":2,
        "title":u"Aishani",
        "description":u"9037283918",
        "done":False
    }
]

@app.route("/add-task",methods=["POST"])

def AddTask():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the data",
        },400)
    
    task = {
        "id":tasks[-1]["id"]+1,
        "title": request.json["title"],
        "description": request.json.get("description",""),
        "done": False
    }
    
    tasks.append(task)
    return jsonify({
        "status": "success",
        "message":"Task added successfully"
    })
    
@app.route("/get-data")

def getTask():
    return jsonify({
        "data":tasks
    })
    
@app.route('/')
def HelloWorld():
    return("Hello World!")

if (__name__=="__main__"):
    app.run(debug=True)