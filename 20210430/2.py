import re
def solution(word, pages):
answer = 0
meta_parser = re.compile('<meta(.+?)/>')
a_parser = re.compile('<a(.+?)>')
page_infos = []
for page in pages:
page_dict = dict()
a_tags = a_parser.findall(page)
outer_url = []
for a_tag in a_tags:
first_idx = end_idx = -1
for idx, char in enumerate(a_tag):
if char == '"':
if first_idx == -1:
first_idx = idx
elif end_idx == -1:
end_idx = idx
outer_url.append(a_tag[first_idx+1:end_idx])
meta_tag = meta_parser.search(page).group()
content_prop = meta_tag.split(' ')[2]
first_idx = end_idx = -1
for idx, char in enumerate(content_prop):
if char == '"':
if first_idx == -1:
first_idx = idx
elif end_idx == -1:
end_idx = idx
url = content_prop[first_idx+1: end_idx]
page_dict['outer_url_list'] = outer_url
page_dict['url'] = url
page_dict['keyword_point'] = re.sub('[^a-z]+', '.', page.lower()).split('.').count(word.lower())
page_dict['link_point'] = 0
page_infos.append(page_dict)
for page_info in page_infos:
for outer_url in page_info['outer_url_list']:
for outer_url_page_candidate in page_infos:
if outer_url == outer_url_page_candidate['url']:
outer_url_page_candidate['link_point'] += page_info['keyword_point']/len(page_info['outer_url_list'])
point_lst = [page_info['keyword_point'] + page_info['link_point'] for page_info in page_infos]
print(point_lst)
return point_lst.index(max(point_lst))

