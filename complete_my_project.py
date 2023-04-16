import datetime
import random
from flask import Flask, render_template, request, redirect, session, jsonify
from DBConnection import *

import time,datetime
from encodings.base64_codec import base64_decode
import base64


app = Flask(__name__)
app.secret_key="ajvdj"


@app.route('/')
def login():
    return render_template("loginindex.html")

@app.route('/login_post',methods=['post'])
def login_post():
    User_name=request.form['textfield']
    password=request.form['textfield2']
    db=Db()
    qry="select * from login where username='"+User_name+"' and password='"+password+"'"
    res=db.selectOne(qry)
    if res is not None:
        session['lid']=res['login_id']
        session['log']="lin"
        if res['user_type']=='admin':
            return redirect('/Admin_Home')
        elif res['user_type']=='internal_guide':
            return redirect('/internal_home')
        elif res['user_type']=='external_organization':
            return redirect('/external_home')
        else:
            return '''<script>alert('user not found');window.location="/"</script>'''
    else:
        return '''<script>alert('user not found');window.location="/"</script>'''

###################################################################### Admin  home ##############################

@app.route('/Admin_Home')
def Admin_Home():
    if session['log']=="lin":
        return render_template("admin/adminindex.html")
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''


@app.route('/logout')
def logout():
    session['log']=""
    return '''<script>alert('You Are Loged Out');window.location="/"</script>'''


########################################################################### internal ###################################


@app.route('/internal_add')
def internal_add():
    if session['log']=="lin":
        return render_template("admin/internal_add.html")
    else:
        return  '''<script>alert('You Are Loged Out');window.location="/"</script>'''



@app.route('/internal_add_post',methods=['post'])
def internal_add_post():
    if session['log'] == "lin":
        name=request.form['textfield']
        email=request.form['textfield2']
        phone=request.form['textfield3']
        place=request.form['textfield4']
        dob=request.form['textfield5']
        gender=request.form['RadioGroup1']
        photo=request.files['fileField']
        date=datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        photo.save(r"E:\\project final\\web\\complete_my_project\\static\\internal_guide\\"+date+".jpg")
        path=("/static/internal_guide/"+date+".jpg")
        password=random.randint(0000,9999)
        db=Db()
        qry2="select * from login where `username`='"+email+"'"
        res2=db.selectOne(qry2)
        if res2 is  None:
            qry="INSERT INTO `login`(`username`,`password`,`user_type`) VALUES ('"+email+"','"+str(password)+"','internal_guide')"
            res=db.insert(qry)
            qry1="INSERT INTO `internal_guide` (`internal_name`,`email`,`phoneno`,`place`,`dob`,`gender`,`photo`,`lid`) VALUES('"+name+"','"+email+"','"+phone+"','"+place+"','"+dob+"','"+gender+"','"+str(path)+"','"+str(res)+"')"
            res1=db.insert(qry1)
            return '''<script>alert('Successfully Registered');window.location="/internal_view_admin"</script>'''
        else:
            return '''<script>alert('Allready Registered');window.location="/internal_view_admin"</script>'''
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''

@app.route('/internal_view_admin')
def internal_view_admin():
    if session['log'] == "lin":
        qry="select * from `internal_guide`"
        db=Db()
        res=db.select(qry)
        return render_template("admin/internal_view.html",data=res)
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''

@app.route('/search_internal_guide_view',methods=['post'])
def search_internal_guide_view():
    if session['log'] == "lin":
        search=request.form['textfield']
        qry = "select * from `internal_guide` where `internal_name` like '%"+search+"%'"
        db = Db()
        res = db.select(qry)
        return render_template("admin/internal_view.html", data=res)
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''


@app.route('/delete_internal_guide/<igid>')
def delete_internal_guide(igid):
    if session['log'] == "lin":
        db=Db()
        qry="delete from `internal_guide` where `internal_guide_id`='"+str(igid)+"'"
        res=db.delete(qry)
        return '''<script>alert('Successfully Deleted');window.location="/internal_view_admin"</script>'''
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''


@app.route('/edit_internal_guide/<igid>')
def edit_internal_guide(igid):
    if session['log'] == "lin":
        db=Db()
        qry="select * from `internal_guide` where `internal_guide_id`='"+str(igid)+"'"
        res=db.selectOne(qry)
        return render_template("admin/internal_edit.html",data=res)
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''


@app.route('/edit_internal_guide_post',methods=['post'])
def edit_internal_guide_post():
    if session['log'] == "lin":
        igid=request.form['igid']
        name = request.form['textfield']
        email = request.form['textfield2']
        phone = request.form['textfield3']
        place = request.form['textfield4']
        dob = request.form['textfield5']
        gender = request.form['RadioGroup1']
        photo = request.files['fileField']
        date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        photo.save(r"E:\\project final\\web\\complete_my_project\\static\\internal_guide\\" + date + ".jpg")
        path = ("/static/internal_guide/" + date + ".jpg")
        db=Db()
        if request.files!=None:
            if photo.filename!="":
                qry="UPDATE `internal_guide` SET `internal_name`='"+name+"',`email`='"+email+"',`phoneno`='"+phone+"',`place`='"+place+"',`dob`='"+dob+"',`gender`='"+gender+"',`photo`='"+str(path)+"' WHERE `internal_guide_id`='"+str(igid)+"'"
                res=db.update(qry)
            else:
                qry = "UPDATE `internal_guide` SET `internal_name`='" + name + "',`email`='" + email + "',`phoneno`='" + phone + "',`place`='" + place + "',`dob`='" + dob + "',`gender`='" + gender + "' WHERE `internal_guide_id`='" + str(igid) + "'"
                res = db.update(qry)
        else:
            qry = "UPDATE `internal_guide` SET `internal_name`='" + name + "',`email`='" + email + "',`phoneno`='" + phone + "',`place`='" + place + "',`dob`='" + dob + "',`gender`='" + gender + "' WHERE `internal_guide_id`='" + str(igid) + "'"
            res = db.update(qry)
        return '''<script>alert('Successfully Updated');window.location="/internal_view_admin"</script>'''
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''





######################################################### external ##############################################



@app.route('/external_organization_add')
def external_organization_add():
        return render_template("sign_index.html")



@app.route('/external_organization_add_post', methods=['POST'])
def external_organization_add_post():
    cname = request.form['textfield']
    email = request.form['textfield2']
    phoneno = request.form['textfield3']
    place = request.form['textfield4']
    post = request.form['textfield5']
    pin = request.form['textfield6']
    licenseno = request.form['textfield7']
    logo = request.files['fileField']
    password = request.form['Password']
    confirm = request.form['cpassword']
    date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    logo.save(r"E:\\project final\\web\\complete_my_project\\static\\external_org\\" + date + ".jpg")
    path = ("/static/external_org/" + date + ".jpg")

    if password == confirm:
        db = Db()
        qry = "INSERT INTO `login`(`username`,`password`,`user_type`) VALUES ('" + email + "','" + str(
            confirm) + "','pending')"
        res = db.insert(qry)
        qry1 = "INSERT INTO `external_organization`(`company_name`,`phoneno`,`place`,`email`,`post`,`pin`,`license_no`,`lid`,`logo`)VALUES('" + cname + "','" + phoneno + "','" + place + "','" + email + "','" + post + "','" + pin + "','" + licenseno + "','" + str(
            res) + "','" + str(path) + "')"
        res1 = db.insert(qry1)
        return '''<script>alert('Successfully Registered');window.location="/"</script>'''
    else:
        return '''<script>alert('password missmatch');window.location="/external_organization_add"</script>'''





@app.route('/aprv_ext_org/<id>')
def aprv_ext_org(id):
    db=Db()
    qry = "update external_organization set ac_status='approved' WHERE lid='"+str(id)+"'"
    res = db.update(qry)
    qry1 = "update login set user_type='external_organization' WHERE login_id='"+str(id)+"'"
    res1 = db.update(qry1)
    return '''<script>alert('Approved');window.location='/external_organization_view_admin'</script>'''


@app.route('/rej_ext_org/<id>')
def rej_ext_org(id):
    db=Db()
    qry = "update external_organization set ac_status='Rejected' WHERE lid='"+str(id)+"'"
    res = db.update(qry)
    qry1 = "update login set user_type='Rejected' WHERE login_id='"+str(id)+"'"
    res1 = db.update(qry1)
    return '''<script>alert('Rejected');window.location='/external_organization_view_admin'</script>'''









@app.route('/external_organization_view_admin')
def external_organization_view_admin():
    if session['log'] == "lin":
        db=Db()
        qry="select * from `external_organization`"
        res=db.select(qry)
        return render_template("admin/external_organization_view.html",data=res)
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''


@app.route('/search_external_organization_post', methods=['POST'])
def search_external_organization_post():
    if session['log'] == "lin":
        search=request.form['textfield']
        db = Db()
        qry = "select * from `external_organization` where `company_name` LIKE '%"+search+"%'"
        res = db.select(qry)
        return render_template("admin/external_organization_view.html", data=res)
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''


@app.route('/delete_external_organization/<eoid>')
def delete_external_organization(eoid):
    if session['log'] == "lin":
        db=Db()
        qry="delete from `external_organization` where `external_id`='"+eoid+"'"
        res=db.delete(qry)
        return '''<script>alert('Successfully Deleted');window.location="/external_organization_view_admin"</script>'''
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''


@app.route('/edit_external_organization')
def edit_external_organization():
    if session['log'] == "lin":
        db=Db()
        qry = "select * from `external_organization` where `external_id`='"+str(session['lid'])+"'"
        res = db.selectOne(qry)
        return render_template("admin/external_organization_edit.html",data=res)
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''

@app.route('/edit_external_organization_post', methods=['POST'])
def edit_external_organization_post():
    if session['log'] == "lin":
        # eoid=request.form['eoid']
        cname = request.form['textfield']
        email = request.form['textfield2']
        phoneno = request.form['textfield3']
        place = request.form['textfield4']
        post = request.form['textfield5']
        pin = request.form['textfield6']
        licenseno = request.form['textfield7']

        if 'fileField' in request.files:
            logo = request.files['fileField']
            if logo.filename!="":

                date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
                logo.save(r"E:\\project final\\web\\complete_my_project\\static\\external_org\\" + date + ".jpg")
                path = ("/static/external_org/" + date + ".jpg")

                db = Db()
                qry = "UPDATE `external_organization` SET `company_name`='" + cname + "',`phoneno`='" + phoneno + "',`place`='" + place + "',`email`='" + email + "',`post`='" + post + "',`pin`='" + pin + "',`license_no`='" + licenseno + "',`logo`='"+path+"' WHERE `external_id`='" + str(
                    session['lid']) + "'"
                res = db.update(qry)
                return '''<script>alert('Successfully Updated');window.location="/external_organization_view_admin"</script>'''
            else:
                db = Db()
                qry = "UPDATE `external_organization` SET `company_name`='" + cname + "',`phoneno`='" + phoneno + "',`place`='" + place + "',`email`='" + email + "',`post`='" + post + "',`pin`='" + pin + "',`license_no`='" + licenseno + "' WHERE `external_id`='" + str(
                    session['lid']) + "'"
                res = db.update(qry)
                return '''<script>alert('Successfully Updated');window.location="/external_organization_view_admin"</script>'''
        else:
            db = Db()
            qry = "UPDATE `external_organization` SET `company_name`='" + cname + "',`phoneno`='" + phoneno + "',`place`='" + place + "',`email`='" + email + "',`post`='" + post + "',`pin`='" + pin + "',`license_no`='" + licenseno + "' WHERE `external_id`='" + str(
                session['lid']) + "'"
            res = db.update(qry)
            return '''<script>alert('Successfully Updated');window.location="/external_organization_view_admin"</script>'''



    else:
            return '''<script>alert('You Are Loged Out');window.location="/"</script>'''



##################################################################### student ###############################################


@app.route('/student_add')
def student_add():
    if session['log']=="lin":
        return render_template("admin/studentl_add.html")
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''

@app.route('/student_add_post', methods=['POST'])
def student_add_post():
    if session['log']=="lin":
        name=request.form['textfield']
        email=request.form['textfield2']
        phoneno=request.form['textfield3']
        place=request.form['textfield4']
        post=request.form['textfield6']
        pin=request.form['textfield7']
        disrict=request.form['select']
        dob=request.form['textfield5']
        gender=request.form['RadioGroup1']
        photo=request.files['fileField']
        date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        photo.save(r"E:\\project final\\web\\complete_my_project\\static\\student\\" + date + ".jpg")
        path = ("/static/student/" + date + ".jpg")
        db=Db()
        qry="INSERT INTO `student` (`sname`,`email`,`phoneno`,`place`,`post`,`pin`,`district`,`gender`,`dob`,`photo`) VALUES('"+name+"','"+email+"','"+phoneno+"','"+place+"','"+post+"','"+pin+"','"+disrict+"','"+gender+"','"+dob+"','"+str(path)+"')"
        res=db.insert(qry)
        return '''<script>alert('Successfully Registered');window.location="/student_view_admin"</script>'''
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''

@app.route('/student_view_admin')
def student_view_admin():
    if session['log']=="lin":
        db=Db()
        qry="select * from `student`"
        res=db.select(qry)
        return render_template("admin/student_view.html",data=res)
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''


@app.route('/search_student_view_post', methods=['POST'])
def search_student_view_post():
    if session['log']=="lin":
        search=request.form['textfield']
        db = Db()
        qry = "select * from `student` where `sname` like '%"+search+"%'"
        res = db.select(qry)
        return render_template("admin/student_view.html", data=res)
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''


@app.route('/delete_student_admin/<sid>')
def delete_student_admin(sid):
    if session['log']=="lin":
        db=Db()
        qry="delete from `student` where `student_id`='"+sid+"'"
        db.delete(qry)
        return '''<script>alert('Successfully Deleted');window.location="/student_view_admin"</script>'''
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''

@app.route('/student_edit/<sid>')
def student_edit(sid):
    if session['log']=="lin":
        db=Db()
        qry = "select * from `student` where `student_id`='"+sid+"'"
        res = db.selectOne(qry)
        return render_template("admin/student_edit.html",data=res)
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''


@app.route('/student_edit_post', methods=['POST'])
def student_edit_post():
    if session['log']=="lin":
        db=Db()
        sid=request.form['sid']
        name = request.form['textfield']
        email = request.form['textfield2']
        phoneno = request.form['textfield3']
        place = request.form['textfield4']
        post = request.form['textfield6']
        pin = request.form['textfield7']
        disrict = request.form['select']
        dob = request.form['textfield5']
        gender = request.form['RadioGroup1']
        photo = request.files['fileField']
        date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        photo.save("E:\\project final\\web\\complete_my_project\\static\\student\\" + date + ".jpg")
        path = ("/static/student/" + date + ".jpg")
        if request.files!=None:
            if photo.filename!="":
                qry="UPDATE `student` SET `sname`='"+name+"',`email`='"+email+"',`phoneno`='"+phoneno+"',`place`='"+place+"',`post`='"+post+"',`pin`='"+pin+"',`district`='"+disrict+"',`gender`='"+gender+"',`dob`='"+dob+"',`photo`='"+str(path)+"' WHERE `student_id`='"+str(sid)+"'"
                res=db.update(qry)
            else:
                qry = "UPDATE `student` SET `sname`='" + name + "',`email`='" + email + "',`phoneno`='" + phoneno + "',`place`='" + place + "',`post`='" + post + "',`pin`='" + pin + "',`district`='" + disrict + "',`gender`='" + gender + "',`dob`='" + dob + "' WHERE `student_id`='" + str(sid) + "'"
                res = db.update(qry)
        else:
            qry = "UPDATE `student` SET `sname`='" + name + "',`email`='" + email + "',`phoneno`='" + phoneno + "',`place`='" + place + "',`post`='" + post + "',`pin`='" + pin + "',`district`='" + disrict + "',`gender`='" + gender + "',`dob`='" + dob + "' WHERE `student_id`='" + str(
                sid) + "'"
            res = db.update(qry)
        return '''<script>alert('Successfully Updated');window.location="/student_view_admin"</script>'''
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''



############################################################################ Group##########################################

#
@app.route('/add_group')
def add_group():
    if session['log']=="lin":
        return render_template("admin/add_group.html")
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''


@app.route('/add_group_post', methods=['POST'])
def add_group_post():
    if session['log']=="lin":
        grp_name=request.form['textfield']
        year=request.form['textfield2']
        password=random.randint(0000,9999)
        db=Db()
        qry1="INSERT INTO `login` (`username`,`password`,`user_type`) VALUES('"+grp_name+"','"+str(password)+"','group')"
        res1=db.insert(qry1)
        qry = "INSERT INTO `group` (`group_name`,`year`,`group_lid`) VALUES ('" + grp_name + "','" + year + "','"+str(res1)+"')"
        res = db.insert(qry)
        session['gid']=str(res1)
        return '''<script>alert('Successfully Added');window.location="/group_view_student"</script>'''
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''


@app.route('/admin_view_group')
def admin_view_group():
    if session['log']=="lin":
        db=Db()
        qry="SELECT `group`.*,`group`.group_lid as gp,group_allocation.* FROM `group` LEFT JOIN `group_allocation` ON `group`.`group_lid`=`group_allocation`.`group_id`"
        res=db.select(qry)
        print(res)
        qry1="select * from internal_guide"
        res2=db.select(qry1)
        return render_template("admin/view_group.html",data=res,data2=res2)
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''


@app.route('/admin_view_group_post', methods=['POST'])
def admin_view_group_post():
    if session['log']=="lin":
        search=request.form['textfield']
        db=Db()
        qry = "SELECT `group`.*,`group`.group_lid as gp,group_allocation.* FROM `group` LEFT JOIN `group_allocation` ON `group`.`group_lid`=`group_allocation`.`group_id` and `group`.`group_name` like '%"+search+"%'"
        res = db.select(qry)
        print(res)
        qry1 = "select * from internal_guide"
        res2 = db.select(qry1)
        return render_template("admin/view_group.html", data=res, data2=res2)
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''


@app.route('/delete_group_admin/<gid>')
def delete_group_admin(gid):
    if session['log']=="lin":
        db=Db()
        qry1 = "delete from `group_member` where group_id='" + str(gid) + "'"
        res1 = db.delete(qry1)
        qry2 = "delete from `group_allocation` where group_id='" + str(gid) + "'"
        res2 = db.delete(qry2)
        qry="delete from `group` where group_lid='"+gid+"'"
        res=db.delete(qry)
        return '''<script>alert('Successfully Deleted');window.location="/admin_view_group"</script>'''
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''


########################################################################### members ###################################


@app.route('/group_view_student')
def group_view_student():
    if session['log']=="lin":
        db=Db()
        qry="SELECT * FROM student WHERE `student_id` NOT IN (SELECT `student_lid` FROM `group_member`)"
        res=db.select(qry)
        return render_template("admin/grp_student_view.html",data=res)
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''



@app.route('/add_group_members_admin', methods=['POST'])
def add_group_members_admin():
    if session['log']=="lin":
        members=request.form.getlist('checkbox')
        gid=session['gid']
        b=[]
        db=Db()
        for a in members:
            print(a)
            b.append(a)
            qry1 = "INSERT INTO `group_member`(`group_id`,`student_lid`) VALUES('"+gid+"','"+str(a)+"')"
            res1 = db.insert(qry1)
        return '''<script>alert('Successfully Added');window.location="/Admin_Home"</script>'''
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''



@app.route('/search_group_student_view_post', methods=['POST'])
def search_group_student_view_post():
    if session['log']=="lin":
        search=request.form['textfield']
        db = Db()
        qry = "SELECT * FROM student WHERE `student_id` NOT IN (SELECT `student_lid` FROM `group_member`) and sname like '%"+search+"%'"
        res = db.select(qry)
        return render_template("admin/grp_student_view.html", data=res)
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''


@app.route('/view_group_member_admin/<gid>')
def view_group_member_admin(gid):
    if session['log']=="lin":
        db=Db()
        qry="SELECT `group_member`.*,`student`.* FROM `group_member` INNER JOIN `student` ON  `group_member`.`student_lid`=`student`.`student_id` WHERE `group_member`.`group_id`='"+str(gid)+"'"
        res=db.select(qry)
        return render_template("admin/group_member_view.html",data=res)
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''




@app.route('/group_allot_internals_post', methods=['POST'])
def group_allot_internals_post():
    if session['log']=="lin":
        db=Db()
        gid=request.form['id']
        print(gid)
        internal_id=request.form['internal']
        qry="INSERT INTO `group_allocation` (`group_id`,`internal_lid`,`allocated_date`,`status`) VALUES ('"+gid+"','"+internal_id+"',CURDATE(),'Allocated')"
        res=db.insert(qry)
        return '''<script>alert('Success');window.location="/admin_view_group"</script>'''
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''



########################################################################### schedule #####################################################################


@app.route('/add_schedule')
def add_schedule():
    if session['log']=="lin":
        return render_template("admin/schedule.html")
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''

@app.route('/add_schedule_post', methods=['POST'])
def add_schedule_post():
    if session['log']=="lin":
        db=Db()
        tittle=request.form['textfield']
        description=request.form['textarea']
        date=request.form['textfield2']
        qry="INSERT INTO `project_schedule` (`description`,`date`,`tittle`) VALUES ('"+description+"','"+date+"','"+tittle+"')"
        res=db.insert(qry)
        return '''<script>alert('Success Scheduled');window.location="/Admin_Home"</script>'''
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''


@app.route('/admin_view_schedule')
def admin_view_schedule():
    if session['log']=="lin":
        db=Db()
        qry="select * from `project_schedule`"
        res=db.select(qry)
        return render_template("admin/schedule_view.html",data=res)
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''

@app.route('/delete_schedule_admin/<sid>')
def delete_schedule_admin(sid):
    if session['log']=="lin":
        db=Db()
        qry="delete from `project_schedule` where `schedule_id`='"+str(sid)+"'"
        res=db.delete(qry)
        return '''<script>alert('Success Deleted');window.location="/admin_view_schedule"</script>'''
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''




@app.route('/edit_schedule_admin/<sid>')
def edit_schedule_admin(sid):
    if session['log']=="lin":
        db=Db()
        qry="select * from `project_schedule` where `schedule_id`='"+str(sid)+"'"
        res=db.selectOne(qry)
        return render_template("admin/schedule_edit.html",data=res)
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''



@app.route('/edit_schedule_post', methods=['POST'])
def edit_schedule_post():
    if session['log']=="lin":
        sid=request.form['sid']
        tittle=request.form['textfield']
        description=request.form['textarea']
        date=request.form['textfield2']
        db=Db()
        qry="UPDATE `project_schedule` SET `description`='"+description+"',`date`='"+date+"',`tittle`='"+tittle+"' WHERE `schedule_id`='"+sid+"'"
        res=db.update(qry)
        return '''<script>alert('Success Updated');window.location="/admin_view_schedule"</script>'''
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''


@app.route('/admin_view_attendence/<id>')
def admin_view_attendence(id):
    if session['log']=="lin":
        db=Db()
        qry="SELECT `attendence`.*,`student`.`sname` FROM `attendence` INNER JOIN `group_member` ON `attendence`.`group_member_id`=`group_member`.`member_id` JOIN student ON `student`.`student_id`=`group_member`.`student_lid` AND `group_member`.`group_id`='"+id+"'"
        res=db.select(qry)
        return render_template("admin/view_attendace.html",data=res)
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''

@app.route('/admin_view_progress/<gid>')
def admin_view_progress(gid):
    if session['log']=="lin":
        db=Db()
        qry="SELECT * FROM `progress` INNER JOIN `group` ON `progress`.`group_id`=`group`.`group_lid` where `progress`.`group_id`='"+str(gid)+"'"
        res=db.select(qry)
        return render_template("admin/view_progress.html",data=res)
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''


######################################################## end admin ###############################################################

#####################################################################################################################################



#########################################home

@app.route('/internal_home')
def internal_home():
    if session['log']=="lin":
         return render_template("internal_guide/internalindex.html")
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''

#################################### assigned works


@app.route('/Internal_view_assigned_group')
def Internal_view_assigned_group():
    if session['log']=="lin":
        db=Db()
        # qry="SELECT * FROM `group_allocation` INNER JOIN `group` ON `group_allocation`.`group_id`=`group`.`group_id` WHERE `group_allocation`.`internal_lid`='"+str(session['lid'])+"'"
        qry="SELECT `group`.*,`group`.`group_lid` AS gp,`group_allocation`.*,`external_group_allocation`.* FROM `group` INNER JOIN `group_allocation` ON `group`.`group_lid`=`group_allocation`.`group_id` LEFT JOIN `external_group_allocation` ON `external_group_allocation`.`group_id`=`group`.`group_lid` WHERE `group_allocation`.`internal_lid`='"+str(session['lid'])+"'"
        res=db.select(qry)
        qry1 = "SELECT * FROM `external_organization`"
        res1 = db.select(qry1)
        return render_template("internal_guide/view_allocated_group.html",data=res,data1=res1)
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''


@app.route('/iguide_view_members/<gid>')
def iguide_view_members(gid):
    db=Db()
    qry="SELECT * FROM `group_member` INNER JOIN  `group_allocation` ON `group_allocation`.`group_id`=`group_member`.`group_id` INNER JOIN  `student` ON `student`.`student_id`=`group_member`.`student_lid` where `group_member`.`group_id`='"+gid+"'"
    res=db.select(qry)
    return render_template("internal_guide/group_member_view.html",data=res)



@app.route('/iguide_add_mark/<sid>')
def iguide_add_mark(sid):
    return render_template("internal_guide/add_mark.html",data=sid)


@app.route('/iguide_add_mark_post', methods=['POST'])
def iguide_add_mark_post():
    sid=request.form['stid']
    mark=request.form['textfield']
    db=Db()
    qry="INSERT INTO `mark` (`student_id`,`mark`,`date`) VALUES('"+sid+"','"+mark+"',CURDATE())"
    res=db.insert(qry)
    return '''<script>alert('Success');window.location="/Internal_view_assigned_group"</script>'''

@app.route('/iguide_view_mark/<sid>')
def iguide_view_mark(sid):
    db=Db()
    qry="SELECT * FROM `mark` WHERE `student_id`='"+sid+"'"
    res=db.select(qry)
    return render_template("internal_guide/view_mark.html",data=res)


@app.route('/view_uploaded_topics/<gid>')
def view_uploaded_topics(gid):
    if session['log']=="lin":
        db=Db()
        qry="SELECT `group_topic`.*,`group`.`group_lid` FROM `group_topic` INNER JOIN `group` ON `group_topic`.`group_id`=`group`.`group_lid` where `group_topic`.`group_id`='"+gid+"'"
        res=db.select(qry)
        return  render_template("internal_guide/view_group_topics.html",data=res)
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''


@app.route('/internal_approve_topics/<gpid>')
def internal_approve_topics(gpid):
    if session['log']=="lin":
        db=Db()
        qry="update `group_topic` set status='Approved' where grp_topic_id='"+str(gpid)+"'"
        res=db.update(qry)
        return '''<script>alert('Approved Successfully');window.location="/Internal_view_assigned_group"</script>'''
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''


@app.route('/internal_reject_topics/<gpid>')
def internal_reject_topics(gpid):
    if session['log']=="lin":
        db = Db()
        qry = "update `group_topic` set status='Rejected' where grp_topic_id='" + str(gpid) + "'"
        res = db.update(qry)
        return '''<script>alert('Rejected Successfully');window.location="/Internal_view_assigned_group"</script>'''
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''


@app.route('/internal_allocated_organization_post',methods=['post'])
def internal_allocated_organization_post():
    if session['log']=="lin":
        db=Db()
        gid=request.form['id']
        print(gid)
        external=request.form['external']
        qry="INSERT INTO `external_group_allocation`(`group_id`,`external_lid`,`status`,`date`,`internal_lid`) VALUES('"+str(gid)+"','"+external+"','Allocated',CURDATE(),'"+str(session['lid'])+"')"
        res=db.insert(qry)
        return '''<script>alert('Allot Successfully');window.location="/Internal_view_assigned_group"</script>'''
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''



################################################## chat ###############################################################

#######################################################################################################################


@app.route("/chat")
def chat():
    if session['log']=="lin":
        # session["userid"]=id
        return render_template("internal_guide/fur_chat.html")
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''

@app.route("/chatview",methods=['post'])
def chatview():
    if session['log']=="lin":
        db=Db()
        qry="select * from external_organization"
        # qry="select * from student where user_lid='"+str(session["userid"])+"'"
        res=db.select(qry)
        print(res)
        return jsonify(data=res)
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''

@app.route("/doctor_insert_chat/<msg>")
def insert_chat(msg):
    if session['log']=="lin":
        db=Db()
        qry="insert into chat (date,from_id,to_id,chat) values (curdate(),'"+str(session['lid'])+"','"+str(session["userid"])+"','"+msg+"')"
        db.insert(qry)
        return jsonify(status="ok")
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''



@app.route("/drviewmsg/<id>")        # refresh messages chatlist
def chat_usr_chk(id):
    if session['log']=="lin":
        session["userid"]=id
        # qry = "select from_id,message as msg,date,chat_id from chat where (from_id='"+str(session["lid"])+"' and to_id='" + str(id) + "') or ((from_id='" + str(id) + "' and to_id='"+str(session["lid"])+"')) order by chat_id desc"
        qry = "select from_id,chat as msg,date,chat_id from chat where (from_id='"+str(session['lid'])+"' and to_id='" + str(session["userid"]) + "') or ((from_id='" + str(session["userid"]) + "' and to_id='"+str(session['lid'])+"')) order by chat_id asc"
        c = Db()
        res = c.select(qry)
        ry = "select * from external_organization where lid='" + str(session["userid"]) + "'"
        rest = c.selectOne(ry)
        print(rest)
        return jsonify(data=res,user_name=rest["company_name"],user_photo=rest["logo"],user_lid=rest["lid"])
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''


##################################### end chat #########################################################################

########################################################################################################################

###################################################### attendance


@app.route('/internal_view_attendance/<gid>')
def internal_view_attendance(gid):
    # if session['log']=="log":
        db=Db()
        qry="SELECT *, `attendence`.`status` AS astatus FROM `attendence` INNER JOIN `group_member` ON `group_member`.`member_id`=`attendence`.`group_member_id` INNER JOIN `group` ON `group`.`group_lid`=`group_member`.`group_id` INNER JOIN `group_allocation` ON `group_allocation`.`group_id`=`group`.`group_lid` INNER JOIN `student` ON `student`.`student_id`=`group_member`.`student_lid` WHERE `group_allocation`.`internal_lid`='"+str(session['lid'])+"' AND `group_allocation`.`group_id`='"+gid+"' "
        res=db.select(qry)
        return render_template("internal_guide/view_attendace.html",data=res)
    # else:
    #     return '''<script>alert('You Are Loged Out');window.location="/"</script>'''



####################################### schedule



@app.route('/internal_view_schedle')
def internal_view_schedle():
    if session['log']=="lin":
        db=Db()
        qry="SELECT * FROM `project_schedule`"
        res=db.select(qry)
        return render_template("internal_guide/schedule_view.html",data=res)
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''


################################################## progresss ########################

@app.route('/internal_view_progress/<gid>')
def internal_view_progress(gid):
    if session['log']=="lin":
        db=Db()
        qry="SELECT *, `progress`.`date` AS pdate FROM `progress` INNER JOIN `group` ON `group`.`group_lid`=`progress`.`group_id` INNER JOIN `group_allocation` ON `group_allocation`.`group_id`=`group`.`group_lid` WHERE  `progress`.`group_id`='"+gid+"' AND `group_allocation`.`internal_lid`='"+str(session['lid'])+"'"
        res=db.select(qry)
        return render_template("internal_guide/view_progress.html",data=res)
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''



#####################################################files ############################


@app.route('/internal_view_files')
def internal_view_files():
    if session['log']=="lin":
        db=Db()
        qry="SELECT `files`.*,`group_allocation`.`group_id`,`group_allocation`.`internal_lid`,`group`.`group_id`,`group`.`group_name` FROM `files` INNER JOIN `group_allocation` ON `group_allocation`.`group_id`=`files`.`group_id` JOIN `group` ON `group_allocation`.`group_id`=`group`.`group_id` WHERE `group_allocation`.`internal_lid`='"+str(session['lid'])+"'"
        res=db.select(qry)
        return render_template("internal_guide/view_files.html",data=res)
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''



############################################################# video####################################

@app.route('/internal_view_vidoes/<gid>')
def internal_view_vidoes(gid):
    if session['log']=="lin":
        db=Db()
        qry="SELECT *, `videos`.`date` AS vdate FROM `videos` INNER JOIN `group` ON `group`.`group_lid`=`videos`.`group_id` INNER JOIN `group_allocation` ON `group_allocation`.`group_id`=`group`.`group_lid` WHERE `videos`.`group_id`='"+str(gid)+"' AND `group_allocation`.`internal_lid`='"+str(session['lid'])+"'"
        res=db.select(qry)
        return render_template("internal_guide/view_videos.html",data=res)
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''


############################################################  internl end #################################################


######################################################### External start ##############################################

@app.route('/external_home')
def external_home():
    if session['log']=="lin":
        return render_template("external_organization/externalindex.html")
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''

################################################################### profile

@app.route('/external_view_profile')
def external_view_profile():
    if session['log']=="lin":
        db=Db()
        qry="SELECT * FROM `external_organization` WHERE `lid`='"+str(session['lid'])+"'"
        res=db.selectOne(qry)
        return render_template("external_organization/view_profile.html",data=res)
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''

#################################################################################  group

@app.route('/external_view_group')
def external_view_group():
    if session['log']=="lin":
        db=Db()
        qry="SELECT `external_group_allocation`.*,`group`.*,`internal_guide`.`lid`,`internal_guide`.`internal_name` FROM `external_group_allocation` INNER JOIN `group` ON `external_group_allocation`.`group_id`=`group`.`group_lid` JOIN  `internal_guide` ON `external_group_allocation`.`internal_lid`=`internal_guide`.`lid` WHERE `external_group_allocation`.`external_lid`='"+str(session['lid'])+"'"
        res=db.select(qry)
        return render_template("external_organization/view_group.html",data=res)
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''



################################################################# attendance #########################

@app.route('/external_view_members/<gid>')
def external_view_members(gid):
    if session['log']=="lin":
        db=Db()
        session["gp_id"]=gid
        qry="SELECT `group_member`.*,`group`.`group_lid`,`student`.* FROM `group_member` INNER JOIN `group` ON `group_member`.`group_id`=`group`.`group_lid` JOIN `student` ON `group_member`.`student_lid`=`student`.`student_id` WHERE `group_member`.`group_id`='"+str(gid)+"'"
        res=db.select(qry)
        return render_template("external_organization/view_member.html",data=res)
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''


@app.route('/external_update_attendance',methods=['post'])
def external_update_attendance():
    if session['log']=="lin":
        db=Db()
        attandance=request.form.getlist('checkbox')
        b=[]
        for a in attandance:
            b.append(a)
            print(a)
            qry="INSERT INTO `attendence` (`date`,`group_member_id`,`status`,`external_lid`)VALUES(CURDATE(),'"+str(a)+"','Present','"+str(session['lid'])+"')"
            res=db.insert(qry)
        qry2="SELECT * FROM `group_member` WHERE `group_id`='"+str(session["gp_id"])+"' AND `member_id` NOT IN (SELECT `group_member_id` FROM `attendence` WHERE `date`=curdate())"
        res2=db.select(qry2)
        for i in res2:
            qry = "INSERT INTO `attendence` (`date`,`group_member_id`,`status`,`external_lid`)VALUES(CURDATE(),'" + str(
                i["member_id"]) + "','Absent','" + str(session['lid']) + "')"
            res = db.insert(qry)
        return '''<script>alert('Successfully Marked');window.location="/external_view_group"</script>'''
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''



##################################################################### daily works#######################################

@app.route('/external_upload_work_info/<gid>')
def external_upload_work_info(gid):
    if session['log']=="lin":
        return render_template("external_organization/upload_workinfo.html",gp_id=gid)
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''

@app.route('/external_upload_workinfo_post', methods=['POST'])
def external_upload_workinfo_post():
    if session['log']=="lin":
        db=Db()
        gpid=request.form['gid']
        info=request.form['textarea']
        qry="INSERT INTO `daily_works` (`group_id`,`workinfo`,`date`,`external_lid`) VALUES('"+str(gpid)+"','"+info+"',CURDATE(),'"+str(session['lid'])+"')"
        res=db.insert(qry)
        return '''<script>alert('Successfully uploaded');window.location="/external_view_group"</script>'''
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''




@app.route('/external_view_schedle')
def external_view_schedle():
    if session['log']=="lin":
        db=Db()
        qry="SELECT * FROM `project_schedule`"
        res=db.select(qry)
        return render_template("external_organization/schedule_view.html",data=res)
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''


############################################################## chat ##################################################3
######################################################################################################################



@app.route("/chat1")
def chat1():
    if session['log']=="lin":
        # session["userid"]=id
        return render_template("external_organization/fur_chat1.html")
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''

@app.route("/chatview1",methods=['post'])
def chatview1():
    if session['log']=="lin":
        db=Db()
        qry="select * from `internal_guide`"
        # qry="select * from student where user_lid='"+str(session["userid"])+"'"
        res=db.select(qry)
        print(res)
        return jsonify(data=res)
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''



@app.route("/doctor_insert_chat1/<msg>")
def insert_chat1(msg):
    if session['log']=="lin":
        db=Db()
        qry="insert into chat (date,from_id,to_id,chat) values (curdate(),'"+str(session['lid'])+"','"+str(session["userid"])+"','"+msg+"')"
        db.insert(qry)
        return jsonify(status="ok")
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''



@app.route("/drviewmsg1/<id>")        # refresh messages chatlist
def chat_usr_chk1(id):
    if session['log']=="lin":
        session["userid"]=id
        # qry = "select from_id,message as msg,date,chat_id from chat where (from_id='"+str(session["lid"])+"' and to_id='" + str(id) + "') or ((from_id='" + str(id) + "' and to_id='"+str(session["lid"])+"')) order by chat_id desc"
        qry = "select from_id,chat as msg,date,chat_id from chat where (from_id='"+str(session['lid'])+"' and to_id='" + str(session["userid"]) + "') or ((from_id='" + str(session["userid"]) + "' and to_id='"+str(session['lid'])+"')) order by chat_id asc"
        c = Db()
        res = c.select(qry)
        ry = "select * from `internal_guide` where lid='" + str(session["userid"]) + "'"
        rest = c.selectOne(ry)
        print(rest)
        return jsonify(data=res,user_name=rest["internal_name"],user_photo=rest["photo"],user_lid=rest["lid"])
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''



############################################################################### chat ######################################


################################################################################################


@app.route('/external_share_files/<gid>')
def external_share_files(gid):
    if session['log']=="lin":
        return render_template("external_organization/share_file.html",gpid=gid)
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''

@app.route('/external_share_file_post', methods=['POST'])
def external_share_file_post():
    if session['log']=="lin":
        db=Db()
        gid=request.form['gid']
        tittle=request.form['textfield']
        file=request.files['file']
        date=datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        file.save(r"E:\\project final\\web\\complete_my_project\\static\\files\\"+date+".pdf")
        path=("/static/files/"+date+".pdf")
        qry="INSERT INTO `files` (`group_id`,`tittle`,`filename`,`date`) VALUES('"+gid+"','"+tittle+"','"+path+"',CURDATE())"
        res=db.insert(qry)
        return '''<script>alert('Successfully Shared');window.location="/external_view_group"</script>'''
    else:
        return '''<script>alert('You Are Loged Out');window.location="/"</script>'''




#####################################################################################################################################


############################################## Android  ##########################################################################


@app.route('/and_login',methods = ['post'])
def and_loginz():
    db = Db()
    u = request.form['u']
    p = request.form['p']
    qry="SELECT * FROM `login` WHERE `username` = '"+u+"'  AND `password`= '"+p+"'"
    res = db.selectOne(qry)
    # print(res)
    if res is not None:
        if res['user_type'] == 'group':
            return jsonify(status='ok',lid=res["login_id"],type=res["user_type"])
        else:
            return jsonify(status='no')
    else:
        return jsonify(status='no')


@app.route('/and_group_view_internal_guide', methods=['POST'])
def and_group_view_internal_guide():
    db=Db()
    lid=request.form['lid']
    qry="SELECT * FROM `group_allocation` INNER JOIN `internal_guide` ON `group_allocation`.`internal_lid`=`internal_guide`.`lid` WHERE `group_allocation`.`group_id`='"+lid+"'"
    res=db.select(qry)
    return jsonify(status="ok",data=res)


@app.route('/upload_group_topics', methods=['POST'])
def upload_group_topics():
    db=Db()
    lid=request.form['lid']
    tname=request.form['name']
    topic=request.form['pic']
    timestr = time.strftime("%Y%m%d-%H%M%S")
    # print(timestr)
    a = base64.b64decode(topic)
    fh = open("E:\\project final\\web\\complete_my_project\\static\\topic\\" + timestr + "..pdf", "wb")
    path = "/static/topic/" + timestr + ".pdf"
    fh.write(a)
    fh.close()


    # date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    # topic.save("E:\\project final\\web\\complete_my_project\\static\\topic\\" + date + ".pdf")
    # path = ("/static/topic/" + date + ".pdf")

    qry="INSERT INTO `group_topic` (`group_id`,`topic_name`,`file`,`date_of_upload`,`status`) VALUES ('"+lid+"','"+tname+"','"+path+"',curdate(),'pending')"
    res=db.insert(qry)
    return jsonify(status="ok")



@app.route('/and_upload_work_progress', methods=['POST'])
def and_upload_work_progress():
    db=Db()
    status=request.form['project_status']
    date=request.form['project_duration']
    duration=request.form['project_date']
    photo=request.form['photo']
    lid=request.form['lid']
    timestr = time.strftime("%Y%m%d-%H%M%S")
    print(timestr)
    a = base64.b64decode(photo)
    fh = open("E:\\project final\\web\\complete_my_project\\static\\progress\\" + timestr +".jpg","wb")
    path = "\\static\\progress\\" + timestr + ".jpg"
    fh.write(a)
    fh.close()
    qry="INSERT INTO `progress` (`progress_status`,`group_id`,`duration`,`date`,`file_name`) VALUES('"+status+"','"+lid+"','"+duration+"','"+date+"','"+path+"')"
    res=db.insert(qry)
    return jsonify(status="ok")


@app.route('/and_view_schedules', methods=['POST'])
def and_view_schedules():
    db=Db()
    qry="select * from `project_schedule`"
    res=db.select(qry)
    print(res)
    return jsonify(status="ok",data=res)


@app.route('/and_view_external_organization', methods=['POST'])
def and_view_external_organization():
    db=Db()
    qry="SELECT * FROM `external_group_allocation` INNER JOIN `external_organization` ON `external_group_allocation`.`external_lid`=`external_organization`.`lid` INNER JOIN `group` ON `external_group_allocation`.`group_id`=`group`.`group_lid`"
    res=db.select(qry)
    print(res)
    return jsonify(status="ok",data=res)


@app.route('/and_view_mark', methods=['POST'])
def and_view_mark():
    db=Db()
    lid=request.form['lid']
    qry="SELECT * FROM `mark` INNER JOIN `group_member` ON `mark`.`student_id`=`group_member`.`student_lid` INNER JOIN `student` ON `mark`.`student_id`=`student`.`student_id` WHERE `group_member`.`group_id`='"+lid+"'"
    res=db.select(qry)
    print(res)
    return jsonify(status="ok",data=res)






@app.route('/upload_group_videos', methods=['POST'])
def upload_group_videos():
    db=Db()
    lid=request.form['lid']
    tname=request.form['tname']
    topic=request.form['topic']
    timestr = time.strftime("%Y%m%d-%H%M%S")
    print(timestr)
    a = base64.b64decode(topic)
    fh = open("E:\\project final\\web\\complete_my_project\\static\\videos\\" + timestr + ".mp4", "wb")
    path = "/static/videos/" + timestr + ".mp4"
    fh.write(a)
    fh.close()
    qry="INSERT INTO `videos` (`group_id`,`tittle`,`filename`,`date`) VALUES('"+lid+"','"+tname+"','"+path+"',CURDATE())"
    res=db.insert(qry)
    return jsonify(status="ok")


@app.route('/and_view_video', methods=['POST'])
def and_view_video():
    db=Db()
    lid=request.form['lid']
    qry="SELECT * FROM `videos` WHERE `group_id` ='"+lid+"'"
    res=db.select(qry)
    print(res)
    return jsonify(status="ok",data=res)



###################################################


@app.route('/public_view_list_of_projects_don_in__the_collage', methods=['POST'])
def public_view_list_of_projects_don_in__the_collage():
    db=Db()
    qry="SELECT * FROM `group_topic`"
    res=db.select(qry)
    return jsonify(status="ok",data=res)



@app.route('/public_view_list_of_projects_don_in__the_collage_grp', methods=['POST'])
def public_view_list_of_projects_don_in__the_collage_grp():
    db=Db()
    lid=request.form['lid']
    qry="SELECT * FROM `group_topic` WHERE group_id='"+lid+"'"
    res=db.select(qry)
    return jsonify(status="ok",data=res)





@app.route('/public_view_project_schedule', methods=['POST'])
def public_view_project_schedule():
    db=Db()
    qry="SELECT * FROM `project_schedule`"
    res=db.select(qry)
    return jsonify(status="ok",data=res)

@app.route('/public_view_working_videos', methods=['POST'])
def public_view_working_videos():
    db=Db()
    qry="SELECT * FROM `videos`"
    res=db.select(qry)
    return  jsonify(status="ok",data=res)

@app.route('/group_video_delete', methods=['POST'])
def group_video_delete():
    db=Db()
    did=request.form['vid']
    qry="DELETE FROM `videos` WHERE `video_id`='"+did+"'"
    res=db.delete(qry)
    return  jsonify(status="ok",data=res)




# @app.route('/', methods=['POST'])
# def ():
#     pass





if __name__ == '__main__':
    app.run(debug=True,port=5000,host='0.0.0.0')
