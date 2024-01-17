import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogger.settings')  
django.setup()

from blog.models import Post
from comment.models import Comment  

def create_posts():
    posts_data = [
        {'title': 'Post 1', 'slug': 'post-1', 'body': 'Content for Post 1'},
        {'title': 'Post 2', 'slug': 'post-2', 'body': 'Content for Post 2'},
        {'title': 'Post 3', 'slug': 'post-3', 'body': 'Content for Post 3'},
    ]

    for data in posts_data:
        Post.objects.create(**data)


def query_and_display_posts(title_or_slug):
    posts_with_title_or_slug = Post.objects.filter(title=title_or_slug) | Post.objects.filter(slug=title_or_slug)
    print(f"Posts with title or slug '{title_or_slug}':")
    for post in posts_with_title_or_slug:
        print(f"{post.title}: {post.body}")
    print()



def update_post_content(post_title, new_content):
    post_to_update = Post.objects.get(title=post_title)
    post_to_update.body = new_content
    post_to_update.save()


def delete_post(post_title):
    Post.objects.get(title=post_title).delete()


def create_comments():
    comments_data = [
        {'user': 'User 1', 'content': 'Comment for Post 1', 'post': Post.objects.get(title='Post 1')},
        {'user': 'User 2', 'content': 'Comment for Post 2', 'post': Post.objects.get(title='Post 2')},
        {'user': 'User 3', 'content': 'Comment for Post 3', 'post': Post.objects.get(title='Post 3')},
    ]

    for data in comments_data:
        Comment.objects.create(**data)


def query_and_display_comments(post_title):
    post_comments = Comment.objects.filter(post__title=post_title)
    print(f"Comments for {post_title}:")
    for comment in post_comments:
        print(comment.content)
    print()


def update_comment_content(comment_content, new_content):
    comment_to_update = Comment.objects.get(content=comment_content)
    comment_to_update.content = new_content
    comment_to_update.save()


def delete_comment(comment_content):
    Comment.objects.get(content=comment_content).delete()


if __name__ == '__main__':
    create_posts()
    query_and_display_posts('Post 1')  
    update_post_content('Post 1', 'Updated content for Post 1')
    query_and_display_posts('Post 1')
    delete_post('Post 2')
    query_and_display_posts('Post 2')  
    create_comments()
    query_and_display_comments('Post 1')
    update_comment_content('Comment for Post 1', 'Updated comment for Post 1')
    query_and_display_comments('Post 1')
    delete_comment('Comment for Post 2')
    query_and_display_comments('Post 2')  

