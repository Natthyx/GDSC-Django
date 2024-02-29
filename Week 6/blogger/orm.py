import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogger.settings')  
django.setup()

from blog.models import Post
from comment.models import Comment  

def create_posts():
    post1 = Post.objects.create(title='Post 1', content='Content 1', category='Category 1', tags='tag1, tag2')
    post2 = Post.objects.create(title='Post 2', content='Content 2', category='Category 2', tags='tag2, tag3')
    post3 = Post.objects.create(title='Post 3', content='Content 3', category='Category 1', tags='tag1, tag3')
    print('Posts created successfully.')

def query_posts_by_category(category):
    posts = Post.objects.filter(category=category)
    print(f'Posts in category "{category}":')
    for post in posts:
        print(f'{post.title} - {post.content}')

def update_post_content(post_id, new_content):
    post = Post.objects.get(id=post_id)
    post.content = new_content
    post.save()
    print(f'Content of Post {post_id} updated successfully.')

def delete_post(post_id):
    Post.objects.get(id=post_id).delete()
    print(f'Post {post_id} deleted successfully.')

def create_comments():
    comment1 = Comment.objects.create(content='Comment 1', author='Author 1', published_date='2024-02-29 12:00:00', post_id=1)
    comment2 = Comment.objects.create(content='Comment 2', author='Author 2', published_date='2024-02-29 12:30:00', post_id=2)
    comment3 = Comment.objects.create(content='Comment 3', author='Author 3', published_date='2024-02-29 13:00:00', post_id=3)
    print('Comments created successfully.')

def query_comments_by_post(post_id):
    comments = Comment.objects.filter(post_id=post_id)
    print(f'Comments for Post {post_id}:')
    for comment in comments:
        print(f'{comment.author} - {comment.content}')

def update_comment_content(comment_id, new_content):
    comment = Comment.objects.get(id=comment_id)
    comment.content = new_content
    comment.save()
    print(f'Content of Comment {comment_id} updated successfully.')

def delete_comment(comment_id):
    Comment.objects.get(id=comment_id).delete()
    print(f'Comment {comment_id} deleted successfully.')

if __name__ == '__main__':
    create_posts()
    query_posts_by_category('Category 1')
    update_post_content(1, 'Updated content for Post 1')
    delete_post(2)
    create_comments()
    query_comments_by_post(1)
    update_comment_content(2, 'Updated content for Comment 2')
    delete_comment(3)
