pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'coulr')
gnome = import('gnome')

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', join_paths(get_option('prefix'), get_option('localedir')))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'coulr.in',
  output: 'coulr',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir')
)

coulr_sources = [
  '__init__.py',
  'main.py',
  'window.py'
]

install_data(coulr_sources, install_dir: moduledir)
