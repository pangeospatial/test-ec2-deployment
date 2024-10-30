sudo apt update
sudo apt install python3 python3-venv python3-pip -y
git clone https://github.com/pangeospatial/test-ec2-deployment.git
cd test-ec2-deployment
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt