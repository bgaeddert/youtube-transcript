# flask app for an API the returns hello world
from flask import Flask, request, jsonify

# import get_video_details from youtube.py
from youtube_details import get_video_details

app = Flask(__name__)

# define a route for the default URL, which loads the form
@app.route('/', methods=['GET'])
def video_deatils():
    # get url from query string parameter video
    url = request.args.get('video', default=None)

    # if url is not provided, return in json format
    if not url:
        return jsonify({'error': 'Please provide a video URL or id'})

    try:
        return get_video_details(url)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')