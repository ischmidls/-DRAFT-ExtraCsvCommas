"""
changeCsv.py

This file deletes extra commas

"""


class Spaces:
    def __init__(self, file):
        self.i_file = file

    def space_comma(self, o_file):
        new = open(o_file, 'w+')
        for i_line in open(self.i_file, 'r'):
            line_string = str(i_line.strip().split(' '))[1:-1]
            temp = ''
            for ch in line_string:
                if ch != '\'':
                    temp += ch
                line_string = temp
            new.writelines(line_string + '\n')
    def del_last(self):
        pass

class Pairs:
    def __init__(self, ll):
        self.temp = ''  # INITIALIZE NEW LINE
        self.num = ''  # INITIALIZE COUNTER
        self.ll = ll

    def sentinel(self):
        s = ','  # ^^ SENTINEL
        i = 0  # ^^ INDEX
        while not s:  # WHILE SENTINEL NOT COMMA
            ch = self.ll[i]  # GET CHARACTER IN LINE
            i += 1  # ADD 1 TO INDEX
            s = ch  # SENTINEL = CHARACTER
            self.temp += ch  # ADD CHARACTER TO NEW LINE
        for ch in self.ll[1:]:
            if ch != ",":
                self.temp += ch
        print(f'{self.temp}=temp {self.ll}=ll')

    def del_com(self):
        """
        >>> ls = ["d,o,g", "d,,og", ",dog,"]
        >>> del_com(ls)
        ["d,og", "d,og", ",dog"]
        """
        for ch in self.ll:
            if ch == ",":
                self.num += ch  # COUNT COMMAS
        if len(self.num) > 1:  # IF MORE THAN ONE COMMA IN LINE
            self.sentinel()
        if self.temp == '':
            return self.ll.split(',')
        else:
            return self.temp.split(',')


if __name__ == '__main__':
    main()
