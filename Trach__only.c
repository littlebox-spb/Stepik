const int max_size = 5;

#define SIZE    1
#define IS_CPP

#if !defined(SIZE) 
#endif

// #if IS_CPP 
// #endif

#if SIZE > 0 
#endif

#if SIZE > 10 - 8 
#endif

#ifdef IS_CPP 
#endif

// #ifdef(IS_CPP) 
// #endif

#if max_size > 1 
#endif

#if(SIZE == 1) 
#endif

#if defined(SIZE) 
#endif

#if SIZE >= 0 && SIZE <= 10 
#endif

#ifndef IS_CPP 
#endif