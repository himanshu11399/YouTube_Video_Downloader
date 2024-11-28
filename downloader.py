import yt_dlp

# Provide the YouTube video URL
url = input("Enter the URL of the video: ")

# Set up options to download the highest resolution video
ydl_opts = {
    'format': 'best',  # Download the best available quality
    'outtmpl': '%(title)s.%(ext)s',  # Output file name with video title
}

# Download the video and print author, quality, title, and publish date
try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Extract video information (metadata) without downloading the video
        info_dict = ydl.extract_info(url, download=False)

        # Get video title, author, quality, and publish date
        video_title = info_dict.get('title', 'Unknown Title')
        video_author = info_dict.get('uploader', 'Unknown Author')
        video_quality = info_dict.get('format_note', 'Unknown Quality')
        video_publish_date = info_dict.get('upload_date', 'Unknown Publish Date')

        # Convert the publish date from YYYYMMDD to a readable format (optional)
        if video_publish_date != 'Unknown Publish Date':
            video_publish_date = f"{video_publish_date[:4]}-{video_publish_date[4:6]}-{video_publish_date[6:]}"

        # Print video metadata
        print(f"Video Title: {video_title}")
        print(f"Author: {video_author}")
        print(f"Quality: {video_quality}")
        print(f"Publish Date: {video_publish_date}")

        # Now download the video
        print("Downloading video...")
        ydl.download([url])

    # Print confirmation after the download is complete
    print()
    print("Download completed successfully!")
    print(f"Video Title: {video_title}")
    print(f"Author: {video_author}")
    print(f"Quality: {video_quality}")
    print(f"Publish Date: {video_publish_date}")
    print("Thanks for Using :-")

except Exception as e:
    print(f"An error occurred: {e}")
