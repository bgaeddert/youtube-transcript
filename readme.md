## YouTube Transcript and Video Details

This Python Flask app runs in a Docker container and listens on the default port 5000. It is designed to process a YouTube video URL or ID and return details such as channel name, video title, transcript in plain text, and the video URL in JSON format. The output structure is as follows:

```json
{
    "channel": "channel name",
    "title": "video title",
    "transcript": "transcript in plain text",
    "url": "https://www.youtube.com/watch?v=<video_id>"
}
```

### Usage

```bash
curl "http://localhost?video=https://www.youtube.com/watch?v=<video_id>"
```

### Google Cloud Run

This app is a small experiment intended to run on Google Cloud Run, a managed platform that enables running containers on Google Cloud with automatic scaling based on request volume. Google Cloud Run allows users to specify a Docker image from DockerHub, set network ports, and provides a URL to access the running container. The service also supports environment variable configuration and resource allocation management.