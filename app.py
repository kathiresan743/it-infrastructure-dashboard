from flask import Flask, render_template, jsonify
from collector import get_server_stats
from servers import SERVERS
import threading

app = Flask(__name__)

def fetch_all():
    results = []
    threads = []
    lock = threading.Lock()

    def fetch(server):
        data = get_server_stats(
            server["ip"],
            server["username"],
            server["password"]
        )
        data["name"] = server["name"]
        with lock:
            results.append(data)

    for server in SERVERS:
        t = threading.Thread(target=fetch, args=(server,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return sorted(results, key=lambda x: x["name"])

@app.route("/")
def index():
    return render_template("dashboard.html")

@app.route("/api/servers")
def api_servers():
    return jsonify(fetch_all())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)