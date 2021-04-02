from src import create_app

from src.config import set_config_from_file

config = set_config_from_file("./config.yaml")
app = create_app(config)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
