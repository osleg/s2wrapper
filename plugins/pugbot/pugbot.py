'''
Created on Jan 6, 2012

@author: alex
'''

class PugBot(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.game = {
                 'duel': [],
                 '6v6': [],
                 '11v11': [],
                 }
        
        self.players = []
        
        
        
    def get_players_list(self, *args):
        if args > 0:
            for game, players in self.game:
                if game in args:
                    return game, players
        else:
            return self.players 
    
    def on_player_add(self, player, game):
        if game in self.game:
            if player in self.game[game]:
                return 'aAdded'
            else:
                self.game[game].append(player)
                return 'Added' 
        else:
            return 'Wrong'
    
    def on_player_remove(self, player, game):
        pass
    
    def on_game_start(self, playerList):
        pass
    
    def get_games(self):
        return self.game
    

        