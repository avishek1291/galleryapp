from __init__ import create_app


def run():
    app = create_app()
    app.run(port=8080)


if __name__ == "__main__":
    run()
