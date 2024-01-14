import json

def get_comments_from_video(youtube,video_ids):

    video_comments = []

    for video_id in video_ids:
        
        #pull video info
        request = youtube.videos().list(
            part="id,snippet,statistics",
            id=video_id
        )
        response = request.execute()

        videoTitle = response['items'][0]['snippet']['title']
        videoTimestamp = response['items'][0]['snippet']['publishedAt']
        viewCount = response['items'][0]['statistics']['viewCount']
        likeCount = response['items'][0]['statistics']['likeCount']
        commentCount = response['items'][0]['statistics']['commentCount']
        videoAuthor = response['items'][0]['snippet']['channelTitle']

    
        #pull comment threads info
        request = youtube.commentThreads().list(
            part="id,snippet,replies",
            videoId=video_id
        )
        response = request.execute()

        #check if there are parent comments for this video
        if 'items' in response:

            #for each parent comment, extract author, ID, text, and timestamp
            parent_comments = []
            for parent_comment in response['items'][0:10]:

                parentAuthor = parent_comment['snippet']['topLevelComment']['snippet']['authorDisplayName']
                parentId = parent_comment['snippet']['topLevelComment']['id']
                parentText = parent_comment['snippet']['topLevelComment']['snippet']['textOriginal']
                parentTimestamp = parent_comment['snippet']['topLevelComment']['snippet']['publishedAt']

                # Check if there are replies for this parent comment
                if 'replies' in parent_comment and 'comments' in parent_comment['replies']:

                    #for each reply, extract author, ID, text, and timestamp
                    replies = []
                    for reply in parent_comment['replies']['comments'][0:10]:

                        childAuthor = reply['snippet']['authorDisplayName']
                        childId = reply['id']
                        childText = reply['snippet']['textOriginal']
                        childTimestamp = reply['snippet']['publishedAt']

                        replies.append({'childAuthor' : childAuthor,
                                        'childId' : childId,
                                        'childText' : childText,
                                        'childTimestamp' : childTimestamp})
                    
                    parent_comments.append({'parentAuthor' : parentAuthor,
                                            'parentId' : parentId,
                                            'parentText' : parentText,
                                            'parentTimestamp' : parentTimestamp, 
                                            'replies' : replies})
                
                else:
                    # If there are no replies, skip replies
                    parent_comments.append({'parentAuthor' : parentAuthor,
                                            'parentId' : parentId,
                                            'parentText' : parentText,
                                            'parentTimestamp' : parentTimestamp})

            video_comments.append({'video_id' : video_id,
                                   'videoTitle' : videoTitle,
                                   'videoTimestamp' : videoTimestamp,
                                   'viewCount' : viewCount,
                                   'likeCount' : likeCount,
                                   'commentCount' : commentCount,
                                   'videoAuthor' : videoAuthor,
                                   'parent_comments' : parent_comments})

        else:
            # If there are no comments, skip comments
            video_comments.append({'video_id' : video_id,
                                   'videoTitle' : videoTitle,
                                   'videoTimestamp' : videoTimestamp,
                                   'viewCount' : viewCount,
                                   'likeCount' : likeCount,
                                   'commentCount' : commentCount,
                                   'videoAuthor' : videoAuthor})

    return json.dumps(video_comments)
