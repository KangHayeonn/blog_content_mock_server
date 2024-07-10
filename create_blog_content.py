import pandas as pd
import os

# 예시 블로그 글 데이터 생성
data = [
    {"article_id": 1, "title": "Python으로 데이터 분석 시작하기", "content": "Python은 데이터 분석에 매우 유용한 도구입니다. 이번 글에서는 pandas 라이브러리를 사용하여 데이터를 분석하는 방법을 알아보겠습니다.", "writer": "홍길동", "create_date": "2024-01-01"},
    {"article_id": 2, "title": "JavaScript 비동기 처리 이해하기", "content": "JavaScript의 비동기 처리는 매우 중요합니다. 이번 글에서는 콜백 함수, 프로미스, 그리고 async/await를 사용하여 비동기 처리를 이해해보겠습니다.", "writer": "이몽룡", "create_date": "2024-01-02"},
    {"article_id": 3, "title": "React로 간단한 웹 애플리케이션 만들기", "content": "React는 현대 웹 개발에서 중요한 역할을 합니다. 이번 글에서는 React를 사용하여 간단한 웹 애플리케이션을 만드는 방법을 알아보겠습니다.", "writer": "성춘향", "create_date": "2024-01-03"},
    {"article_id": 4, "title": "CSS Grid를 활용한 레이아웃 디자인", "content": "CSS Grid는 복잡한 레이아웃을 쉽게 만들 수 있는 도구입니다. 이번 글에서는 CSS Grid를 사용하여 다양한 레이아웃을 디자인해보겠습니다.", "writer": "변학도", "create_date": "2024-01-04"},
    {"article_id": 5, "title": "Python으로 웹 스크래핑 하기", "content": "Python의 BeautifulSoup 라이브러리를 사용하여 웹 페이지의 데이터를 추출하는 방법을 알아보겠습니다. 웹 스크래핑을 통해 다양한 데이터를 수집할 수 있습니다.", "writer": "방자", "create_date": "2024-01-05"},
    {"article_id": 6, "title": "Docker를 사용한 애플리케이션 배포", "content": "Docker는 애플리케이션을 배포하고 실행하는 데 매우 유용한 도구입니다. 이번 글에서는 Docker를 사용하여 애플리케이션을 배포하는 방법을 알아보겠습니다.", "writer": "임꺽정", "create_date": "2024-01-06"},
    {"article_id": 7, "title": "머신러닝 기본 개념 정리", "content": "머신러닝은 인공지능의 한 분야로, 데이터를 통해 학습하고 예측하는 기술입니다. 이번 글에서는 머신러닝의 기본 개념을 정리해보겠습니다.", "writer": "김삿갓", "create_date": "2024-01-07"},
    {"article_id": 8, "title": "HTML5 새로운 기능 소개", "content": "HTML5는 웹 개발에 많은 새로운 기능을 추가했습니다. 이번 글에서는 HTML5의 주요 기능과 이를 활용하는 방법을 알아보겠습니다.", "writer": "홍길순", "create_date": "2024-01-08"},
    {"article_id": 9, "title": "Node.js로 서버 만들기", "content": "Node.js는 JavaScript를 사용하여 서버 사이드 개발을 가능하게 합니다. 이번 글에서는 Node.js를 사용하여 간단한 서버를 만드는 방법을 알아보겠습니다.", "writer": "이방원", "create_date": "2024-01-09"},
    {"article_id": 10, "title": "Git과 GitHub을 활용한 협업", "content": "Git은 버전 관리 시스템으로, GitHub은 이를 이용한 협업 도구입니다. 이번 글에서는 Git과 GitHub을 사용하여 협업하는 방법을 알아보겠습니다.", "writer": "정도전", "create_date": "2024-01-10"},
    {"article_id": 11, "title": "Python으로 데이터 시각화하기", "content": "Python의 Matplotlib과 Seaborn 라이브러리를 사용하여 데이터를 시각화하는 방법을 알아보겠습니다. 시각화를 통해 데이터를 더 잘 이해할 수 있습니다.", "writer": "장보고", "create_date": "2024-01-11"},
    {"article_id": 12, "title": "CSS Flexbox를 활용한 반응형 디자인", "content": "CSS Flexbox는 반응형 웹 디자인을 쉽게 구현할 수 있는 도구입니다. 이번 글에서는 Flexbox를 사용하여 반응형 디자인을 만드는 방법을 알아보겠습니다.", "writer": "안중근", "create_date": "2024-01-12"},
    {"article_id": 13, "title": "Django로 블로그 만들기", "content": "Django는 Python 기반의 웹 프레임워크로, 강력한 기능을 제공합니다. 이번 글에서는 Django를 사용하여 블로그를 만드는 방법을 알아보겠습니다.", "writer": "윤봉길", "create_date": "2024-01-13"},
    {"article_id": 14, "title": "Java로 스프링 부트 애플리케이션 만들기", "content": "Spring Boot는 Java 기반의 프레임워크로, 빠르게 애플리케이션을 개발할 수 있게 도와줍니다. 이번 글에서는 Spring Boot를 사용하여 애플리케이션을 만드는 방법을 알아보겠습니다.", "writer": "이순신", "create_date": "2024-01-14"},
    {"article_id": 15, "title": "웹 성능 최적화 방법", "content": "웹 성능 최적화는 사용자 경험을 향상시키는 중요한 요소입니다. 이번 글에서는 웹 성능을 최적화하는 다양한 방법을 알아보겠습니다.", "writer": "김유신", "create_date": "2024-01-15"},
    {"article_id": 16, "title": "Vue.js로 프론트엔드 개발하기", "content": "Vue.js는 인기 있는 JavaScript 프레임워크로, 쉽고 빠르게 프론트엔드 개발을 할 수 있습니다. 이번 글에서는 Vue.js를 사용하여 프론트엔드 애플리케이션을 만드는 방법을 알아보겠습니다.", "writer": "최영", "create_date": "2024-01-16"},
    {"article_id": 17, "title": "Python과 Flask로 REST API 만들기", "content": "Flask는 Python 기반의 마이크로 웹 프레임워크로, 간단하게 REST API를 만들 수 있습니다. 이번 글에서는 Flask를 사용하여 REST API를 만드는 방법을 알아보겠습니다.", "writer": "강감찬", "create_date": "2024-01-17"},
    {"article_id": 18, "title": "Kubernetes로 애플리케이션 배포하기", "content": "Kubernetes는 컨테이너화된 애플리케이션을 관리하는 도구입니다. 이번 글에서는 Kubernetes를 사용하여 애플리케이션을 배포하는 방법을 알아보겠습니다.", "writer": "김구", "create_date": "2024-01-18"},
    {"article_id": 19, "title": "Python의 장고 ORM 이해하기", "content": "Django의 ORM(Object-Relational Mapping)은 데이터베이스와 상호작용을 쉽게 해줍니다. 이번 글에서는 Django ORM의 기본 개념을 알아보겠습니다.", "writer": "안창호", "create_date": "2024-01-19"},
    {"article_id": 20, "title": "AI와 머신러닝의 차이점", "content": "AI와 머신러닝은 서로 다른 개념입니다. 이번 글에서는 AI와 머신러닝의 차이점과 각 기술의 활용 사례를 알아보겠습니다.", "writer": "유관순", "create_date": "2024-01-20"}
]

# 데이터프레임 생성
df = pd.DataFrame(data)

# 데이터 저장
DATA_FILE = 'blog_data.pkl'
df.to_pickle(DATA_FILE)

print(f"데이터가 {DATA_FILE} 파일에 저장되었습니다.")
