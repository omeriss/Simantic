from RestController import create_app


def main():
    app = create_app(model_path="./model/model.dat")
    app.run(host='0.0.0.0', port=80)


if __name__ == '__main__':
    main()
