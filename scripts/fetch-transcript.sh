#!/bin/bash
# Fetch YouTube Transcript
# Usage: ./scripts/fetch-transcript.sh "https://www.youtube.com/watch?v=XXXXX"
# Output: Raw transcript text to stdout

set -e

URL="$1"

if [ -z "$URL" ]; then
    echo "Usage: fetch-transcript.sh <youtube-url>" >&2
    exit 1
fi

# Extract video ID from various YouTube URL formats
VIDEO_ID=""

# youtube.com/watch?v=ID
if echo "$URL" | grep -q '[?&]v='; then
    VIDEO_ID=$(echo "$URL" | sed -E 's/.*[?&]v=([^&]+).*/\1/')
# youtu.be/ID
elif echo "$URL" | grep -q 'youtu\.be/'; then
    VIDEO_ID=$(echo "$URL" | sed -E 's/.*youtu\.be\/([^?]+).*/\1/')
# youtube.com/live/ID
elif echo "$URL" | grep -q 'youtube\.com/live/'; then
    VIDEO_ID=$(echo "$URL" | sed -E 's/.*youtube\.com\/live\/([^?]+).*/\1/')
# youtube.com/embed/ID
elif echo "$URL" | grep -q 'youtube\.com/embed/'; then
    VIDEO_ID=$(echo "$URL" | sed -E 's/.*youtube\.com\/embed\/([^?]+).*/\1/')
fi

if [ -z "$VIDEO_ID" ]; then
    echo "Error: Could not extract video ID from URL: $URL" >&2
    exit 1
fi

echo "Fetching transcript for video: $VIDEO_ID" >&2

# Install youtube_transcript_api if not present
pip3 install --user --quiet youtube_transcript_api 2>/dev/null

# Fetch and output transcript
export VIDEO_ID="$VIDEO_ID"
python3 -c "
import os, sys

try:
    from youtube_transcript_api import YouTubeTranscriptApi

    video_id = os.environ['VIDEO_ID']
    ytt_api = YouTubeTranscriptApi()
    transcript = ytt_api.fetch(video_id)

    for entry in transcript:
        print(entry.text)

except Exception as e:
    print(f'Error fetching transcript: {e}', file=sys.stderr)
    sys.exit(1)
"
