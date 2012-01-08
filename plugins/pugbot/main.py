import logging
import sys

from twisted.internet import reactor

#from masterserver import get_auth_token
#from chatserver import ChatClientFactory
from irc import RelayBotFactory
from controller import Controller

# Configuration
CHATHOST="chatserver.savage2.s2games.com"
CHATPORT=11030
MASTERHOST="masterserver.savage2.s2games.com"
MASTERPORT=80
MASTERURL="/irc_updater/irc_requester.php"
IRCHOST="irc.s2games.com"
IRCPORT=6667

USERNAME="Osleg"
PASSWORD="inSR6gEW"
ACCOUNTID=206933
IRCNAME="pugbot"
IRCCHANNEL="#pug"

def main():
    # Set up logging
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

    # To login to the chat server, we need an authentification token which
    # we can receive by logging into the master server.
#    token = get_auth_token(MASTERHOST, MASTERURL, USERNAME, PASSWORD)

    # Create factory for IRC connection
    i = RelayBotFactory(IRCCHANNEL, IRCNAME)

    # Create factory protocol and application for chat server
#    f = ChatClientFactory(token, ACCOUNTID)

    # Create controller object that provides actual logic
    c = Controller(i)

    # Connect to network
#    reactor.connectTCP(CHATHOST, CHATPORT, f)
    reactor.connectTCP(IRCHOST, IRCPORT, i)

    # Run bot
    reactor.run()

# Only run when module was not imported
if __name__ == '__main__':
    main()
