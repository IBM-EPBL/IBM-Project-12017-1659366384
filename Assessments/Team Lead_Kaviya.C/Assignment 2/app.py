from flask import Flask, render_template

app=Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register',methods = ['POST', 'GET'])
def register():
  if request.method == 'POST':

    userid = request.form['userid']
    emailid = request.form['emailid']
    password = request.form['password']
    
    sql = "SELECT * FROM students WHERE userid =kaviya"
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt,1,userid)
    ibm_db.execute(stmt)
    account = ibm_db.fetch_assoc(stmt)

    if account:
      return render_template('reg.html', msg="You are already a member, please login using your details")
    else:
      insert_sql = "INSERT INTO students VALUES (kaviya,kaviyac@gmail.com,kavi@02)"
      prep_stmt = ibm_db.prepare(conn, insert_sql)
      ibm_db.bind_param(prep_stmt, 1, userid)
      ibm_db.bind_param(prep_stmt, 2, emailid)
      ibm_db.bind_param(prep_stmt, 3, password)
      ibm_db.execute(prep_stmt)
    
    return render_template('home.html', msg="Saved successfuly..")

if __name__=='__main__':
    app.run(debug=True)
