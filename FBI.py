import svgwrite

CALL, FPOS, FORMATION, MOTION, PERSONNEL, SHIFT, STRENGTH, TPOS = \
    'CALL', 'FPOS', 'FORMATION', 'MOTION', 'PERSONNEL', 'SHIFT', 'STRENGTH', 'TPOS'

LT, LG, C, RG, RT, FB, TB, Z, X, Y, QB = 'LT', 'LG', 'C', 'RG', 'RT', 'FB', 'TB', 'Z', 'X', 'Y', 'QB'


class Play(object):
    locations = dict(LT=(204, 240), LG=(222, 240), C=(237, 237), RG=(258, 240), RT=(276, 240), QB=(240, 258))
    positions = [LT, LG, C, RG, RT, FB, TB, Z, X, Y, QB]

    def __init__(self, **kwargs):
        # receive the input from the interpreter and construct a play object
        self.text = {'call': kwargs['call'], 'personnel': kwargs['personnel'], 'formation': kwargs['formation'],
                     'strength': kwargs['strength'], 'fpos': kwargs['fpos'], 'shift': kwargs['shift'],
                     'motion': kwargs['motion'], 'tpos': kwargs['tpos']}
        self.raw = kwargs['raw']
        self.dwg = svgwrite.Drawing(filename='{name}.svg'.format(name=self.raw), size=(480, 480))
        offense = self.dwg.add(self.dwg.g(id='offense', stroke='black', fill='white'))
        for player in Play.positions:
            if player == C:
                offense.add(self.dwg.rect(id=player, insert=Play.locations[player],
                                          size=(6, 6), stroke='black',
                                          fill='white'))
            elif player in [LT, LG, RG, RT, QB]:
                offense.add(self.dwg.circle(id=player, center=Play.locations[player],
                                            r=3, stroke='black',
                                            fill='white'))
            elif player == Y:
                if kwargs['formation'].value in ['doubles', 'twins', 'pro']:
                    if kwargs['strength'].value == 'right':
                        offense.add(self.dwg.circle(id=player, center=(294, 240), r=3, stroke='black', fill='white'))
                    else:
                        offense.add(self.dwg.circle(id=player, center=(186, 240), r=3, stroke='black', fill='white'))
                elif kwargs['formation'].value == 'off':
                    if kwargs['strength'].value == 'right':
                        offense.add(self.dwg.circle(id=player, center=(294, 231), r=3, stroke='black', fill='white'))
                    else:
                        offense.add(self.dwg.circle(id=player, center=(186, 231), r=3, stroke='black', fill='white'))
                elif kwargs['formation'].value == 'flex':
                    if kwargs['strength'].value == 'right':
                        offense.add(self.dwg.circle(id=player, center=(330, 240), r=3, stroke='black', fill='white'))
                    else:
                        offense.add(self.dwg.circle(id=player, center=(150, 240), r=3, stroke='black', fill='white'))
            elif player == FB:
                if kwargs['fpos'].value in ['near', 'far']:
                    if kwargs['strength'].value == 'right':
                        offense.add(self.dwg.circle(id=player, center=(258, 252), r=3, stroke='black', fill='white'))
                    else:
                        offense.add(self.dwg.circle(id=player, center=(222, 252), r=3, stroke='black', fill='white'))
                elif kwargs['fpos'].value == 'weak':
                    if kwargs['strength'].value == 'right':
                        offense.add(self.dwg.circle(id=player, center=(168, 246), r=3, stroke='black', fill='white'))
                    else:
                        offense.add(self.dwg.circle(id=player, center=(348, 246), r=3, stroke='black', fill='white'))
                elif kwargs['fpos'].value == 'strong':
                    if kwargs['strength'].value == 'right':
                        offense.add(self.dwg.circle(id=player, center=(348, 246), r=3, stroke='black', fill='white'))
                    else:
                        offense.add(self.dwg.circle(id=player, center=(168, 246), r=3, stroke='black', fill='white'))
            elif player == TB:
                if kwargs['tpos']:
                    if kwargs['tpos'].value == 'split':
                        offense.add(self.dwg.circle(id=player, center=(132, 246), r=3, stroke='black', fill='white'))
                    elif kwargs['tpos'].value == 'spread':
                        offense.add(self.dwg.circle(id=player, center=(364, 246), r=3, stroke='black', fill='white'))
                else:
                    offense.add(self.dwg.circle(id=player, center=(240, 274), r=3, stroke='black', fill='white'))
            elif player == X:
                if kwargs['formation'] != 'doubles':
                    if kwargs['strength'].value == 'right':
                        offense.add(self.dwg.circle(id=player, center=(18, 240), r=3, stroke='black', fill='white'))
                    else:
                        offense.add(self.dwg.circle(id=player, center=(468, 240), r=3, stroke='black', fill='white'))
                else:
                    if kwargs['strength'].value == 'right':
                        offense.add(self.dwg.circle(id=player, center=(18, 246), r=3, stroke='black', fill='white'))
                    else:
                        offense.add(self.dwg.circle(id=player, center=(468, 246), r=3, stroke='black', fill='white'))
            elif player == Z:
                if kwargs['formation'].value == 'doubles':
                    if kwargs['strength'].value == 'right':
                        offense.add(self.dwg.circle(id=player, center=(54, 240), r=3, stroke='black', fill='white'))
                    else:
                        offense.add(self.dwg.circle(id=player, center=(432, 240), r=3, stroke='black', fill='white'))
                elif kwargs['formation'].value == 'twins':
                    if kwargs['strength'].value == 'right':
                        offense.add(self.dwg.circle(id=player, center=(54, 246), r=3, stroke='black', fill='white'))
                    else:
                        offense.add(self.dwg.circle(id=player, center=(432, 246), r=3, stroke='black', fill='white'))
                elif kwargs['formation'].value == 'off':
                    if kwargs['strength'].value == 'right':
                        offense.add(self.dwg.circle(id=player, center=(468, 240), r=3, stroke='black', fill='white'))
                    else:
                        offense.add(self.dwg.circle(id=player, center=(18, 246), r=3, stroke='black', fill='white'))
                elif kwargs['formation'].value in ['pro', 'flex']:
                    if kwargs['strength'].value == 'right':
                        offense.add(self.dwg.circle(id=player, center=(468, 246), r=3, stroke='black', fill='white'))
                    else:
                        offense.add(self.dwg.circle(id=player, center=(18, 246), r=3, stroke='black', fill='white'))

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        result = ""
        for key in self.text:
            if self.text[key] is not None:
                result += self.text[key].__str__() + ", "
        return result.strip(' ,')

    def draw(self):
        self.dwg.save()


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
        fpos = self.eat(FPOS)
        tpos = self.eat(TPOS)
        shift = self.eat(SHIFT)
        motion = self.eat(MOTION)
        call = self.eat(CALL)

        # TODO: Once we've tokenized the play call, build a play object
        play = Play(raw=self.text, personnel=personnel, formation=formation, strength=strength, tpos=tpos, fpos=fpos,
                    shift=shift,
                    motion=motion,
                    call=call)
        play.draw()
        return play


def main(*args):
    text = input('play> ')
    interpreter = Interpreter(text)
    result = interpreter.expr()
    print(result)


main()
