from application import app
import random


@app.route('/randomphrase', methods=['GET', 'POST'])
def ending():

	list = ['Okay','doing good','amazing feels','alright','enthusiastic','well?','understanding?']
	
	return list[random.randrange(6)]