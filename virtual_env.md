#### install needed files
apt install -y python3-pip python3 make build-essential libssl-dev zlib1g-dev libbz2-dev \
  libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
  xz-utils tk-dev libffi-dev liblzma-dev python-openssl git

#### download pyenv and install
curl https://pyenv.run | bash

#### add this to bashrc
export PATH="$HOME/.pyenv/bin:$PATH" 
eval "$(pyenv init -)" 
eval "$(pyenv virtualenv-init -)"

#### install a version of python
pyenv install 3.7.4 

#### create a virt env
pyenv virtualenv <version>  <name> 

#### start virt env
pyenv activate <nam>

#### list virt envs
pyenv virtualenvs

#### end virt env
pyenv deactivate

#### delete virt env
pyenv virtualenv-delete my-virtual-env
