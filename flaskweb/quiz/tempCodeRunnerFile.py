@login_required
def co2_polution():
    co2_quiz = Quiz.query.filter_by(user_id=current_user.id).first()
    print (co2_quiz)
       
co2_polution