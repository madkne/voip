# Setup VOIP Server

## get started

1. requirements:
  - Issabel
  - python3

2. install python3.9+

```bash
# for CentOS 8 / CentOS 7
sudo yum -y update
sudo yum install -y python36
```

3. install project requirements:
```
pip3 install -r requirements
```

4. install other system need packages:
```

yum install -y mpg123 # for play sound

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


## set custom sounds

1. create a .wav file
2. convert it to .gsm file by using sox:
```
sox sound1.wav  -r 8000 -c1 sound1.gsm lowpass 4000 compand 0.02,0.05 -60,-60,-30,-10,-20,-8,-5,-8,-2,-8 -8 -7 0.05
```
3. copy `sound1.gsm` to `/var/lib/asterisk/sounds/en`

4. now you can play it by `agi.stream_file('sound1')` on python script

### convert mp3 files to gsm files

1. create a folder named `voices/mp3s`
2. copy mp3 files to `voices/mp3s`
3. copy `convert_mp3_to_gsm.sh` to `voices/`
4. run script