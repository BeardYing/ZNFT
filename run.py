from flask import Flask,jsonify ,request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/my", methods=['GET'])
def my():
    # e.g. /my?id=1
    userId = request.args.get('id', default = None)
    if userId is not None:
        res = {
            "error": "",
            "message": "",
            "response": {
                "username": "beard",
                "userid": userId
            }
        }
    else:
        res = {
            "error": "NO_INPUT_ID",
            "message": "id為必填資訊",
            "response": ""
        }
    
    return jsonify(res)
  
    
@app.route("/my_nft", methods=['GET'])
def my_nft():
    # e.g. /my_nft?id=1&page_size=30&cursor=0
    userId = request.args.get('id', default = None)
    pageSize = request.args.get('page_size', default = 30)
    cursor = request.args.get('cursor', default = 0)
    
    if userId is not None:
        res = {
            "error": "",
            "message": "",
            "response": {
                "count": 3,
                "more" : False,
                "nft_list" : [{
                    "cache_img": "/asset/...",
                    "src": "https://storage.googleapis.com/nftimagebucket/tokens/0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d/preview/8420.png",
                    "name": "BoredApeYachtClub #8420"
                },{
                    "cache_img": "/asset/...",
                    "src": "https://storage.googleapis.com/nftimagebucket/tokens/0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d/preview/6383.png",
                    "name": "BoredApeYachtClub #6383"
                },{
                    "cache_img": "/asset/...",
                    "src": "https://storage.googleapis.com/nftimagebucket/tokens/0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d/preview/7943.png",
                    "name": "BoredApeYachtClub #7943"
                }]
            }
        }
    else:
        res = {
            "error": "NO_INPUT_ID",
            "message": "id為必填資訊",
            "response": ""
        }
    return jsonify(res)

@app.route("/put_nft", methods=['GET'])
def put_nft():
    # e.g. /put_nft?id=1&lat=23&lng=32&nft_id=10
    userId = request.args.get('id', default = None)
    lat = request.args.get('lat', default = None)
    lng = request.args.get('lng', default = None)
    nft_id = request.args.get('nft_id', default = None)


    if userId is None:
        res = {
            "error": "NO_INPUT_ID",
            "message": "id為必填資訊",
            "response": ""
        }
    elif lat is None:
        res = {
            "error": "NO_LAT",
            "message": "緯度為必填資訊",
            "response": ""
        }
    elif lng is None:
        res = {
            "error": "NO_LNG",
            "message": "經度為必填資訊",
            "response": ""
        }
    elif nft_id is None:
        res = {
            "error": "NO_NFT_ID",
            "message": "NFT 編號為必填",
            "response": ""
        }
    else:
        # 放置成功，回傳空白
        res = {
            "error": "",
            "message": "",
            "response": ""
        }
    
    return jsonify(res)



@app.route("/nearby_nft", methods=['GET'])
def nearby_nft():
    # e.g. /put_nft?id=1&lat=23&lng=32&nft_id=10
    lat = request.args.get('lat', default = None)
    lng = request.args.get('lng', default = None)
    pageSize = request.args.get('page_size', default = 30)
    cursor = request.args.get('cursor', default = 0)


    if lat is None:
        res = {
            "error": "NO_LAT",
            "message": "緯度為必填資訊",
            "response": ""
        }
    elif lng is None:
        res = {
            "error": "NO_LNG",
            "message": "經度為必填資訊",
            "response": ""
        }
    else:
        # e.g. /nearby_nft?lat=10&lng=10&page_size=2&cursor=0
        res = {
            "error": "",
            "message": "",
            "response": {
                "count": 10,
                "more" : True,
                "nft_list" : [{
                    "cache_img": "/asset/...",
                    "src": "https://storage.googleapis.com/nftimagebucket/tokens/0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d/preview/8420.png",
                    "name": "BoredApeYachtClub #8420"
                },{
                    "cache_img": "/asset/...",
                    "src": "https://storage.googleapis.com/nftimagebucket/tokens/0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d/preview/6383.png",
                    "name": "BoredApeYachtClub #6383"
                }]
            }
        }
    
    return jsonify(res)

@app.route("/pick_nft", methods=['GET'])
def pick_nft():
    # e.g. /pick_nft?id=1&nft_id=10
    userId = request.args.get('id', default = None)
    nft_id = request.args.get('nft_id', default = None)
    if userId is None:
        res = {
            "error": "NO_INPUT_ID",
            "message": "id為必填資訊",
            "response": ""
        }
    elif nft_id is None:
        res = {
            "error": "NO_NFT_ID",
            "message": "NFT id為必填資訊",
            "response": ""
        }
    else:

        ### 佔領NFT
        
        res = {
            "error": "",
            "message": "",
            "response": ""
        }

        ### 沒搶到的回傳資訊
        res = {
            "error": "FAILED",
            "message": "目前此NFT 處於不可取得狀況",
            "response": ""
        }
        
    
    return jsonify(res)

if __name__=='__main__':
    app.run(debug=True)