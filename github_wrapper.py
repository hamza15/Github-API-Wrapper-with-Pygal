import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

#Make an API call and store the response.
url = 'https://api.github.com/users/hamza15/repos?q=language:python&sort=stars'
r = requests.get(url)
print "Status code:", r.status_code

#Store API response in a variable.
response_dict = r.json()

names, stars = [], []
for repo_dict in response_dict:
	names.append(repo_dict['name'])
	stars.append(repo_dict['stargazers_count'])

#Make visualization
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = "Hamza's Python Projects on GitHub"
chart.x_labels = names
chart.add('', stars)
chart.render_to_file('python_repos.svg')
