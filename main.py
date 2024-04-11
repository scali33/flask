from flask import Flask, render_template,request,redirect,url_for
from db.dbManeger import DataBase
app = Flask(__name__)


db = DataBase()

@app.route('/')
def home():
    return render_template('home.jinja2',posts=db.post_lsit())

@app.route('/post/<int:post_id>')
def poste(post_id):
    post = db.retrive_one_post(post_id)
    if not post:
        return render_template('404.jinja2',message='a post with an id non existence')
    return render_template('blog_posts.jinja2', post=post)

@app.route('/post/create', methods=['GET','POST'])
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        post_id = db.instert_post(title,content)
        return redirect(url_for('poste',post_id=post_id))
    return render_template('create.jinja2')

@app.route('/post/edit/<int:post_id>',methods=['GET','POST'])
def edit_post(post_id):
    post = db.retrive_one_post(post_id)
    if not post:
        return render_template('404.jinja2',message='a post with an id non existence')
    if request.method == 'GET':
        return render_template('edit.jinja2',post=post)
    elif request.method == 'POST':
        content = request.form.get('texto')
        title = request.form.get('title')
        db.save_post(content,post_id,title)
        return redirect(url_for('poste',post_id = post_id))
    
@app.route('/post/dell/<int:post_id>',methods=['GET'])
def delet_post(post_id):
    if not post_id:
        return render_template('404.jinja2',message='Post to delete not found')
    else:
        db.delete_post(post_id)
        return redirect(url_for('home'))
if __name__ == '__main__':
     app.run(debug=True)