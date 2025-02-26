from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_http():
    """Cloud Run HTTP function."""
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'name' in request_json:
        name = request_json['name']
    elif request_args and 'name' in request_args:
        name = request_args['name']
    else:
        name = 'Cloud Run'

    return f"Hello {name}! Deployment Test Successful, finally!"

if __name__ == "__main__":
    import os
    port = int(os.getenv("PORT", 8080))  # Ensure the app runs on the correct port
    app.run(host="0.0.0.0", port=port)


