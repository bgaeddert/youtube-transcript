import re
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

def get_video_details(url):
    # parse video id from url ex. https://www.youtube.com/watch?v=B6oRi9TIkyQ&ab_channel=TinaHuang
    video_id = extract_video_id(url)

    # if video id is not found, return in json format
    if not video_id:
        raise Exception('Please provide a valid video URL or id')

    # create a youtube link with the video id
    url = f'https://www.youtube.com/watch?v={video_id}'

    # if url is not provided, return in json format
    if not url:
        raise Exception('Please provide a valid video URL or id')
    
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the video title and channel name
        title = yt.title
        channel = yt.author

        # Get the video ID from the URL and use it to get the transcript
        video_id = url.split('=')[-1]
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)

        # Format the transcript
        formatter = TextFormatter()
        transcript = formatter.format_transcript(transcript_list)

        # Format the details into a JSON object
        video_details = {
            'url': url,
            'title': title,
            'channel': channel,
            'transcript': transcript
        }

        return video_details
    except Exception as e:
        raise Exception(str(e))

def extract_video_id(url_or_id):
    # detect if url is a youtube url
    if 'youtube' not in url_or_id:
        # just return since it could be just the id
        return url_or_id

    pattern = r'v=([^&]+)'
    match = re.search(pattern, url_or_id)
    if match:
        return match.group(1)
    else:
        return None