import os
import sys

sys.path.append('/utils')
import utils


CONFIG = os.environ["CONFIG"]
INPUT = os.environ["INPUT"]
OUTPUT = os.environ["OUTPUT"]
MSDIR = os.environ["MSDIR"]

cab = utils.readJson(CONFIG)

args = []
for param in cab['parameters']:
    name = param['name']
    value = param['value']

    if value in [False, None]:
        continue

    if name in 'channels timeslots corrs stations ddid field str'.split():
        if name in 'channels timeslots'.split():
            value = ':'.join(value)
        else:
            value = ','.join(value)
    if value is True:
        value = ""
    
    if name == 'msname':
        msname = value
        if isinstance(msname, str):
            msname = [msname]
        continue

    if name=='flagged-any':
        args += ['{0}flagged-any {1}'.format(cab['prefix'], a) for a in value]
        continue

    args.append( '{0}{1} {2}'.format(cab['prefix'], name, value) )

utils.xrun(cab['binary'], args+msname)
