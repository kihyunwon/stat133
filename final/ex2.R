# --------------------------------------------------------------
# EXERCISE 2 
# --------------------------------------------------------------

#  Implement the body of the function 'rmMultipleBlanks' 
#  below so that it removes multiple blank characters (i.e.,
#  spaces, tabs, and newlines) from before and after 
#  a vector of strings. For example:
#
#  " hello, world   "     should be converted to "hello, world"
#  "\n Stat 133 "         should be converted to "Stat 133"
#  "\t\t\tStat 133\n\n "  should be converted to "Stat 133"
#
#  The function takes an argument called 'stringsWithBlanks', which
#  is a character vector of strings (having possible junky prefixing
#  and/or trailing blank characters). 
# 
#  The function should return a character vector of the same 
#  length containing the strings with the 
#  prefixing and/or trailing blanks removed.



rmMultipleBlanks = function(stringsWithBlanks){
  out = stringsWithBlanks; r = c()
  for(i in 1:length(out)){
    a = out[i]; t=0; s=0
    for(j in 1:30){
      if(!identical(substr(a,j,j), " ") & !identical(substr(a,j,j), "\n") & !identical(substr(a,j,j), "\t")){
        s = j
        break
      }
    }
    for(j in 30:1){
      if(!identical(substr(a,j,j), "") & !identical(substr(a,j,j), " ") & !identical(substr(a,j,j), "\n") & !identical(substr(a,j,j), "\t")){
        t = j
        break
      }
    }
    r = c(r, substr(a,s,t))
  }
  return(r)







}




# --------------------------------------------------------------
# TEST 2 
# --------------------------------------------------------------
source('test.R')

testInput      = c(" hello, world ", "\n \tStat 133 ")
functionOutput = rmMultipleBlanks(testInput) 
correctOutput  = c("hello, world", "Stat 133")

tryCatch(
         checkEquals(correctOutput, functionOutput),
	 error = function(err) errmsg(err)
)


