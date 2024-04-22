# i used this manifest to include specific lines in the ssh config file.
file_line { 'ssh_config_disable_pass':
  path => '/etc/ssh/ssh_config',
  line => '	PasswordAuthentication no',
}

file_line { 'ssh_config_identity':
  path	=> '/etc/ssh/ssh_config',
  line	=> '	IdentityFile ~/.ssh/school',
}
