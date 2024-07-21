from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter

def get_video_transcript(video_id):
    try:
        # Fetch the transcript for the given video ID
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        
        # Format the transcript as JSON
        formatter = JSONFormatter()
        formatted_transcript = formatter.format_transcript(transcript)
        
        return formatted_transcript
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    # List of video IDs or video URLs
    video_urls = [
        'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
        'https://www.youtube.com/watch?v=3JZ_D3ELwOQ'
    ]
    
    # Extract video IDs from URLs
    video_ids = [url.split('v=')[-1] for url in video_urls]
    
    # Fetch and print transcripts for each video
    for video_id in video_ids:
        transcript = get_video_transcript(video_id)
        print(f"Transcript for video ID {video_id}:\n{transcript}\n")
