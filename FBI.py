# Token types
#
# EOF token is used to indicate that there is no more input left for lexical analysis

CALL, FPOS, FORMATION, MOTION, PERSONNEL, SHIFT, STRENGTH, TPOS = \
    'CALL', 'FPOS', 'FORMATION', 'MOTION', 'PERSONNEL', 'SHIFT', 'STRENGTH', 'TPOS'


class Play(object):
    def __init__(self, **kwargs):
        # receive the input from the interpreter and construct a play object
        self.text = {'call': kwargs['call'], 'personnel': kwargs['personnel'], 'formation': kwargs['formation'],
                     'strength': kwargs['strength'], 'fpos': kwargs['fpos'], 'shift': kwargs['shift'],
                     'motion': kwargs['motion'], 'tpos': kwargs['tpos']}

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        result = ""
        for key in self.text:
            if self.text[key] is not None:
                result += self.text[key].__str__() + ", "
        return result.strip(' ,')

    @staticmethod
    def SVG_writer(width: int, height: int, file: str = "output.svg") -> None:
        output_file = open(file, 'w')
        output_file.write(
            "<?xml version=\"1.0\"?>\n<!DOCTYPE svg PUBLIC \"-//W3C//DTD SVG 1.1//EN\"\n\t\"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd\">\n")
        output_file.write(
            "<svg xmlns=\"http://www.w3.org/2000/svg\"\n\twidth=\"{}\" height=\"{}\">".format(width, height))
        # Put contents of svg file here
        output_file.write("</svg>")
        return None


class Player(object):
    # An object for each player on the field
    def __init__(self, position, shape, symbol):
        self.position = position
        self.shape = shape
        self.symbol = symbol


class Token(object):
    call = ['power', 'iso', 'counter']  # the play call
    fpos = ['far', 'near', 'strong', 'weak']  # locates the F
    formation = ['doubles', 'flex', 'off', 'pro', 'twins']  # locates the Y and Z
    motion = ['none']  # motion at snap
    personnel = ['none']
    shift = ['none']  # pre-snap shift
    strength = ['right', 'left']  # the side for Y
    tpos = ['spread', 'split']

    def __init__(self, type, value):
        # token type: CALL, FPOS, FORMATION, MOTION, PERSONNEL, SHIFT, STRENGTH
        self.type = type
        # token value
        self.value = value

    def __str__(self):
        """String representation of the class instance.

        Examples:
             Token(FORMATION, PRO)
             Token(STRENGTH, RIGHT)
        """
        return 'Token({type}, {value})'.format(type=self.type, value=repr(self.value))

    def __repr__(self):
        return self.__str__()


class Interpreter(object):
    def __init__(self, text):
        # client string input, e.g. "pro right near power right"
        self.text = text
        # self.pos is an index into self.text
        self.pos = 0
        # current token instance
        self.current_token = None

    def error(self):
        raise ValueError("Error parsing input")

    def get_next_token(self):
        """Tokenizer (lexical analyzer). This method is responsible for breaking the input string apart into tokens,
        one token at a time.
        """
        try:
            token = self.text.split()[self.pos]
        except IndexError:
            return
        if token in Token.call:
            token = Token(CALL, token)
        elif token in Token.fpos:
            token = Token(FPOS, token)
        elif token in Token.formation:
            token = Token(FORMATION, token)
        elif token in Token.motion:
            token = Token(MOTION, token)
        elif token in Token.personnel:
            token = Token(PERSONNEL, token)
        elif token in Token.shift:
            token = Token(SHIFT, token)
        elif token in Token.strength:
            token = Token(STRENGTH, token)
        elif token in Token.tpos:
            token = Token(TPOS, token)
        else:
            self.error()
        return token

    def eat(self, token_type):
        # compare the current otken type with the passed token type and if they match then "eat" the current token
        # and assign the next token to the self.current_token, otherwise raise an exception.

        result = None
        if self.current_token.type == token_type:
            # if we validate the token, return it
            result = self.current_token
            self.pos += 1
            self.current_token = self.get_next_token()

        # Note that personnel, motion, and shift calls are optional. If they are not present, do not shift forward
        elif token_type == PERSONNEL or token_type == MOTION or token_type == SHIFT or token_type == TPOS:
            # If we cannot validate an optional token, set it to None
            result = None
        else:
            self.error()
        return result

    def expr(self):
        # set current token to the first token taken from the input
        self.current_token = self.get_next_token()

        # the expected format is PERSONNEL FORMATION STRENGTH TPOS FPOS SHIFT MOTION CALL
        personnel = self.eat(PERSONNEL)
        formation = self.eat(FORMATION)
        strength = self.eat(STRENGTH)
        tpos = self.eat(TPOS)
        fpos = self.eat(FPOS)
        shift = self.eat(SHIFT)
        motion = self.eat(MOTION)
        call = self.eat(CALL)

        # TODO: Once we've tokenized the play call, build a play object
        play = Play(personnel=personnel, formation=formation, strength=strength, tpos=tpos, fpos=fpos, shift=shift, motion=motion,
                    call=call)
        return play


def main(*args):
    text = input('play> ')
    interpreter = Interpreter(text)
    result = interpreter.expr()
    print(result)


main()
