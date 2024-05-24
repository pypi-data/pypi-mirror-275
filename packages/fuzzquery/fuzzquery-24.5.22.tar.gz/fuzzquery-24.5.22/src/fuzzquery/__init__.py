"""A lightweight package for fuzzy word/phrase searches in a body of text, using a very simple token system.

project: https://pypi.org/project/fuzzquery/

version: 24.5.22

author: OysterShucker

tokens:
 - "{x}"  : from 0 to x non-whitespace characters
 - "{!x}" : exactly x non-whitespace characters
 - "{?}"  : 0 or more unknown words
    
query examples:
 - "home{5}"       : home, homer, homely, homeward, homestead
 - "bomb{!2}"      : bomber, bombed
 - "bomb{!2}{3}"   : bomber, bombed, bombers, bombastic
 - "thou {?} kill" : thou shalt not kill
 - "{2}ward{!2}"   : warden, awarded, rewarded
 * "{4}{!3}-{!4}"  : 504-525-5555, 867-5309, more-or-less
 
 * searches this broad are bound to return some unwanted results
"""
import regex
from typing import Iterator

__all__ = 'finditer', 'findany', 'iterall'

REPL  = '`'                                  # character to represent substitution and deletion points
TOKEN = regex.compile(r'\{(!{0,1}\d+|\?)\}') # for splitting on token guts
FLAGS = regex.V1, regex.V1|regex.I           # case-sensitive, case-insensitive

# https://github.com/mrabarnett/mrab-regex?tab=readme-ov-file#approximate-fuzzy-matching-hg-issue-12-hg-issue-41-hg-issue-109
FORMAT = {
    '.':r'{{{over}i+1d+1s<={limit}:\S}}',    # allowed range of mixed substitutions and deletions
    '!':r'{{{limit}<=s<={limit}:\S}}'   ,    # strict amount of substitutions only
    '?':r'([\w\W]+?(?=\s))*?'           ,}   # 0 or more unknown words 
    
# convert query to expression
def __expr(query:str, group:bool=True) -> str:

    # convert term segment to expression
    def subexpr(segment:str) -> str:
        
        # assume this is a token and get alleged integer range
        limit = int(''.join(filter(str.isdigit, segment)) or 0)
        
        # alias some facts
        d, t  = segment.isdigit(), segment[0]
        
        # if range or strict get replacement characters group
        expr  = ('', fr'({REPL * limit})')[d | (t == '!')] 
        
        # append respective value and format compatible results with limits
        expr += FORMAT.get((t, '.')[d], regex.escape(segment)).format(over=limit+1, limit=limit)
        
        return expr
    
    # term segments
    segmap = filter(None, map(TOKEN.split, query.split(' ')))
    
    # generator of terms from processed term segments
    terms = (r''.join(map(subexpr, filter(None, segments))) for segments in segmap)
    
    # join terms with conditional spacing
    expr  = r'((?<=\s)|\s)+?'.join(terms)
    
    # create final expression
    return f'{"("*group}{expr}{")"*group}'
   
# execute final expression on text
def __exec(expr:str, text:str, skip:None|list|tuple|set=None, ci:bool=False) -> Iterator:
    skip = skip or []
    
    for match in regex.finditer(expr, text, flags=FLAGS[ci]):
        result = match['result']
        
        # determine if result should be skipped
        for item in skip:
            if item in result: break
        else:
            yield match.span(), result

def finditer(text:str, query:str, **kwargs) -> Iterator:
    """Format query into an expression and yield matches
    
     - text    : str
       the text to be searched
         
     - query   : str
       str of term(s) to search for
         
     ** skip   : list|tuple|set, optional
       words and/or characters that trigger a skip when found in a result
         
     ** ci     : bool, optional
       case insensitive matching  
         
     return tuple of query results (`span`, `results`)
    """
    expr = fr'\m(?P<result>{__expr(query, False)})\M'
    
    for span, result in __exec(expr, text, **kwargs):
        yield span, result
          
def findany(text:str, queries:list|tuple|set, **kwargs) -> Iterator:
    """Format and OR queries into a singular expression and yield matches
    
     - text    : str
       the text to be searched
       
     - queries : list|tuple|set
       Iterable of search terms
       
     ** skip   : list|tuple|set, optional
       words and/or characters that trigger a skip when found in a result
       
     ** ci     : bool, optional
       case insensitive matching  
     
     return tuple of query results (`span`, `results`)
    """
    expr = r'|'.join(map(__expr, queries))
    expr = fr'\m(?P<result>{expr})\M'
    
    for span, result in __exec(expr, text, **kwargs):
        yield span, result

def iterall(text:str, queries:list|tuple|set, **kwargs) -> Iterator: 
    """Yield from multiple consecutive queries
     
     - text    : str
       the text to be searched
       
     - queries : list|tuple|set
       Iterable of search terms
       
     ** skip   : list|tuple|set, optional
       words and/or characters that trigger a skip when found in a result
       
     ** ci     : bool, optional
       case insensitive matching  
     
     return tuple of query results (`query`, `span`, `results`)
    """
    for query in queries:
        q = query
            
        for span, match in finditer(text, query, **kwargs):
            yield q, span, match
            q = None # only yield `query` on first match

