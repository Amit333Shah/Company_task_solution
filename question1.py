import requests
import json


def task():
    #     fetching data from api using requests api
    posts_res = requests.get("https://my-json-server.typicode.com/typicode/demo/posts")
    comment_res = requests.get("https://my-json-server.typicode.com/typicode/demo/comments")
    #     fetching ends

    # converting data to required format
    result_data = []
    for post in posts_res.json():
        tmp_comments = []
        for comment in comment_res.json():
            if int(post['id']) == int(comment['postId']):
                tmp_comments.append(comment)
        post['comments'] = tmp_comments
        result_data.append(post)

        #         returning result
        return json.dumps(result_data)


result = task()

print(result)