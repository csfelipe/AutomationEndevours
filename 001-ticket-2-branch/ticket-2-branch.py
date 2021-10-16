import re

ticket_number = input("Enter ticket number (e.g. TKT-1234): ")
ticket_name = input("Enter ticket name: ") 

ticket_number = ticket_number.replace('-','')

ticket_name = ticket_name.replace(' - ','-')
ticket_name = ticket_name.replace(' (','-')
ticket_name = ticket_name.replace('(','')
ticket_name = ticket_name.replace(')','')
ticket_name = ticket_name.replace(' ','_')
ticket_name = re.sub(r"[^a-zA-Z0-9\-\_]","",ticket_name)

branch_name = ticket_number + "-" + ticket_name
feature_branch_name = "feature/" + branch_name

def output_ticket(prepared_output):
	print("-----------------------------------------------------")
	print("-")
	print("\tBranch: " + prepared_output.lower())
	print("-")
	print("-----------------------------------------------------")
	
output_ticket(branch_name)
output_ticket(feature_branch_name)