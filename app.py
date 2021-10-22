from src import app
import sys
import os

if __name__ == "__main__":
    app.config["sample_img"] = sys.argv[1]
    app.run(debug=False, port=os.environ.get("PORT", 5000), host="0.0.0.0")

    # app.run(debug=True)
