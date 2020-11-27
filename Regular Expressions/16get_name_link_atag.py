import re
n = int(input())
link_pattern = r'<a href="(.+?)".*?>([^<>]*)</'
for _ in range(n):
    m = re.findall(link_pattern, input())
    print(m)
    for link, title in m:
        print(link, title)
        print(f'{link},{title.strip()}')

'''
2
<p><a href="http://www.quackit.com/html/tutorial/html_links.cfm">Example Link</a></p>
<div class="more-info"><a href="http://www.quackit.com/html/examples/html_links_examples.cfm">More Link Examples...</a></div>

'''