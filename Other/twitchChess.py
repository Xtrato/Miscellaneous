#This program is used to allow twitch users to play chess from the IRC text chat. It is uncommented and a discontinued.
#project. It did however work. Let me know fi you need any help with it. james@jamesdotcom.com
import pywinauto
import socket
import re

def errorCheck():
    try:
        errorWindow = pywinauto.findwindows.find_windows(title=u'Error', class_name='#32770')[0]
        print "error"
        errwindow = pwa_app.window_(handle=errorWindow)
        #errwindow.SetFocus()
        errwindow.Close()
        return True
    except IndexError:
        print "No Error"
        pass

def chessMove(sentMove):
    pwa_app = pywinauto.application.Application()
    try:
        w_handle = pywinauto.findwindows.find_windows(title=u'WinBoard: Fairy-Max 4.8S', class_name='WinBoard')[0]
     except IndexError:
		try:
			w_handle = pywinauto.findwindows.find_windows(title=u'James vs. Fairy-Max 4.8S', class_name='WinBoard')[0]
        except IndexError:
			w_handle = pywinauto.findwindows.find_windows(title=u'White\'s flag fell', class_name='WinBoard')[0]
    window = pwa_app.window_(handle=w_handle)
    window.SetFocus()
    normalInput = sentMove
    window.TypeKeys(normalInput + "{ENTER}")
    if errorCheck() == True:
        errorInput = sentMove
        window.TypeKeys(errorInput + "{ENTER}")

PORT = 6667
PASSWORD = ''
IDENT = 'xtrato1988'
NICK = 'xtrato1988'
HOST = 'irc.twitch.tv'
REALNAME = 'James'
CHANNEL = '#xtrato1988'

irc=socket.socket( )
irc.connect((HOST, PORT))
irc.send("PASS %s\r\n" % PASSWORD)
irc.send("NICK %s\r\n" % NICK)
irc.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
irc.send("JOIN %s\r\n" % CHANNEL)
print irc.recv ( 4096 )

while True:
    data = irc.recv ( 4096 )
    if data.find ( 'PING' ) != -1:
        irc.send ( 'PONG ' + data.split() [ 1 ] + '\r\n' )
    if data.find ( '!botty quit' ) != -1:
        irc.send ( 'PRIVMSG #paul :Fine, if you don\'t want me\r\n' )
        irc.send ( 'QUIT\r\n' )
    if data.find ( 'hi botty' ) != -1:
        irc.send ( 'PRIVMSG #paul :I already said hi...\r\n' )
    if data.find ( 'hello botty' ) != -1:
        irc.send ( 'PRIVMSG #paul :I already said hi...\r\n' )
    if data.find ( 'KICK' ) != -1:
        irc.send ( 'JOIN #paul\r\n' )
    if data.find ( 'cheese' ) != -1:
        irc.send ( 'PRIVMSG #paul :WHERE!!!!!!\r\n' )
    if data.find ( 'slaps botty' ) != -1:
        irc.send ( 'PRIVMSG #paul :This is the Trout Protection Agency. Please put the Trout Down and walk away with your hands in the air.\r\n' )
    print data
    move = data[-6:]
    regex = re.compile('^[a-h][1-8][a-h][1-8]')
    if regex.match(move) != None:
        print move
        chessMove(move)
