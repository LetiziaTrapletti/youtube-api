import googleapiclient.discovery

from api_function import get_comments_from_video

# Get credentials and create an API client
api_key = '' #Provide your Youtube API Key
api_service_name = "youtube"
api_version = "v3"
youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=api_key)

#Social Campaign IDs
video_ids = ['vDWSdBN9Fu4','sxPqBT19bfA'] #Replace with video_ids or social campaigns for which you would like to retrieve comments data

# Call API and convert output to JSON
social_media_campaign_comments = get_comments_from_video(youtube,video_ids)

# Print the JSON string 
print(social_media_campaign_comments)