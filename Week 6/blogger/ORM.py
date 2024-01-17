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
    posts_to_update = Post.objects.filter(title=post_title)
    
    if posts_to_update.count() == 1:
        post_to_update = posts_to_update.first()
        post_to_update.body = new_content
        post_to_update.save()
    elif posts_to_update.count() > 1:
        print(f"Warning: Multiple posts found with title '{post_title}'. Skipping update.")
    else:
        print(f"Error: No posts found with title '{post_title}'. Update failed.")



def delete_post(post_title):
    posts_to_delete = Post.objects.filter(title=post_title)

    if posts_to_delete.exists():
        posts_to_delete.delete()
        print(f"Deleted posts with title '{post_title}'.")
    else:
        print(f"No posts found with title '{post_title}'. Delete failed.")




def create_comments():
    # Create at least 3 comments related to different blog posts
    posts = Post.objects.filter(title='Post 1')

    for post in posts:
        comment_data = {'user': 'User 1', 'content': f'Comment for {post.title}', 'post': post}
        Comment.objects.create(**comment_data)

    print("Comments created successfully.")


def query_and_display_comments(post_title):
    post_comments = Comment.objects.filter(post__title=post_title)
    print(f"Comments for {post_title}:")
    for comment in post_comments:
        print(comment.content)
    print()

def update_comment_content(comment_content, new_content):
    comments_to_update = Comment.objects.filter(content=comment_content)
    
    for comment in comments_to_update:
        comment.content = new_content
        comment.save()
    
    print(f"Updated content for comments with content '{comment_content}'.")



def delete_comment(comment_content):
    try:
        comment_to_delete = Comment.objects.get(content=comment_content)
        comment_to_delete.delete()
        print(f"Deleted comment with content '{comment_content}'.")
    except Comment.DoesNotExist:
        print(f"Comment with content '{comment_content}' does not exist. Delete failed.")



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

