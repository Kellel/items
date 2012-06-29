#include <iostream>
#include <string>
using namespace std;

//Globals
const int ARG_COUNT = 2;

main( int argc, char *argv[] )
{
    cout << "blarg..." << endl;
    
    if ( argc > ARG_COUNT ){
       int over = argc - ARG_COUNT;  
       for ( int i = 0; i < argc; i++){
           if ( i < ARG_COUNT )
               cout << argv[i] << " ";
           else
               cout << "? " << argv[i] << " ";
       }
       cout << endl;
    }
}

