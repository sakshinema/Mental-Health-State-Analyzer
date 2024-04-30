@app.post("/recommand/")
def get_recommendation(data):
    d = {}
    for name in data.keys():
        with open("/recommendations/"+name+".txt","r") as f:
            content = f.read()
        d[name] = content
    return d