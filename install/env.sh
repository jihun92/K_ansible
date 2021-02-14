echo 'export ANSIBLE_CONFIG=~/ansible-core/cfg' >> ~/.bashrc
echo "alias anp='ansible-playbook'" >> ~/.bashrc
echo "alias ans='ansible'" >> ~/.bashrc
source ~/.bashrc

echo "#############################"
echo "#### Ansible Information ####"
echo "#############################"
ansible --version

echo "#############################"
echo "#### Set Alias ##############"
echo "#############################"
ansible --version
cat ~/.bashrc | grep "alias an*"
