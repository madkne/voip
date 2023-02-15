#!/bin/bash
sudo apt install -y sox libsox-fmt-mp3

# convert mp3 to wav
mkdir -p mp3s waves gsms
rm -rdf waves/*
mp3_FILES=mp3s/*.mp3
for f in $mp3_FILES
do
   echo "Processing ${f} file..."
   sox "$f" "waves/$(basename "$f" .mp3).wav"
done
# convert wav to gsm
rm -rdf gsms/*
FILES=waves/*.wav
for f in $FILES
do
  echo "Processing ${f} file..." 
  sox "$f"  -r 8000 -c1 "gsms/$(basename "$f" .wav)".gsm lowpass 4000 compand 0.02,0.05 -60,-60,-30,-10,-20,-8,-5,-8,-2,-8 -8 -7 0.05
  # take action on each file. $f store current file name
  # cat $f
done
