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
        
        sdf
        
    def get_players_list(self, *args):
        if args > 0:
            for game, players in self.game:
                if game in args:
                    return game, players
        else:
            return self.players 
    
    def on_player_add(self, player, args):
        if args[0] in 'all':
            for key in self.game:
                    self.game[key].append(player)
            return 'You been added to %s ' % ', '.join(self.game.keys())
        else:
            self.added_to = []
            self.already_added = []
            for game in args:
                if game in self.game:
                    if player in self.game[game]:
                        self.already_added.append(game)
                    else:
                        self.game[game].append(player)
                        self.added_to.append(game)
            return 'You have been added to %s ' %', '.join(self.added_to) 
                
    def on_player_remove(self, player, game):
        self.remove_list = []
        for i in game:
            if i in 'all':
                for k in self.game:
                    if player in self.game[k]:
                        self.game[k].remove(player)
                return 'You have been removed from all games'
            elif i in self.game:
                if player in self.game[i]:
                    self.game[i].remove(player)
                    self.remove_list.append(i)
        print self.remove_list
        return 'You have been removed from: %s ' % ', '.join(self.remove_list)
    
    def on_game_start(self, playerList):
        pass
    
    def get_games(self):
        return self.game
    

        