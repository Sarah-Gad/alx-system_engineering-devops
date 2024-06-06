
package { 'ruby':
  ensure => installed}

exec { 'install_puppet_lint':
  command => 'gem install puppet-lint -v 2.1.1',
  path    => ['/usr/local/bin', '/usr/bin', '/bin'],
  require => Package['ruby']}

exec {'editing text file':
  command => 'sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'}
