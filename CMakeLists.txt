cmake_minimum_required(VERSION 3.10)  
project(MyProject VERSION 1.0 LANGUAGES CXX)  

set(CMAKE_CXX_STANDARD 17)            
set(CMAKE_CXX_STANDARD_REQUIRED ON)   
set(CMAKE_CXX_EXTENSIONS OFF)         

set(GMP_INCLUDE_DIR /usr/include)
set(GMP_LIBRARY /usr/lib/x86_64-linux-gnu/libgmp.so)
set(GMPXX_LIBRARY /usr/lib/x86_64-linux-gnu/libgmpxx.so)

add_executable(testPeriods 
                src/testPeriods.cpp
                src/QuadraticIrrationals.cpp
) 
add_executable(testPells
                src/testPells.cpp
                src/QuadraticIrrationals.cpp
                src/PellsEquations.cpp
)

target_link_libraries(testPeriods PRIVATE ${GMP_LIBRARY} ${GMPXX_LIBRARY})
target_link_libraries(testPells PRIVATE ${GMP_LIBRARY} ${GMPXX_LIBRARY})