from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Nancy Luo! I am adding my first code change.'

@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.route('/about')
def about():
    course = request.args.get('course')
    grade=request.args.get('grade')
    return render_template('about.html',course=course,grade=grade)

@app.route('/favorite_course')
def favorite_course():
    subject=request.args.get('subject')
    course_number=request.args.get('course_number')
    return render_template('favorite_course.html',subject=subject,course_number=course_number)

@app.route('/contact',methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        return render_template('contact.html',form_submitted=True)
    else:
        return render_template('contact.html')



@app.route('/about-css')
def aboutcss():
    return render_template('about-css.html')

if __name__ == '__main__':
    app.run()
