import webbrowser
import sys

print("Welcome to google dorking V1.0")
print("made by ALexdieu")
site = input("What is the website adress ?\n")
print("What would you like to do ?")
def choix():
    global site
    answer = input("1.Directory listing vulnerabilities\n2.Config file exposed\n3.Databse files exposed\n4.Log file exposed\n5.Backup and old files\n6.Login pages\n7.SQL errors\n8.Publicly exposed documents\n9.phpinfo()\n10.change url\n11.exit\n")
    if answer == "1":
        dlv = ('''https://www.google.com/search?q=site:'''+site+'''+intitle:index.of''')
        webbrowser.open(dlv)
        choix()
    elif answer == '2':
        cfe = ('''https://www.google.com/search?q=site:'''+site+'''+ext:xml+%7C+ext:conf+%7C+ext:cnf+%7C+ext:reg+%7C+ext:inf+%7C+ext:rdp+%7C+ext:cfg+%7C+ext:txt+%7C+ext:ora+%7C+ext:ini''')
        webbrowser.open(cfe)
        choix()
    elif answer == '3':
        dfe = ('''https://www.google.com/search?q=site:'''+site+'''+ext:sql+%7C+ext:dbf+%7C+ext:mdb''')
        webbrowser.open(dfe)
        choix()
    elif answer == '4':
        lfe = ('''https://www.google.com/search?q=site:'''+site+'''+ext:log''')
        webbrowser.open(lfe)
        choix()
    elif answer == '5':
        baof = ('''https://www.google.com/search?q=site:'''+site+'''+ext:bkf+%7C+ext:bkp+%7C+ext:bak+%7C+ext:old+%7C+ext:backup''')
        webbrowser.open(baof)
        choix()
    elif answer == '6':
        lp = ('''https://www.google.com/search?q=site:'''+site+'''+inurl:login''')
        webbrowser.open(lp)
        choix()
    elif answer == '7':
        sqle = ('''https://www.google.com/search?q=site%3A'''+site+'''%2Bintext%3A"sql%2Bsyntax%2Bnear"%2B%257C%2Bintext%3A"syntax%2Berror%2Bhas%2Boccurred"%2B%257C%2Bintext%3A"incorrect%2Bsyntax%2Bnear"%2B%257C%2Bintext%3A"unexpected%2Bend%2Bof%2BSQL%2Bcommand"%2B%257C%2Bintext%3A"Warning%3A%2Bmysql_connect()"%2B%257C%2Bintext%3A"Warning%3A%2Bmysql_query()"%2B%257C%2Bintext%3A"Warning%3A%2Bpg_connect()"''')
        webbrowser.open(sqle)
        choix()
    elif answer == '8':
        ped = ('''https://www.google.com/search?q=site:'''+site+'''+ext:doc+%7C+ext:docx+%7C+ext:odt+%7C+ext:pdf+%7C+ext:rtf+%7C+ext:sxw+%7C+ext:psw+%7C+ext:ppt+%7C+ext:pptx+%7C+ext:pps+%7C+ext:csv''')
        webbrowser.open(ped)
        choix()
    elif answer == '9':
        phpi = ('''https://www.google.com/search?q=site%3A'''+site+'''%2Bext%3Aphp%2Bintitle%3Aphpinfo%2B"published%2Bby%2Bthe%2BPHP%2BGroup"''')
        webbrowser.open(phpi)
        choix()
    elif answer == '10':
        site = input("What is the website adress ?\n")
        choix()
    elif answer == '11':
        ANS2 = input("Are you sure you want to quit ? y or n\n")
        if ANS2 == 'y' or 'yes':
            sys.exit("bye !")
        else:
            print('ok! back to menu')
            choix()
    else:
        print("pls answer by numbers !")
        choix()
            
        
        
choix()
