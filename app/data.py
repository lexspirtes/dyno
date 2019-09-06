
#creates SQL query for hamming distance 1, including exact matches
def hamSQL(s):
    """
    input
        str: DNA sequence to match
    returns
        str: SQL Query to find exact and
             hamming distance 1matches
    """
    SQL = "SELECT * FROM VIRUSES WHERE "
    for index in range(0, len(s)):
        SQL +=  "SEQUENCE LIKE '%" + s[:index]+"_"+s[index+1:] + "%'"
        if index != len(s) -1:
            SQL += " OR "
    return SQL

def exactSQL(s):
    """
    input
        str: DNA sequence to match
    returns
        str: SQL Query to find exact matches
    """
    #identical to:
    # Virus.query.filter(Virus.sequence.like('%' + searchSeq + '%')).all()
    SQL = "SELECT * FROM VIRUSES WHERE SEQUENCE LIKE '%{}%'".format(s)
    return SQL

def editSQL(s):
    """
    input
        str: DNA sequence to match
    returns
        str: SQL Query to find exact and edit distance 1 matches
    """
    SQL = "SELECT * FROM VIRUSES WHERE "
    for index in range(0, len(s)):
        #hamming case
        SQL += "SEQUENCE LIKE '%" + s[:index]+"_"+s[index+1:] + "%' OR "
        #insertion case
        SQL += "SEQUENCE LIKE '%" + s[:index]+s[index+1:] + "%' OR "
        #deletion case
        if index != 0 and index != len(s):
            SQL += "SEQUENCE LIKE '%" + s[:index] + "_" + s[index:] + "%'"
        if index != len(s) -1 and index != 0:
            SQL += " OR "
    return SQL
