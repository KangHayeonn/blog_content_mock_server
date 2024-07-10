from flask import Flask, request, jsonify
import pandas as pd
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # CORS 활성화
DATA_FILE = 'blog_data.pkl'

# 데이터 파일이 존재하지 않으면 초기화
if not os.path.exists(DATA_FILE):
    df = pd.DataFrame(columns=['article_id', 'title', 'content', 'writer', 'create_date'])
    df.to_pickle(DATA_FILE)


def load_data():
    return pd.read_pickle(DATA_FILE)


def save_data(df):
    df.to_pickle(DATA_FILE)


@app.route('/api/articles', methods=['POST'])
def create_article():
    data = request.json
    df = load_data()
    new_id = df['article_id'].max() + 1 if not df.empty else 1
    data['article_id'] = new_id
    df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
    save_data(df)
    return jsonify(data), 201


@app.route('/api/articles', methods=['GET'])
def get_articles():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    df = load_data()
    total_articles = len(df)
    total_pages = (total_articles + per_page - 1) // per_page

    if page > total_pages or page < 1:
        return jsonify({"error": "Invalid page number"}), 400

    start_idx = (page - 1) * per_page
    end_idx = start_idx + per_page
    articles = df.iloc[start_idx:end_idx].to_dict(orient='records')

    return jsonify({
        'page': page,
        'per_page': per_page,
        'total_articles': total_articles,
        'total_pages': total_pages,
        'articles': articles
    })


@app.route('/api/articles/<int:article_id>', methods=['DELETE'])
def delete_article(article_id):
    df = load_data()
    if article_id not in df['article_id'].values:
        return jsonify({"error": "Article not found"}), 404

    df = df[df['article_id'] != article_id]
    save_data(df)
    return jsonify({"message": "Article deleted"}), 200


if __name__ == '__main__':
    app.run(debug=True)
