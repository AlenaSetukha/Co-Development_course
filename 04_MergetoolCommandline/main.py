import cmd
import shlex
from cowsay import cowsay, list_cows, make_bubble, cowthink, Bubble 
from cowsay import wrap_bubble


MESSAGES = {'Hello,guest!', 'Hi,im_a_cow!'}
COWS = {'elephant2', 'whale', 'skeleton'}
EYES = {'oo', '00'}
TONGUE = {'U', 'W'}



def get_dict(words):
    diction = dict()

    diction['width'] = 40
    diction['message'] = ''
    diction['cow'] = 'default'
    diction['eyes'] = '00'
    diction['tongue'] = 'U'

    for w in words:
        match w:
            case '-m' | '--message':
                indx = words.index(w)
                diction['message'] = words[indx + 1] 

            case '-f' | '--file':
                indx = words.index(w)
                cow = words[indx + 1]
                if cow in list_cows():
                    diction['cow'] = cow
                else:
                    raise ValueError('Error in cow file!')
                
            case '-e' | '--eyes':
                indx = words.index(w)
                if (len(words[indx + 1]) > 2):
                    raise ValueError('Wrong eyes!')
                diction['eyes'] = words[indx + 1]

            case '-T' | '--tongue':
                indx = words.index(w)
                if (len(words[indx + 1]) > 2):
                    raise ValueError('Wrong tongue!')
                diction['tongue'] = words[indx + 1]

    return diction


def get_dict_bubble(words):
    diction = dict()

    diction['text'] = ''
    diction['wrap_text'] = True
    diction['width'] = 40
    diction['brackets'] = Bubble(stem='\\', l='<', r='>', tl='/',
            tr='\\', ml='|', mr='|', bl='\\', br='/')

    for w in words:
        match w:
            case '-t' | '--text':
                indx = words.index(w)
                diction['text'] = words[indx + 1] 

            case '--wrap_text':
                indx = words.index(w)
                if words[indx + 1] == "True":
                    diction['wrap_text'] = True
                elif words[indx + 1] == "False":
                    diction['wrap_text'] = False
                else:
                    raise ValueError('Wrong wrap_text value!')
    return diction


def give_a_hint(words, endidx):
    DICT = []
    match len(words):
        case 3:
            DICT = MESSAGES
        case _:
            if words[endidx - 1] == '-f' or words[endidx - 1] == '--file':
                DICT = COWS
            elif words[endidx - 1] == '-e' or words[endidx - 1] == '--eyes':
                DICT = EYES
            elif words[endidx - 1] == '-t' or words[endidx - 1] == '--tongue':
                DICT = TONGUE
    return DICT




class MyCmd(cmd.Cmd):
    prompt = "MyCmd>>"
    
    def do_list_cows(self, arg):
        """Lists all cow file names in the given directory"""
        print(list_cows())


    def do_cowsay(self, arg):
        """Similar to the cowsay command. Parameters are listed with their
            corresponding options in the cowsay command. Returns the resulting cowsay
            string"""
        words = shlex.split(arg)
        diction = get_dict(words)
        print(cowsay(message=diction['message'], cow=diction['cow'], 
                     eyes=diction['eyes'], tongue=diction['tongue'], width=diction['width']))
        return


    def complete_cowsay(self, text, line, begidx, endidx):
        words = (line[:endidx] + ".").split()
        DICT = give_a_hint(words, endidx)
        return [c for c in DICT if c.startswith(text) or text=='.']
    




    def do_cowthink(self, arg):
        """Similar to the cowthink command. Parameters are listed with their
            corresponding options in the cowthink command. Returns the resulting
            cowthink string"""
        words = shlex.split(arg)
        diction = get_dict(words)

        print(cowthink(message=diction['message'], cow=diction['cow'], 
                     eyes=diction['eyes'], tongue=diction['tongue'], width=diction['width']))
        return


    def complete_cowthink(self, text, line, begidx, endidx):
        words = (line[:endidx] + ".").split()
        DICT = give_a_hint(words, endidx)
        return [c for c in DICT if c.startswith(text) or text=='.']
    



    def do_make_bubble(self, arg):
        """Wraps text is wrap_text is true, then pads text and sets inside a
        bubble. This is the text that appears above the cows"""
        words = shlex.split(arg)
        diction = get_dict_bubble(words)
        if diction['wrap_text'] == True:
            print(make_bubble(text= diction['text'], brackets= diction['brackets'],
                width= diction['width'], wrap_text=True))
        else:
            print(wrap_bubble(lines= diction['text'], ops= diction['brackets']))
        return


    def complete_make_bubble(self, text, line, begidx, endidx):
        words = (line[:endidx] + ".").split()
        DICT = give_a_hint(words, endidx)
        return [c for c in DICT if c.startswith(text) or text=='.']


    def do_EOF(self):
        return 1
    





if __name__ == "__main__":
    MyCmd().cmdloop()

