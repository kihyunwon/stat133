# --------------------------------------------------------------
# EXERCISE 3 
# --------------------------------------------------------------


#  Implement the body of the function 'keepDoubleQuotesOnly' below so that
#  it returns a character vector containing only the elements 
#  of the character vector 'theString' (passed as a function argument)
#  that have more than one double quoted string.
#  
#  For example, if the following strings 
#  
#  this "line" has "quoted" "strings"
#  "one" more to follow "two"
#  "a""b"
#  there's "one" quoted string
#  Here's a quote "
#  No quotes here
#  
#  are the elements of the character vector 'theString',
#  then the function should return a character vector 
#  with the three first strings only. 



keepDoubleQuotesOnly = function(theString){
  out = c(); counter = 0
  for(i in 1:length(theString)){
    
    for(j in 1:100){
      if(identical(substr(theString[i],j,j),'\"')){
        counter = counter + 1
      }
    }
    if(counter >= 4){
      out = c(out, theString[i])
    }
    counter = 0
  }
  return(out)






}

# --------------------------------------------------------------
# TEST 3 
# --------------------------------------------------------------

source('test.R')

testInput  = c('this "line" has "quoted" "strings"',
               'there\'s "one" quoted string',
               '"one" more to follow "two"',
               'Here\'s a quote "',
               '"a""b"')


correctOutput = c('this "line" has "quoted" "strings"',
                  '"one" more to follow "two"',
                  '"a""b"')

functionOutput = keepDoubleQuotesOnly(testInput) 

tryCatch(
         checkEquals(correctOutput, functionOutput),
	 error = function(err) errmsg(err)
	 )


