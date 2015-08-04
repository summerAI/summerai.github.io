import yaml

ORDER = 999
BOOK_PATH = 'books/'
POSTS = []


def preBuild(site):
    global POSTS
    print "BUILDING BOOKS"
    # Build all the posts
    for page in site.pages():
        if page.path.startswith(BOOK_PATH):
            with open(page.full_source_path) as f:
                POSTS.append(yaml.load(f))


def preBuildPage(site, page, context, data):
    """
    Add the list of posts to every page context so we can
    access them from wherever on the site.
    """
    shelves = set(post['shelf'] for post in POSTS)
    context['books'] = {shelf: [post for post in POSTS if post['shelf'] == shelf] for shelf in shelves}

    for post in POSTS:
        context.update(post)

    return context, data
