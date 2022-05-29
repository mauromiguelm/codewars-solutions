two_oldest_ages <- function(ages){
  ages = eval(ages)
  m1 = max(ages)
  
  if(length(ages[!ages == m1])>0){
    m2 = max(ages[ages!=m1])
  }else{
    m2=m1
  }
  return(c(m2, m1))
}