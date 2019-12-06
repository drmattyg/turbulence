from turbulence.pca9685 import PCA9685
import yaml
import os
import signal
import sys
global pca
CONFIG_FILE = os.path.join(os.path.dirname(__file__), '..', 'config.yml')


def read_config(filename=CONFIG_FILE):
	with open(CONFIG_FILE, 'r') as f:
		config = yaml.load(f)
	return config

def load_pca(i2c_address=0x40):
	global pca
	pca = PCA9685(i2c_address=i2c_address)

def signal_handler(sig, frame):
	global pca
	print("Shutting down")
    for i in range(16):
    	pca.set_off(i)
        sys.exit(0)

def main():
	# handle ctrl-c
	signal.signal(signal.SIGINT, signal_handler)

	for i, m in config['motors'].items():
		pca.set_duty(m['pca_channel'], m['speed'])

	signal.pause()

