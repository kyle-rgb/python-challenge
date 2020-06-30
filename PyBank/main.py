#! python3
## main.py - Aggregates Results based on Financial Data
import os, sys, csv, datetime

csvPath = os.path.join(".", "Resources", "budget_data.csv")

with open(csvPath) as csvfile:
	months = 0
	total_p = 0
	last_m = 0
	change_counter = 0
	max_profit = 0
	max_name = ""
	min_profit = 0
	min_name = ""
	csvreader = csv.reader(csvfile, delimiter=",")
	csvheader = next(csvreader)
	for row in csvreader:
		if csvreader.line_num == 2:
			last_m = float(row[1])
			months += 1
			total_p += float(row[1])
			if float(row[1]) > max_profit:
				max_profit = float(row[1])
				max_name = str(row[0])
			elif float(row[1]) < min_profit:
				min_profit = float(row[1])
				min_name = str(row[0])
			else:
				max_profit = max_profit
				min_profit = min_profit
		elif row[0] != "" and csvreader.line_num != 2:
			months += 1
			total_p += float(row[1])
			last_m = -(last_m - float(row[1]))
			change_counter += last_m
			if last_m > max_profit:
				max_profit = last_m
				max_name = str(row[0])
			elif last_m < min_profit:
				min_profit = last_m
				min_name = str(row[0])
			else:
				max_profit = max_profit
				min_profit = min_profit
			last_m = float(row[1])
		else:
			break
	change_counter = round(change_counter / (months - 1), 2)
	
	total_months = f"Total Months: {months}"
	total_profit = f"Total: ${total_p}"
	avg_prof_change = f"Average Change: ${change_counter}"
	greatest_inc = f"Greatest Increase in Profits: {max_name} ${max_profit}"
	greatest_dec = f"Greatest Decrease in Profits: {min_name} ${min_profit}"

	
	print(total_months)
	print(total_profit)
	print(avg_prof_change)
	print(greatest_inc)
	print(greatest_dec)
csvfile.close()
	
textPath = os.path.join(".", "Analysis", "results.txt")
with open(textPath, "w") as resultfile:
    resultfile.write(total_months + "\n")
    resultfile.write(total_profit + "\n")
    resultfile.write(avg_prof_change + "\n")
    resultfile.write(greatest_inc + "\n")
    resultfile.write(greatest_dec + "\n")
    resultfile.close()


    
    
