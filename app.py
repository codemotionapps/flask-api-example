from app import app
import os


if __name__ == '__main__':
	app.run(debug=True, use_debugger=False, use_reloader=True, threaded=True, host='0.0.0.0', port=5001)
