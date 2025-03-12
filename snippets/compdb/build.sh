# Make sure `cmake-4.0.0-rc4-linux-x86_64/bin/` is in your PATH
cmake --preset default -DCMAKE_CXX_FLAGS=-stdlib=libc++
cmake --build --preset default 
