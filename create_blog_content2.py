import pandas as pd
import os

# 기존 데이터 불러오기
DATA_FILE = 'blog_data.pkl'
if os.path.exists(DATA_FILE):
    df = pd.read_pickle(DATA_FILE)
else:
    df = pd.DataFrame(columns=['article_id', 'title', 'content', 'writer', 'create_date'])

# 새로운 예시 블로그 글 데이터 생성
new_data = [
    {"article_id": df['article_id'].max() + i + 1 if not df.empty else i + 1, "title": f"새로운 블로그 글 {i+1}",
     "content": f"이것은 {i+1}번째 새로운 블로그 글 내용입니다. 다양한 주제를 다루고 있습니다.",
     "writer": f"작성자{i+21}", "create_date": f"2024-02-{i+1:02d}"}
    for i in range(20)
]

# 데이터프레임으로 변환
new_df = pd.DataFrame(new_data)

# 기존 데이터에 새로운 데이터 추가
df = pd.concat([df, new_df], ignore_index=True)

# 데이터 저장
df.to_pickle(DATA_FILE)

print(f"새로운 데이터가 {DATA_FILE} 파일에 추가 저장되었습니다.")
