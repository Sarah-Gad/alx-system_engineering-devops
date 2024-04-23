# This manifest will automate the configiration process of nginx

exec { 'updating sys':
  command  => '/usr/bin/apt-get update',
}

package { 'installing nginx':
  ensure   => 'installed',
  require  => Exec['updating sys']
}

file {'/var/www/html/index.html':
  content  => 'Hello World!'
}

exec {'redirecting':
  command  => 'sed -i "24i\       rewrite ^/redirect_me https://www.google.com/ permanent;" /etc/nginx/sites-available/default',
  provider => 'shell'
}

service {'running_nginx':
  ensure   => running,
  require  => Package['installing nginx']
}
