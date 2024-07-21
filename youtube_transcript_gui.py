import tkinter as tk
from tkinter import scrolledtext
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

def fetch_transcripts():
    # Clear the text area
    text_area.delete('1.0', tk.END)
    
    # Get video URLs from the input field
    urls = url_entry.get("1.0", tk.END).strip().split('\n')
    video_ids = [url.split('v=')[-1] for url in urls]
    
    # Fetch and display transcripts
    for video_id in video_ids:
        transcript = get_video_transcript(video_id)
        text_area.insert(tk.END, f"Transcript for video ID {video_id}:\n{transcript}\n\n")

# Create the main window
window = tk.Tk()
window.title("YouTube Transcript Fetcher")

# Create and place widgets
url_label = tk.Label(window, text="Enter YouTube Video URLs (one per line):")
url_label.pack(pady=5)

url_entry = scrolledtext.ScrolledText(window, height=10, width=50)
url_entry.pack(pady=5)

fetch_button = tk.Button(window, text="Fetch Transcripts", command=fetch_transcripts)
fetch_button.pack(pady=5)

text_area = scrolledtext.ScrolledText(window, height=20, width=80)
text_area.pack(pady=5)

# Run the application
window.mainloop()
