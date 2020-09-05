"""

problem link : https://programmers.co.kr/learn/courses/30/lessons/42893?language=python3

"""

import re


def solution(word, pages):
    word = word.lower()

    url_idx_dict = {}  # key: url, value: url's index
    basic_score_dict = {}  # key: url, value: basic score
    link_dict = {}  # key: url, value: link's index

    for idx, page in enumerate(pages):

        # 1. calculate basic score
        basic_score = 0
        texts = re.split('[^a-zA-Z]', "".join(page))
        for text in texts:
            if text.lower() == word:
                basic_score += 1

        # 2. find url
        meta = re.findall("(\<meta property=[^>]+[\>])", page)[0]
        url = meta.replace('<meta property="og:url" content=', "").replace("/>", "").replace('"', '')

        # 3. find links
        links = re.findall("(\<a href=[^>]+[\>])", page)
        refined_links = [l.replace("<a href=", "").replace(">", "").replace('"', '')
                         for l in links]

        url_idx_dict[url] = idx
        basic_score_dict[url] = basic_score
        link_dict[url] = refined_links

    ans = []

    for url in url_idx_dict:

        idx = url_idx_dict[url]
        # 1. 해당 페이지의 기본 점수
        basic_score = basic_score_dict[url]
        # 2. 링크 점수
        link_score = 0
        for k, bs in basic_score_dict.items():
            if k != url and url in link_dict[k]:
                link_score += bs / len(link_dict[k])
        # 3. 매칭 점수 = 기본 점수 + 링크 점수
        match_score = basic_score + link_score
        ans.append((idx, match_score))

    return max(ans, key=lambda x: x[1])[0]
