# Manifest that creates a file, sets permissions and places content in it
node default {
  file { 'tmp/school':
    path    => '/tmp/school',
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0744',
    content => 'I love Puppet',
  }
}
