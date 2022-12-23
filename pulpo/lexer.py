from pulpo.ply.lex import lex


literals = '+-*/%()'

tokens = ('INTDIV', 'NUMBER')

def get_lexer(*args, **kwargs):
    # token rules
    t_INTDIV = r'//'
    t_NUMBER = r'-?(0|[1-9][0-9]*)(\.[0-9]*)?'

    # ignore spaces and tabs
    t_ignore = r' \t'

    return lex(*args, **kwargs)
