from django.shortcuts import render, get_object_or_404
from blog.models import Post
from blog.forms import CommentForm


def blogListView(request):
    all_post = Post.objects.all()
    context = {
        'all_post': all_post
    }
    return render(request, 'blog/blog_list.html', context)


def post_details(request, pk):
    single_post = get_object_or_404(Post, pk=pk)

    comments = single_post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            print(comment_form.cleaned_data)
            new_comment = comment_form.save(commit=False)
            """assign comment to post"""
            new_comment.post = single_post
            """save the post"""
            # print(new_comment.post)
            new_comment.save()


    else:
        comment_form = CommentForm()

    context = {
        'single_post': single_post,
        'comment_form': comment_form,
        'new_comment': new_comment,
        'comments': comments
    }
    return render(request, 'blog/post_details.html', context)


# def post_detail(request, id):
#
#     single_post = get_object_or_404(Post, id=id)
#
#     """ list of similar posts"""
#     # # list IDs for the tags of the current post
#     # post_tags_ids = post.tags.values_list('id', flat=True)
#     # # get all posts that contain any of these tags, excluding the current post itself.
#     # similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
#     # similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4]
#
#     """list of active comments for this post"""
#     comments = single_post.comments.filter(active=True)
#     """new_comment variable for creating new comment to post"""
#     new_comment = None
#     if request.method == 'POST':
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#             """create a comment object but don't save to DB"""
#             new_comment = comment_form.save(commit=False)
#             """assign the current post to the comment"""
#             new_comment.single_post = single_post
#             """Save the comment to DB"""
#             new_comment.save()
#     else:
#         comment_form = CommentForm()
#     return render(request, 'blog/post_details.html', {'single_post': single_post,
#                                                      'comments': comments,
#                                                      'new_comment': new_comment,
#                                                      'comment_form': comment_form,
#                                                })