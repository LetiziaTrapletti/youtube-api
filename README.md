Youtube API - Social Campaign Comments

I first created a project on Google Developers Console, then requested an authorization credential (API key). Afterwards, I enabled Youtube API for my application, so that I can send API requests to Youtube API services. Then, I went on Youtube and checked the video ID of each of the social media campaigns that I would like to include in my research scope (using their URLs). Then I created the function for getting the video statistics and comments via the API: the function returns the data in json format.

Note:
* This API gets top level comments from all videos with given IDs (only the first 10 comments due to quote limit of Youtube API).
* This API gets replies for all top level comments (only the first 10 replies due to quote limit of Youtube API).

Params:
youtube: the build object from googleapiclient.discovery
video_ids: list of video IDs

Returns:
Json document with (i) video IDs, (ii) associated video statistics, (iii) top level comments in json (up to 10), and (iv) replies to top level comments (up to 10).