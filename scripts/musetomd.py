
import re
import sys
import os

infile = sys.argv[1]
outfile = os.path.basename(infile).split('.')[0] + '.md'
print(outfile)

def replacestars(matchobj):
    ret = ''
    print(matchobj.span())
    for i in range(matchobj.span()[1]):
        ret += '#'
    return ret

def replacetitle(matchobj):
    ret = '---\n' + 'title: '
    ret += matchobj.group(0)
    ret += 'layout: default\n' + '---\n'
    return ret

def fixlinks(matchobj):
    ret = ''
    st = matchobj.group(0)[2:-2]
    st = st.split('][')
    ret = '[' + st[1] +'](' + st[0] + ')'

    return ret

with open(infile, 'rt') as fin:
    with open(outfile, 'wt') as fout:
        for line in fin:
            # fix #title:
            lineout = re.sub('^#title .*', replacetitle, line)
            lineout = re.sub('^\*+', replacestars, line)
            match = re.match(';', lineout)
            if match is not None:
                lineout = '<!-- ' + lineout[:-1] +  '-->\n'
            lineout = re.sub('<comment>', '<!--', lineout)
            lineout = re.sub('</comment>', '-->', lineout)
            lineout = re.sub('\[\[.*\]\[.*\]\]', fixlinks, lineout)
            fout.write(lineout)
