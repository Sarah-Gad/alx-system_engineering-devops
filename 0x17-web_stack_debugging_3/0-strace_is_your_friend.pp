
package { 'ruby':
  ensure => installed}
  
exec {'editing text file':
  command => 'sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'}
