import os, sys
from decoder import *
from utils_class import *
from network import *
from network_properties import *
from parameters import *


class DepModel:
    def __init__(self, train_data_file=None, word_file=None, pos_file=None, label_file=None, action_file=None,
                 model_path=None):
        """
            You can add more arguments for examples actions and model paths.
            You need to load your model here.
            actions: provides indices for actions.
            it has the same order as the data/vocabs.actions file.
        """

        if word_file and pos_file and label_file and action_file and model_path:
            # creating vocabulary files
            self.word = Word(word_file)
            self.pos = Pos(pos_file)
            self.label = Label(label_file)
            self.action = Action(action_file)
            self.actions = self.action.id_action
            self.model_path = model_path

            # creating network properties
            self.properties = NetProperties(word_embed_dim, pos_embed_dim, label_embed_dim, first_hidden_dim,
                                            second_hidden_dim,mini_batch_size)

        if train_data_file and model_path:
            # constructing network
            self.network = Network(self.word, self.pos, self.label, self.action, self.properties);

            # training
            self.network.train(train_data_file, epochs)

            # saving network
            self.network.save(model_path)

        if train_data_file is None and model_path:
            self.network = Network(self.word, self.pos, self.label, self.action, self.properties);
            self.network.load(model_path)

    def score(self, str_features):
        """
         :param str_features: String features
         20 first: words, next 20: pos, next 12: dependency labels.
         DO NOT ADD ANY ARGUMENTS TO THIS FUNCTION.
         :return: list of scores
        """
        # change this part of the code
        # constructing network
        # print(str_features[0])
        network = self.network

        # loading network trained model
        word_feat, pos_feat, label_feat = str_features[0:20], str_features[20:40], str_features[40:52]

        for i in range(len(word_feat)):
            if word_feat[i] not in self.word.word_id:
                word_feat[i] = '<unk>'

        for i in range(len(pos_feat)):
            if pos_feat[i] not in self.pos.pos_id:
                pos_feat[i] = '<null>'

        for i in range(len(label_feat)):
            if label_feat[i] not in self.label.label_id:
                label_feat[i] = '<null>'

        # running forward
        output = network.build_graph(word_feat, pos_feat, label_feat)

        # getting list value of the output
        scores = output.npvalue()

        # dynet.renew_cg()
        return scores


if __name__ == '__main__':
    m = DepModel(train_data_file, word_file, pos_file, label_file, action_file, model_path)
    # input_p = 'trees/dev.conll'
    # output_p = 'cd_outputs/dev_part1.conll'
    input_p = os.path.abspath(sys.argv[1])
    output_p = os.path.abspath(sys.argv[2])
    # Decoder(m.score, m.actions).parse(input_p, output_p)
