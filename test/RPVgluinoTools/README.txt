Instructions for installing fastjet and tools for computing fat jet sum jet mass

- install fast jet

curl -O http://fastjet.fr/repo/fastjet-3.0.6.tar.gz 
tar zxvf fastjet-3.0.6.tar.gz
cd fastjet-3.0.6/

./configure --prefix=$PWD/../fastjet-install
make 
make check
make install
cd ..

- install code to 

g++ `root-config --cflags` RA2nTuple.cc addFatJetsToTree.C `root-config --glibs` -l$PWD/fastjet-3.0.6/src/.libs/libfastjet.so.0.0.0 -Ifastjet-3.0.6/include/ -o addFatJetsToTree.exe -Wall