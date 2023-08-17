import pygame
from pong import Game

import neat 
import os
import pickle

class PongGame:
    def __init__(self,window,width,height):
        self.game = Game(window,width,height)
        self.left_paddle = self.game.left_paddle
        self.right_paddle = self.game.right_paddle
        self.ball = self.game.ball
        
    def test_ai(self, net):
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(180)
            game_info = self.game.loop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

            output = net.activate((self.ball.x_vel,self.right_paddle.y, abs(self.right_paddle.x - self.ball.x), self.ball.y))
            decision = output.index(max(output))

            if decision == 1:  # AI moves up
                self.game.move_paddle(left=False, up=True)
            elif decision == 2:  # AI moves down
                self.game.move_paddle(left=False, up=False)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.game.move_paddle(left=True, up=True)
            elif keys[pygame.K_s]:
                self.game.move_paddle(left=True, up=False)

            self.game.draw(draw_score=True)
            pygame.display.update()
    
    def train_ai(self, genome1,genome2,config):
        net1 = neat.nn.FeedForwardNetwork.create(genome1, config)
        net2 = neat.nn.FeedForwardNetwork.create(genome2, config)
        
        
        run = True
        while run:
            # put in a way to quit the game as well
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
            
            # this is having the 3 input nodes being (height of paddle,location of ball, distance to the ball)
            output1 = net1.activate((self.left_paddle.y,self.ball.y,self.ball.x_vel,abs(self.left_paddle.x-self.left_paddle.y))) 
            # will give the index of 1 move up, 0 stay still, and -1 to move down
            decision1 = output1.index(max(output1))
            if decision1==0:
                pass
            elif decision1 ==1:
                self.game.move_paddle(left=True,up=True)
            else:
                self.game.move_paddle(left= True,up =False)
            
            
            output2 = net2.activate((self.right_paddle.y,self.ball.y,self.ball.x_vel,abs(self.right_paddle.x-self.right_paddle.y)))     
            decision2 = output2.index(max(output2))
            if decision2==0:
                pass
            elif decision2 ==1:
                self.game.move_paddle(left=False,up=True)
            else:
                self.game.move_paddle(left= False,up =False)
            
            
            
            
            game_info = self.game.loop()
            self.game.draw(draw_score=False,draw_hits=True)
            pygame.display.update()
            
            # basically stops the game if one of the bats misses the ball
            # as most of the ai will be bad, it'll speed up the inital ones
            if game_info.left_score == 1 or game_info.right_score == 1 or game_info.left_hits >= 50:
                self.calculate_fitness(genome1,genome2,game_info)
                break
                
    def calculate_fitness(self, genome1, genome2, game_info):
        genome1.fitness += game_info.left_hits
        genome2.fitness += game_info.right_hits
    
                
# eval method used is round robin of ai's in generation to find the best of them (takes
# longer but is meant to be better)
def eval_genomes(genomes, config):
    width,height = 700,500
    # can disable flags=pygame.HIDDEN to show the game window in training mode
    win = pygame.display.set_mode((width, height), flags=pygame.HIDDEN)
    pygame.display.set_caption("Pong")
    
    # genomes is list of tuples with the ID of genome and genome object
    for i, (genome_id1,genome1) in enumerate(genomes):
        # second for and enumerate used to not have the round robin involving 
        # ai's playing themselves too many times
        if i == len(genomes)-1:
            break
        # genomes don't have fitness by default, so initialising it here
        genome1.fitness = 0
        for genome_id2,genome2 in genomes[min((i+1),len(genomes)-1):]:
            # basically don't want to set the fitness to zero if genome2 has already played some 
            # of the games in the round robin
            if (genome_id1==genome_id2):
                continue
            genome2.fitness = 0 if genome2.fitness ==None else genome2.fitness 
            game = PongGame(win,width,height)
            game.train_ai(genome1,genome2,config)
            
        
def run_neat(config):
    # to restore from previous checkpointer use:
    p=neat.Checkpointer.restore_checkpoint('checkpoints/trained-final-50')

    # setup pop using config files
    # p = neat.Population(config)
    # setup reporters
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    # saves reporter at each point, so can run and restart over few days (Checkpointer(gen=1) does this)
    p.add_reporter(neat.Checkpointer(1,filename_prefix='checkpoints/trained-final-'))
    # 50 is max N.o. of generations to run for , winner is the best nn
    winner = p.run(eval_genomes,1)
    
    with open("gh-commit-final.pickle","wb") as f:
        pickle.dump(winner,f)
    
def test_best_network(config):
    with open("final.pickle", "rb") as f:
        winner = pickle.load(f)
    winner_net = neat.nn.FeedForwardNetwork.create(winner, config)

    width, height = 700, 500
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pong")
    pong = PongGame(win, width, height)
    pong.test_ai(winner_net)


if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')

    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)

    # run_neat(config)
    test_best_network(config)


    

