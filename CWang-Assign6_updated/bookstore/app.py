from flask import Flask, render_template, request

app = Flask(__name__)

# Categories

categories = [
    {"id": 1, "name": "A Dream of Red Mansions", "image": "hongloumeng.png"},
    {"id": 2, "name": "Three Kingdoms", "image": "sanguoyanyi.png"},
    {"id": 3, "name": "Journey to the West", "image": "xiyouji.png"},
    {"id": 4, "name": "Outlaws of the Marsh", "image": "shuihuzhuan.png"},
]

# Books 

books = [

    {"id": 1, "categoryId": 1, "title": "A Dream of Red Mansions Volume I", "author": "Cao Xueqin",
     "isbn": "978-7-5399-001-1", "price": 8.88, "image": "hlm1.jpg", "readNow": 1},

    {"id": 2, "categoryId": 1, "title": "A Dream of Red Mansions Volume II", "author": "Cao Xueqin",
     "isbn": "978-7-5399-002-8", "price": 8.88, "image": "hlm2.jpg", "readNow": 0},

    {"id": 3, "categoryId": 1, "title": "A Dream of Red Mansions Volume III", "author": "Cao Xueqin",
     "isbn": "978-7-5399-003-5", "price": 8.88, "image": "hlm3.jpg", "readNow": 1},

    {"id": 4, "categoryId": 1, "title": "A Dream of Red Mansions Volume IV", "author": "Cao Xueqin",
     "isbn": "978-7-5399-004-2", "price": 8.88, "image": "hlm4.jpg", "readNow": 1},

    {"id": 5, "categoryId": 2, "title": "Three Kingdoms Volume I", "author": "Luo Guanzhong",
     "isbn": "978-7-5321-101-9", "price": 5.26, "image": "sgyy1.jpg", "readNow": 0},

    {"id": 6, "categoryId": 2, "title": "Three Kingdoms Volume II", "author": "Luo Guanzhong",
     "isbn": "978-7-5321-102-6", "price": 5.26, "image": "sgyy2.jpg", "readNow": 0},

    {"id": 7, "categoryId": 2, "title": "Three Kingdoms Volume III", "author": "Luo Guanzhong",
     "isbn": "978-7-5321-103-3", "price": 5.26, "image": "sgyy3.jpg", "readNow": 0},

    {"id": 8, "categoryId": 2, "title": "Three Kingdoms Volume IV", "author": "Luo Guanzhong",
     "isbn": "978-7-5321-104-0", "price": 5.26, "image": "sgyy4.jpg", "readNow": 1},

    {"id": 9, "categoryId": 3, "title": "Journey to the West Volume I", "author": "Wu Cheng'en",
     "isbn": "978-7-5345-201-5", "price": 7.54, "image": "xyj1.jpg", "readNow": 0},

    {"id": 10, "categoryId": 3, "title": "Journey to the West Volume II", "author": "Wu Cheng'en",
     "isbn": "978-7-5345-202-2", "price": 7.54, "image": "xyj2.jpg", "readNow": 1},

    {"id": 11, "categoryId": 3, "title": "Journey to the West Volume III", "author": "Wu Cheng'en",
     "isbn": "978-7-5345-203-9", "price": 7.54, "image": "xyj3.jpg", "readNow": 1},

    {"id": 12, "categoryId": 3, "title": "Journey to the West Volume IV", "author": "Wu Cheng'en",
     "isbn": "978-7-5345-204-7", "price": 7.54, "image": "xyj4.jpg", "readNow": 0},

    {"id": 13, "categoryId": 4, "title": "Outlaws of the Marsh Volume I", "author": "Shi Nai'an",
     "isbn": "978-7-5375-301-2", "price": 4.24, "image": "shz1.jpg", "readNow": 1},

    {"id": 14, "categoryId": 4, "title": "Outlaws of the Marsh Volume II", "author": "Shi Nai'an",
     "isbn": "978-7-5375-302-5", "price": 4.24, "image": "shz2.jpeg", "readNow": 0},

    {"id": 15, "categoryId": 4, "title": "Outlaws of the Marsh Volume III", "author": "Shi Nai'an",
     "isbn": "978-7-5375-303-8", "price": 4.24, "image": "shz3.jpg", "readNow": 0},

    {"id": 16, "categoryId": 4, "title": "Outlaws of the Marsh Volume IV", "author": "Shi Nai'an",
     "isbn": "978-7-5375-304-1", "price": 4.24, "image": "shz4.png", "readNow": 1},
]

# Home page

@app.route('/')
def home():
    return render_template("index.html", categories=categories)

# Category Page

@app.route('/category')
def category():
    category_id = request.args.get("categoryId", type=int)
    selected_books = [b for b in books if b["categoryId"] == category_id]

    return render_template(
        "category.html",
        categories=categories,
        selectedCategory=category_id,
        books=selected_books
    )

# Search Page 

@app.route('/search')
def search():
    return render_template("search.html")
    
# Error Page

@app.errorhandler(Exception)
def handle_error(e):
    return render_template("error.html", error=e)

# ---------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)

