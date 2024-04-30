def anxiety(score):
	if score<=17:return "Mild anxiety"
	elif score in range(18,25): return "Mild to Moderate anxiety"
	else: return "Moderate to severe anxiety"

def ocd(score):
	if score in range(8,16):return "mild OCD"
	elif score in range(16,24):return "moderate OCD"
	elif score in range(24,32):return "severe OCD"
	elif score in range(32,41):return "extreme OCD"
	return "No OCD"

def depression(value):
	if value in range(17,21) : return 'borderline clinical depression'
	elif value in range(11,17):return "mild mood depression"
	elif value in range(1,11): return "There ups and downs are considered normal"
	elif value in range(21,31): return 'moderate depression'
	elif value in range(31,41):return 'severe depression'
	elif value>=40: return 'extreme depression'

def did(score):
	if socre>=30:return "High Dissociative Identity Disorder"
	else:return "Low Dissociative Identity Disorder"

def ptsd(score):
	if score in range(0,33):return "PTSD severity below threeshold level"
	else:	return "PTSD severity above threeshold level"

def schizophrenia(score):
	if score>=14: return "severe schizophrenia. Suggestive of psychosis. See a health professional"
	elif score in renge(10,14): return "mild schizophrenia. Possible early psychosis. See a health professional"
	else: return "Unlikely to be psychosis"

def adhd(score):
	if score>=20:return "Symptoms highly consistent with ADHD"
	else: return "No symptoms of ADHD"

def postpartum(score):
	if score>=10:return "Possible postpartum depression"
	else: return "No postpartum depression"

def bipolar(score):
	if score<=15:return "Major depression"
	elif score>=25: return "bipolar spectrun disorder"
	return "may have either major depression or a disorder in the bipolar spectrum"

def pmdd(score):
	if score in range(0,3):return "little or no PMDD indication"
	elif score in range(3,6) : return "Moderate PMDD indication"
	elif score in range(6,9): return "strong PMDD indication"

def suicidal(score):
	if score <=2: return "No suicidal tendencies"
	elif score in range(3,5):return "Potential risk identified"
	elif score == 5:return "Imminent risk identified"