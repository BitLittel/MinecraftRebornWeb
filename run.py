#!flask/bin/python
from main import main


if __name__ == "__main__":
    main.run(debug=True, host='0.0.0.0', port=5000)