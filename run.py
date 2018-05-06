from myapp.create_app import app

if __name__ == '__main__':
    app.run(app.config['IP_ADDRESS'], port=909090, debug=True)