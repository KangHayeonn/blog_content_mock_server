# blog_content_mock_server

이 프로젝트는 Flask를 사용하여 간단한 블로그 글 작성 및 조회 API를 제공합니다. 데이터는 로컬 파일에 저장되며, CORS를 지원합니다.

## 요구 사항

- Python 3.x
- Flask
- pandas
- Flask-CORS

## 설치 방법

1. 프로젝트를 클론하거나 다운로드합니다.
```bash
 git clone https://github.com/SoNgSeUNgMiN96/blog_content_mock_server.git
 cd blog_content_mock_server
```

2. 필요한 모듈을 개별로 설치합니다.
``` bash
pip install flask
pip install pandas
pip install flask_cors
```

### API 종류 및 호출법
* 글 작성 (POST /api/articles)
  * URL: http://localhost:5000/api/articles
  * Method: POST
  * Body: JSON 형식 (raw)
```json
{
    "title": "Sample Title",
    "content": "This is the content of the article.",
    "writer": "Author Name",
    "create_date": "2024-07-10"
}
```

* 글 조회 (GET /api/articles)
  * URL: http://localhost:5000/api/articles?page=1&per_page=10
  * Method: GET
* 글 삭제 (DELETE /api/articles/<article_id>)
  * URL: http://localhost:5000/api/articles/1 (1은 삭제할 article_id입니다)
  * Method: DELETE

## 실행 방법
1. main.py 파일을 실행합니다.
```bash
python main.py 
```

