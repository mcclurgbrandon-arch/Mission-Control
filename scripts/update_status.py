#!/usr/bin/env python3
import json,sys,datetime
p='agent_status.json'
with open(p,'r') as f:
    s=json.load(f)
cmd=sys.argv[1] if len(sys.argv)>1 else 'idle'
msg=' '.join(sys.argv[2:]) if len(sys.argv)>2 else ''
if cmd=='start':
    s['status']='working'
    s['task']=msg
    s['since']=datetime.datetime.now().isoformat()
    s['log'].append({'time':s['since'],'msg':'START '+msg})
elif cmd=='done':
    s['status']='idle'
    s['task']=None
    s['since']=None
    s['log'].append({'time':datetime.datetime.now().isoformat(),'msg':'DONE '+msg})
else:
    s['status']=cmd
    s['task']=msg
    s['since']=datetime.datetime.now().isoformat()
    s['log'].append({'time':s['since'],'msg':msg})
with open(p,'w') as f:
    json.dump(s,f,indent=2)
print('updated')
