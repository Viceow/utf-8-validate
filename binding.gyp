{
  'targets': [
    {
      'target_name': 'validation',
      'sources': [
        'src/validation.cc',
        'deps/simdutf/singleheader/simdutf.cpp'
      ],
      'cflags_cc': ['-std=gnu++11'],
      'include_dirs': ["<!(node -p \"require('node-addon-api').include_dir\")"],
      'defines': ['NAPI_DISABLE_CPP_EXCEPTIONS']
    }
  ]
}
