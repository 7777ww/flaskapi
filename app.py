from flask import Flask,request
app=Flask((__name__))

@app.route("/")
def hello_word():
    return "hello"


stores=[
    {
        "name":"my_store",
        "items":[
            {
                "name":"chair",
                "price":200,
            }
        ]
    }
]

@app.get("/store")
def get_store(): 
    return {"store":stores}

@app.post("/store")
def create_store():
    request_data=request.get_json()
    new_store={
        "name":request_data["name"],
        "items":[],
    
    }
    stores.append(new_store)
    return new_store,201

@app.post("/store/<string:name>/item")
def create_item(name):
    request_data=request.get_json()
    print(f"Received data: {request_data}")
    for store in stores:
        if(store["name"]==name):
            new_items={
                "name":request_data["name"],
                "price":request_data["price"],

            }
            store["items"].append(new_items)
            return new_items,201
        
    return {"message": "Store not found"}, 404


@app.get("/store/<string:name>")
def get_store_by_name(name):
    for store in stores:
        if(store["name"]==name):
            return store
    return {"message": "Store not found"}, 404

@app.get("/store/<string:name>/item")
def get_item(name):
    for store in stores:
        if(store["name"]==name):
            return {"items":store["items"]}
            
    return {"message": "Store not found"}, 404

