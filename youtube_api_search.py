from googleapiclient.discovery import build

def get_youtube_video_links(api_key, query, max_results=10):
    # Create a YouTube API client
    youtube = build('youtube', 'v3', developerKey=api_key)
    
    # Perform a search request
    search_response = youtube.search().list(
        q=query,
        part='snippet',
        type='video',
        maxResults=max_results
    ).execute()
    
    # Extract video links from the response
    video_links = []
    for item in search_response['items']:
        video_id = item['id']['videoId']
        video_link = f"https://www.youtube.com/watch?v={video_id}"
        video_links.append(video_link)
    
    return video_links

if __name__ == "__main__":
    API_KEY = 'API KEY'  # Replace with your API key
    search_query = input("Enter search query: ")
    
    video_links = get_youtube_video_links(API_KEY, search_query)
    
    print("Top video links:")
    for link in video_links:
        print(link)
