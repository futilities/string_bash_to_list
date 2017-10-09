import sys
class BashStringToList:
    """
    This class converts a string of a bash command with its arguments into a list for some use ....
    """

    def __init__(self):
        pass

    def convert(self,bash_command_string):
        split_bash = bash_command_string.split()

        bash_command_argument_list = []
        temp_arg = ''
        for i,c in enumerate(split_bash):
            if i == 0:
                bash_command_argument_list.append(c)
                continue
            if split_bash[i][0] == '-':
                temp_arg = c
            elif split_bash[i][0] != '-':
                temp_arg = temp_arg + ' ' + c 

            if len(split_bash) < i+2 or split_bash[i+1][0] == '-':
                bash_command_argument_list.append(temp_arg)
        return bash_command_argument_list

if __name__ == "__main__":
    
    if len(sys.argv) > 1:
        bash_string = sys.argv[1]
    else:
        bash_string = '/path/to/some/command -y -hide_banner -loglevel panic  -i /some/stuff/gif -i /I/am/a/cat/ -i /poof/puff/stfuf/Tem -filter_complex " [0:v]trim=duration=7[a];   [1:v]trim=duration=5[b];   [2:v]trim=duration=5[c];   [3:v]trim=duration=3[d];  [a][b][c][d] concat=n=4:v=1:a=0 [v]"  -filter_complex " [0:a]atrim=duration=7[a];   [1:a]atrim=duration=5[b];   [2:a]atrim=duration=5[c];   [3:a]atrim=duration=3[d];  [a][b][c][d] concat=n=4:v=0:a=1 [a]" -map "[v]"  -map "[a]" /Users/pewpewl.mp4'
    bs2l = BashStringToList()
    print bs2l.convert(bash_string)
