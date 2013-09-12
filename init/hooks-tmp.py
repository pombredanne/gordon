from github import Github as git
from web.config import properties

def auth_git():
    return git(properties.get('GITHUB_USERNAME'), properties.get('GITHUB_PASSWORD'), timeout=3000)

g = auth_git()
docker_repo = g.get_repo("keeb/docker-build")
hooks = ['push', 'issues', 'issue_comment', 'commit_comment', 'pull_request',
        'pull_request_review_comment', 'watch', 'fork', 'fork_apply']
config = {'url': 'http://stinemat.es:5000', 'content_type': 'json'}

docker_repo.create_hook('web', config, hooks, True)

