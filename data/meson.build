pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())

gnome = import('gnome')

gnome.compile_resources('coulr',
  'coulr.gresource.xml',
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
)

desktop_file = i18n.merge_file(
  input: 'com.github.huluti.Coulr.desktop.in',
  output: 'com.github.huluti.Coulr.desktop',
  type: 'desktop',
  po_dir: '../po',
  install: true,
  install_dir: join_paths(get_option('datadir'), 'applications')
)

desktop_utils = find_program('desktop-file-validate', required: false)
if desktop_utils.found()
  test('Validate desktop file', desktop_utils,
    args: [desktop_file]
  )
endif

appstream_file = i18n.merge_file(
  input: 'com.github.huluti.Coulr.appdata.xml.in',
  output: 'com.github.huluti.Coulr.appdata.xml',
  po_dir: '../po',
  install: true,
  install_dir: join_paths(get_option('datadir'), 'appdata')
)

appstream_util = find_program('appstream-util', required: false)
if appstream_util.found()
  test('Validate appstream file', appstream_util,
    args: ['validate', appstream_file]
  )
endif

install_data('com.github.huluti.Coulr.gschema.xml',
  install_dir: join_paths(get_option('datadir'), 'glib-2.0/schemas')
)

compile_schemas = find_program('glib-compile-schemas', required: false)
if compile_schemas.found()
  test('Validate schema file', compile_schemas,
    args: ['--strict', '--dry-run', meson.current_source_dir()]
  )
endif

# Installing the icons
icon_sizes = ['scalable']

foreach i : icon_sizes
  install_data(
    join_paths('icons/hicolor', i , 'apps', 'com.github.huluti.Coulr.svg'),
    install_dir: join_paths(get_option('prefix'), get_option('datadir'), 'icons', 'hicolor', i , 'apps'),
    rename: '@0@.svg'.format('com.github.huluti.Coulr')
  )
endforeach

# Installing the symbolic icon
install_data(
    join_paths('icons/hicolor/symbolic/apps', 'com.github.huluti.Coulr-symbolic.svg'),
    install_dir: join_paths(get_option('prefix'), get_option('datadir'), 'icons/hicolor/symbolic/apps'),
    rename: '@0@-symbolic.svg'.format('com.github.huluti.Coulr')
)
