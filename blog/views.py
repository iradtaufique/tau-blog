from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post, Comment
from blog.forms import CommentForm


def blogListView(request):
    all_post = Post.objects.all()
    context = {
        'all_post': all_post,
        # 'recents': recent_post,
    }
    return render(request, 'blog/blog_list.html', context)


def post_details(request, pk):
    single_post = get_object_or_404(Post, pk=pk)

    comments = single_post.comments.filter(active=True).order_by('-created')
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
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    context = {
        'single_post': single_post,
        'comment_form': comment_form,
        'new_comment': new_comment,
        'comments': comments
    }
    return render(request, 'blog/post_details.html', context)

def financial_posts(request):
    data = Post.objects.filter(post_category='Finance')
    context = {'data': data}
    return render(request, 'blog/post_categories.html', context)


def business_posts(request):
    data = Post.objects.filter(post_category='Business')
    context = {'data': data}
    return render(request, 'blog/post_categories.html', context)


def travels_posts(request):
    data = Post.objects.filter(post_category='Travel')
    context = {'data': data}
    return render(request, 'blog/post_categories.html', context)


def technology_posts(request):
    data = Post.objects.filter(post_category='Technology')
    context = {'data': data}
    return render(request, 'blog/post_categories.html', context)


def update_comment(request, id):
    data = Comment.objects.get(id=id)
    form = CommentForm(request.POST or None, instance=data)
    if request.method == 'POST':
        form = CommentForm(request.POST or None, instance=data)
        if form.is_valid():
            form.save()
            # post_id = Comment.objects.get(post_id=id).id
            # post_id = Post.objects.get(id=id).id
            # return redirect('post_details', post_id)
            return redirect('blog_list')
    context = {
        'form': form
    }
    return render(request, 'blog/edit_comment.html', context)


def delete_comment(request, id):
    obj = Comment.objects.get(id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('blog_list')
    return render(request, 'comment/delete_comment.html', {})