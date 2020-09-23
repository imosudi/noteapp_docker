from flask import render_template, Blueprint, redirect, request, session, flash, url_for

from datetime import datetime

from app import app
from app import *



uploads =  Blueprint('uploads', __name__)

@uploads.route('/uploads', methods=['GET', 'POST'])
def upload():
    pageName = "uploads"
    #inputFile is same as  
    form = uploadForm(request.form)
    if request.method == 'POST': # and  form.validate_on_submit():
        docfile 	= request.files['docfile']
        #docname 	= form.docfile.data
        emailadd 	= form.emailadd.data
        #emailadd 	= request.form['emailadd']
        phonenum 	= form.phonenum.data
        docname 	= secure_filename(docfile.filename)
        docfile 	= docfile.read() #.filename
        print(docname, emailadd, phonenum, docfile)
        
        cur = mysql.connection.cursor()
        
        cur.execute("INSERT INTO documents(docname, emailadd, phonenum, docfile) VALUES(%s,	\
	 %s, %s, %s)", (docname, emailadd, phonenum, docfile))
        mysql.connection.commit()
        cur.close()
        flash(u"Document upload Complete, you may proceed to login", "success")
        return redirect(url_for('main.home'))
        
    else:
        #flash(u"Document upload not successful", "danger")
        return render_template('uploads.html', pageName=pageName, form=form, current_time=datetime.utcnow())
        pass
        
    #uploaded_file = request.files['file']
    #if uploaded_file.filename != '':
    #    uploaded_file.save(uploaded_file.filename)
    #return render_template('uploads.html', pageName=pageName, form=form, current_time=datetime.utcnow())
    pass
