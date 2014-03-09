dna = 'ATGATTTTTCCATCTTTAAGTGCGATACTGTTTTGT'
dna_bases = ['A', 'C', 'G', 'T']
rna_bases = ['A', 'C', 'G', 'U'] 
basecomplement = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'} 

def is_dna(dna):
    """
    Checks whether a string is a DNA string.

    Parameters
    ----------
    dna : string
        A string (i.e., you can assume you get a string)

    Returns
    -------
    out : bool
        Returns True, if dna is a valid DNA string (i.e,
        a string composed of the letters 'A', 'C', 'G', or
        'T' (and False otherwise).

    Hint
    ----
    You may want to iterate over the string checking each character.

    Examples
    --------
    >>> is_dna('ATGATT')
    True
    >>> is_dna('ATGATU')
    False
    >>> is_dna('atgatt')
    False
    >>> is_dna('My grandMa')
    False
    """
    return len(dna.translate(None, 'ACGT')) == 0

def is_rna(rna):
    """
    Checks whether a string is a DNA string.

    Parameters
    ----------
    rna : string
        A valid RNA string

    Returns
    -------
    out : bool
        Returns True, if rna is a valid RNA string (i.e,
        a string composed of the letters 'A', 'C', 'G', or
        'U' (and False otherwise).

    Hint
    ----
    See is_dna above.

    Examples
    --------
    >>> is_rna('ATGATT')
    False
    >>> is_rna('ATGATU')
    False
    >>> is_rna('atgatt')
    False
    >>> is_rna('AUGAUU')
    True
    >>> is_rna('CCCCCC')
    True
    """
    return len(dna.translate(None, 'ACGU')) == 0

def transcribe(dna):
    """
    Transcribes a DNA string into a RNA string.

    Parameters
    ----------
    dna : string
        A valid DNA string

    Returns
    -------
    out : string
        The RNA string is identical to the DNA string that
        it was transcribed from except all occurrences of
        the letter 'T' are replaced with the letter 'U'

    Hint
    ----
    You may want to iterate over the string building up a new string character
    by character (use the '+' operator).
    

    Examples
    --------
    >>> transcribe('ATGATT')
     'AUGAUU'
    """
    if is_dna(dna):
        return dna.replace('T', 'U')

def reverse(dna):
    """
    Return the DNA string in reverse order.

    Parameters
    ----------
    dna : string
        A valid DNA string

    Returns
    -------
    out : string

    Hint
    ----
    You may want to iterate over the string building up a new string character
    by character (use the '+' operator appending to the front of the string).

    Examples
    --------
    >>> reverse('ATGATT')
    'TTAGTA'
    """
    if is_dna(dna):
        return dna[::-1]

def complement(dna):
    """
    Return the complementary DNA string.

    Parameters
    ----------
    dna : string
        A valid DNA string

    Returns
    -------
    out : string

    Hint
    ----
    You may want to iterate over the string building up a new string character
    by character.

    Examples
    --------
    >>> complement('ATGATT')
    'TACTAA'
    """
    if is_dna(dna):
        result = ''
        for a in dna:
            result += basecomplement[a]
        return result

def is_complement(strand1, strand2):
    """
    Return the complementary DNA string.

    Parameters
    ----------
    strand1 : string
        A valid DNA string
    strand2 : string
        A valid DNA string

    Returns
    -------
    out : bool

    Hint
    ----
    You may want to use your complement function ...

    Examples
    --------
    >>> is_complement('ATGATT', 'TACTAA')
    True
    >>> is_complement('ATGATT', 'TACTAT')
    False
    """
    return complement(strand1) == strand2

def reversecomplement(dna):
    """
    Return the complement of the reverse of the DNA string.

    Parameters
    ----------
    dna : string
        A valid DNA string

    Returns
    -------
    out : string

    Hint
    ----
    Use function composition with functions you already defined.

    Examples
    --------
    >>> reversecomplement('TACTAA')
    'TTAGTA'
    """ 
    return complement(dna[::-1])

def gc_content(dna):
    """
    Return the proportion of Gs and Cs in the DNA string.

    Parameters
    ----------
    dna : string
        A valid DNA string

    Returns
    -------
    out : float

    Hint
    ----
    You may want to look over your lecture notes (i.e., the Algorithm nb).
    But you should not just report counts.  It isn't necesary, but you
    can use the len function to get the length of a string.

    Examples
    --------
    >>> gc_content('TACTAA')
    0.16666666666666666
    """
    if is_dna(dna):
        return float(dna.count('G') + dna.count('C'))/len(dna)

def get_codons(dna):
    """
    Return list of codons for the DNA string.

    Parameters
    ----------
    dna : string
        A valid DNA string

    Returns
    -------
    out : list

    Hint
    ----
    You should check that the length of the string is divisible by 3
    (the modulus operator may be helpful).  Then go through the string
    grabbing three characters at time and appending them to a list.    

    Examples
    --------
    >>> get_codons('TACTAA')
    ['TAC', 'TAA']
    >>> get_codons('TACTA')
    Error: the string is not a multiple of 3.
    """
    if len(dna) % 3 != 0:
        return "Error: the string is not a multiple of 3."
    elif is_dna(dna):
        result, codon = [], ''
        for a in dna:
            codon += a
            if len(codon) == 3:
                result.append(codon)
                codon = ''
        return result