import smtplib

def mailStatus(stocklist, name_of_stock):    
    if stocklist[name_of_stock.lower()] == False:  # stocklist[reliance] = false (means mail is not sent)
        stocklist[name_of_stock.lower()] = True  # stocklist[reliance] = true (means mail is sent)
        return True  #  Send mail
    else:
        return False # Dont send mail

def send_mail(subject, body):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('gramopadhyeprasanna@gmail.com', 'prasanna@P2')
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'puspra067@gmail.com', 
        'gramopadhye37@gmail.com', 
        msg
    )
    print("Mail sent")

    server.quit()