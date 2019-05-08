from collections import defaultdict


class Word:
    def __init__(self, data_path):
        sentences = open(data_path, 'r').read().strip().split('\n')

        word_id = defaultdict(int)
        id_word = defaultdict(str)
        for sentence in sentences:
            line = sentence.strip().split(' ')
            word_id[line[0]] = int(line[1])
            id_word[int(line[1])] = line[0]

        self.word_id = word_id
        self.id_word = id_word

    def word2id(self, word):
        return self.word_id[word]

    def id2word(self, id):
        return self.id_word[id]

    def num_words(self):
        return len(self.word_id)


class Pos:
    def __init__(self, data_path):
        sentences = open(data_path, 'r').read().strip().split('\n')

        pos_id = defaultdict(int)
        id_pos = defaultdict(str)
        for sentence in sentences:
            line = sentence.strip().split(' ')
            pos_id[line[0]] = int(line[1])
            id_pos[int(line[1])] = line[0]

        self.pos_id = pos_id
        self.id_pos = id_pos

    def pos2id(self, pos):
        return self.pos_id[pos]

    def id2pos(self, id):
        return self.id_pos[id]

    def num_pos(self):
        return len(self.pos_id)


class Label:
    def __init__(self, data_path):
        sentences = open(data_path, 'r').read().strip().split('\n')

        label_id = defaultdict(int)
        id_label = defaultdict(str)
        for sentence in sentences:
            line = sentence.strip().split(' ')
            label_id[line[0]] = int(line[1])
            id_label[int(line[1])] = line[0]

        self.label_id = label_id
        self.id_label = id_label

    def label2id(self, label):
        return self.label_id[label]

    def id2label(self, id):
        return self.id_label[id]

    def num_labels(self):
        return len(self.label_id)


class Action:
    def __init__(self, data_path):
        sentences = open(data_path, 'r').read().strip().split('\n')

        action_id = defaultdict(int)
        id_action = defaultdict(str)
        for sentence in sentences:
            line = sentence.strip().split(' ')
            action_id[line[0]] = int(line[1])
            id_action[int(line[1])] = line[0]

        self.action_id = action_id
        self.id_action = id_action

    def action2id(self, action):
        return self.action_id[action]

    def id2action(self, id):
        return self.id_action[id]

    def num_actions(self):
        return len(self.action_id)
