library(testthat)

stockList <- function(listOfArt=NA, listOfCat=NA) {
  
  #listOfArt=b
  #listOfCat=c
  
  if(all(is.na(listOfArt))|all(is.na(listOfCat))){
    return("")
  }else{
    listOfCat_count <- rep(0,length(listOfCat))
    
    listOfArt_cat <- substr(listOfArt,1,1)
    
    listOfArt_count <- as.numeric(sapply(strsplit(listOfArt, split = " "), "[[",2))
    
    
    for(idx in seq_along(listOfCat)){
      listOfCat_count[idx]= sum(listOfArt_count[which(listOfArt_cat==listOfCat[idx])])
    }
    
    return(paste0("(",listOfCat, " : ",listOfCat_count,")", collapse = " - "))
    
  }
  
  
  
}


testing <- function(listOfArt, listOfCat, expected) {
  actual <- stockList(listOfArt, listOfCat)
  expect_equal(actual, expected)
}


b = c("BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600", "XRAV 1", "AHJH 0")
c = c("A", "B", "C", "D")
res = "(A : 0) - (B : 1290) - (C : 515) - (D : 600)"
testing(b, c, res)
