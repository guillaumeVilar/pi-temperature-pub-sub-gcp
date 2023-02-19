# pi-temperature-pub-sub-gcp

## OVERVIEW:
Project to do the following: 
1. Get the temperature where the raspberrypi is located (using a breadboard and thermistor - for e.g. using a Monk Makes box)
2. (In progress) Store the temperature in a Redis timeseries database
3. Publish the temperature to a GCP pub-sub topic 
4. (In progress) Front-end to display the temperature from the pub-sub

## INSTALLATION: 
1. Installation of the pub-sub on GCP can be done following the tutorial:   
https://cloud.google.com/pubsub/docs/building-pubsub-messaging-system

2. Local installation: 
```
python -m venv pyenv-qs
source pyenv-qs/bin/activate
pip3 install google-cloud-pubsub
export GOOGLE_APPLICATION_CREDENTIALS=$PWD/key-temperature-pub-sub-account.json
git clone https://github.com/simonmonk/pi_analog.git_analog.git
cd pi_analog
sudo python3 setup.py install
```

## RUN on pi: 
```
source pyenv-qs/bin/activate
python3 thermometer_with_pub.py
```

## Test on subscriber: 
```
source pyenv-qs/bin/activate
python3 sub.py
```
