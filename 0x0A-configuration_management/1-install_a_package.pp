# Manifest that installs flask package
node default {
  package { 'flask':
    ensure   => '2.1.0',
    provider => 'pip3',
  }
}
