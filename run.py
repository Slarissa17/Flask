from app import app

app.config['SECRET_KEY'] = 'chave_secreta'


if __name__ == "__main__":
    app.run()
