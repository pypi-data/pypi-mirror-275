import requests
from bs4 import BeautifulSoup
from datetime import datetime

def Convert_URL(url):
    # HTTPリクエストを送信してページの内容を取得
    response = requests.get(url)
    response.raise_for_status()  # リクエストが成功したかどうかをチェック

    # BeautifulSoupを使用してページを解析
    soup = BeautifulSoup(response.content, 'html.parser')

    # 著者名を取得（metaタグから取得）
    author_name = None
    for meta in soup.find_all('meta'):
        if 'name' in meta.attrs and meta.attrs['name'] == 'author':
            author_name = meta.attrs['content']
            break
    if author_name is None:
        author_name = 'No author found'

    # ページ名を取得し、ダブルクォーテーションで囲む
    page_name = f'"{soup.title.string}"' if soup.title else 'No title found'

    # サイト名を取得（metaタグから取得）
    site_name = None
    for meta in soup.find_all('meta'):
        if 'property' in meta.attrs and meta.attrs['property'] == 'og:site_name':
            site_name = meta.attrs['content']
            break
    if site_name is None:
        site_name = 'No site name found'

    # 更新日を取得（metaタグ・timeタグから取得）
    update_date = None
    for meta in soup.find_all('meta'):
        if 'name' in meta.attrs and meta.attrs['name'] in ['last-modified', 'updated', 'date']:
            update_date = meta.attrs['content']
            update_date = update_date[:4]
            break
    if update_date is None:
        for time_tag in soup.find_all('time'):
            if 'datetime' in time_tag.attrs:
                update_date = time_tag.attrs['datetime']
                update_date = update_date[:4]
                break
    if update_date is None:
        update_date = 'No update date found'

    # コード実行時の日時を取得
    current_date = datetime.now().strftime('%Y-%m-%d')  # 年月日のみを取得

    output = author_name+"．"+page_name+"．"+site_name+"．"+update_date+"．"+url +",（参照"+current_date+"）"

    return output