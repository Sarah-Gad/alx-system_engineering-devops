# This manifest will install flask with the provider pip3
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip',
}
