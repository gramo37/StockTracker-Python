import mail_sender as ms
import stock_tracker as st
stocklist = {}

def submit(search_key, stoploss, target, result_row):
	prev_price = 0
	c_data = st.find_price(search_key.get())
	conv_stoploss = float(stoploss.get())
	conv_target = float(target.get())
	check_value = float(conv_target * 0.3)
	for key, val in c_data.items():
		if abs(float(val) - conv_stoploss) < check_value  or abs(float(val) - conv_target) < check_value:
			stocklist[key.lower()] = False
			calculatePrice(key, stoploss, target, result_row, prev_price)
			break
		
def calculatePrice(key1, stoploss, target, result_row, prev_price):
	result = "Price within range"
	color = "#6666ff"
	c_data = st.find_price(key1)
	for key, val in c_data.items():
		price = float(val)
		name_of_stock = key
		break
	if price >= float(target.get()):
		if ms.mailStatus(stocklist, name_of_stock):
			ms.send_mail("Target Achieved", "Name of Stock: {}\nCurrrent Price: {}".format(name_of_stock, price))
		result = "Target Achieved"
		color = "#b3ffb3"
	elif price < float(stoploss.get()):
		if ms.mailStatus(stocklist, name_of_stock):
			ms.send_mail("Stoploss Triggered", "Name of Stock: {}\nCurrrent Price: {}".format(name_of_stock, price))
		result = "Stoploss Triggered"
		color = "#ff6666"
	display_text(result, result_row, color, 8) # Display result
	if prev_price == 0:
		prev_price = price
	color_of_price, prev_price = change_color_of_price(prev_price, price)
	display_text(price, result_row, color_of_price, 9) # Display current price
	root.after(20000, lambda: calculatePrice(name_of_stock, stoploss, target, result_row, prev_price))

def change_color_of_price(prev_price, price):
	if prev_price > price:
		color_of_price = "red"
		prev_price = price
	elif prev_price < price:
		color_of_price = "green"
		prev_price = price
	else:
		color_of_price = "white"
		prev_price = price
	return color_of_price, prev_price

def display_text(txt, row, color, col):
	T = tk.Entry(root, justify='center', highlightthickness=2)
	T.config(background=color)
	T.grid(row=row,column=col)
	conv_txt = str(txt)
	T.insert(tk.END, conv_txt)

def limit_exceeded():
	pass

def delete_stock_row(row):
	global no_of_rows
	no_of_rows -= 1
	print("Delete row {}".format(row))

def create_stock_row(row):
	global no_of_rows
	global limit
	if(no_of_rows < limit):
		search_key=tk.StringVar()
		stoploss1_entered = tk.StringVar()
		target1_entered = tk.StringVar()

		stock1_label = tk.Label(root, text = 'Stock {}'.format(row), font=('calibre',10, 'bold'))
		stock1 = tk.Entry(root,textvariable = search_key, font=('calibre',10,'normal'))

		stoploss1_label = tk.Label(root, text = 'Stoploss', font = ('calibre',10,'bold'))
		stoploss1=tk.Entry(root, textvariable = stoploss1_entered, font = ('calibre',10,'normal'))

		target1_label = tk.Label(root, text = 'Target', font = ('calibre',10,'bold'))
		target1 = tk.Entry(root,textvariable = target1_entered, font=('calibre',10,'normal')) 

		sub_btn1=tk.Button(root,text = 'Submit', command = lambda: submit(search_key, stoploss1_entered, target1_entered, row))
		# del_btn1=tk.Button(root,text = 'Delete row', bg="red", command = lambda: delete_stock_row(row))

		stock1_label.grid(row=row,column=0)
		stock1.grid(row=row,column=1)
		stoploss1_label.grid(row=row,column=2)
		stoploss1.grid(row=row,column=3)
		target1_label.grid(row=row,column=4)
		target1.grid(row=row,column=5)
		sub_btn1.grid(row=row,column=6)
		# del_btn1.grid(row=row,column=10)
		no_of_rows += 1
	else:
		limit_exceeded()
		# print("Limit Exceeded")


def gui_init():
    global limit
    global no_of_rows
    global root
    global tk
    import tkinter as tk
    root=tk.Tk()
    root.geometry("910x300")
    limit = 11
    no_of_rows = 1
    add_btn =tk.Button(root, text ="Add row",bg="green",command = lambda: create_stock_row(no_of_rows))    
    add_btn.grid(row=limit,column=3)   

    # add_del =tk.Button(root, text ="Delete row",bg="red",command = lambda: del_stock_row(no_of_rows))    
    # add_del.grid(row=limit,column=4)   

    create_stock_row(1)
    root.mainloop()