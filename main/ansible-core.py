from ansible import context
from ansible.cli import CLI
from ansible.module_utils.common.collections import ImmutableDict
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.parsing.dataloader import DataLoader
from ansible.inventory.manager import InventoryManager
from ansible.vars.manager import VariableManager
import sys

hosts_path = "../hosts/" 
pb_path = "../yml/"

# Get aruments
arg = sys.argv
del arg[0] # first arumnet is [fileName].py

hosts_name = hosts_path + arg[0] 
pb_name = pb_path + arg[1]

loader = DataLoader()

context.CLIARGS = ImmutableDict(tags={}, listtags=False, listtasks=False, listhosts=False, syntax=False, connection='smart',
                    module_path=None, forks=50, remote_user='root', private_key_file=None,
                    ssh_common_args=None, ssh_extra_args=None, sftp_extra_args=None, scp_extra_args=None, become=True,
                    become_method='sudo', become_user='root', verbosity=True, check=False, start_at_task=None)

inventory = InventoryManager(loader=loader, sources=(hosts_name))

variable_manager = VariableManager(loader=loader, inventory=inventory, version_info=CLI.version_info(gitinfo=False))

pbex = PlaybookExecutor(playbooks=[pb_name], inventory=inventory, variable_manager=variable_manager, loader=loader, passwords={})

result = pbex.run()
