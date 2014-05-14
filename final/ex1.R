# --------------------------------------------------------------
# EXERCISE 1
# --------------------------------------------------------------

#  Social security numbers in the United States are represented by 
#  numbers conforming to the following format:
#
#    a leading 0 followed by two digits
#    followed by a dash 
#    followed by two digits
#    followed by a dash
#    finally followed by four digits
#  
#  For example 023-45-7890 would be a valid value, 
#  but 05-09-1995 and 059-2-27 would not be.
#  
#  Implement the body of the function 'extractSecuNum' below so that it  
#  returns a numeric vector whose elements are Social Security numbers 
#  extracted from a text, i.e., a vector of strings representing the text lines,
#  passed to the function   as its 'text' argument. 
#  (You can assume that each string in 'text' contains 
#  either zero or one Social Security numbers.)


extractSecuNum  = function(text){
  out = c(); s = 0
  for(i in 1:length(text)){
    a = text[i]
    for(j in 1:50){
      if(substr(a,j,j) == "0"){
        s = j
        break;
      }
    }
    if(s != 0 & identical(substr(a,s+3, s+3), "-") & identical(substr(a,s+6, s+6), "-")){ 
      out = c(out, as.character(substr(a,s,s+10)))
    }
    s = 0
  }
  return(out)
















}


# --------------------------------------------------------------
# TEST 1 
# --------------------------------------------------------------
source('test.R')

testInput = c(
'For example',
'023-45-7890',
'would be a valid value', 
'but 05-09-1995',
'and 059-2-27 would not be.',
'Also 011-99-2234 is okay.'
)

correctOutput = c(
'023-45-7890',
'011-99-2234'
)

functionOutput  = extractSecuNum(testInput) 

tryCatch(
         checkEquals(correctOutput, functionOutput),
	 error = function(err) errmsg(err)
)


