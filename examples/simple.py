from flask import Flask
from flask_exchange import Exchange


exchange = Exchange()


class Config(object):

    EXCHANGE_ACCOUNT = "me@example.com"
    EXCHANGE_PASSWORD = "some_strong_password"
    EXCHANGE_URL = "webmail.example.com"
    EXCHANGE_VERIFY_SSL = False


if __name__ == '__main__':
    app = Flask(__name__)
    app.config.from_object(Config())
    exchange.init_app(app)

    for f in exchange.get_folders:
        print("Folder: \"{}\" contains \"{}\" total items! \"{}\" are unread".format(
            f.name,
            f.total_count,
            f.unread_count)
        )

    app.run()
