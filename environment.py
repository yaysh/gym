class Environment:


    #game_title = game title to be loaded from gym environment

    #state_size gives the input dimensions for the model
    #   - the number of data points saved from each state
    #action_size gives the output dimensions for the model
    #   - the number of actions that can be done
    def __init__(self, game_title, state_size, action_size):
        self.env = gym.make(game_title)        
        self.state = env.reset()

        # #Input dimensions for model
        self.state_size = env.observation_space.shape[0]
        # #Output dimensions for model
        self.action_size = env.action_space.n