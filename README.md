# Dadgam VOIP

## get started

1. install python3.9+

```bash
# for CentOS 8 / CentOS 7
sudo yum -y update
sudo yum install -y python36
```

## install `play.py` script

1. open file `/etc/asterisk/extensions.conf`
2. find `[macro-dial]`
3. before `exten => s,n(dial),AGI(dialparties.agi)` set follow commands
```
exten => s,n, Verbose(0, starting play.py script...)
exten => s,n,Answer()
;exten => s,n,Wait(2)
;exten => s,n,Echo()
exten => s,n(dial),AGI(play.py)
``` 
4. then copy `play.py` file into `/var/lib/asterisk/agi-bin/` directory
5. set permission with `chmod 777 /var/lib/asterisk/agi-bin/play.py`
6. run `./restart.sh` to apply changes

> for enable asterisk debugging `asterisk -rx 'agi set debug on'`
