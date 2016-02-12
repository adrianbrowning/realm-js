{
  "targets": [
    {
      "target_name": "Realm",
      "sources": [
            "../src/object-store/object_store.cpp",
		    "../src/object-store/index_set.cpp",
		    "../src/object-store/list",
		    "../src/object-store/results.cpp",
		    "../src/object-store/schema.cpp",
		    "../src/object-store/object_schema.cpp",
            "../src/object-store/shared_realm.cpp",
		    "../src/object-store/impl/transact_log_handler.cpp",
            "../src/object-store/impl/apple/external_commit_helper.cpp",
            "iorealm.cc",
            "realm.cc",
            "realmobject.cc",
            "realmresults.cc",
            "realmarray.cc",
            "realmschema.cc",
            "realmutils.cpp"
      ],
      "include_dirs": [ "../core/include", "../src/object-store", "../src/object-store/impl", "../src/object-store/impl/apple" ],
      "cflags_cc": [ '-DREALM_ENABLE_REPLICATION', '-fexceptions', '-frtti', '-std=c++14', '-g', '-O0' ],
      "ldflags": [ '-L../core/', '-lrealm' ],
      "xcode_settings" : {
        'OTHER_CFLAGS' : [ '-mmacosx-version-min=10.8', '-DREALM_ENABLE_REPLICATION', '-fexceptions', '-frtti', '-std=c++14', '-stdlib=libc++', '-g', '-O0', '-Wno-mismatched-tags' ],
        'OTHER_LDFLAGS': [ '-L../core/', '-lrealm' ]
      },
    }
  ]
}