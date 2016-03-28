### U-shape Logic
## Testing with 40-20-40. Should Change to dynamic weight soon
def u_logic(df):
	if df.maxm==1:
		return 1
	elif df.maxm==2:
		return 0.5
	elif df.rankm==df.maxm:
		return 0.4
	elif df.rankm==1:
		return 0.4
	else:
		return 0.2/(df.maxm-2)