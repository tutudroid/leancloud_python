

document.querySelector('.navInMonitor').addEventListener('click',function(e){
  try{
    var secondNavToBeUsed = e.target.id;
    if(secondNavToBeUsed === ""){
      throw "nothing";
    }
    var contentUsed = document.querySelectorAll(".content.used");
    for(var content of contentUsed){
      var name = content.className.split(" ")[1];
      content.className = "content " + name;
    }
  
    
    var contentMenuUsed = document.querySelectorAll(".contentMenu .used");
    for(var contentMenu of contentMenuUsed){
      var name = contentMenu.className.split(" ")[1];
      contentMenu.className = "mp " + name;
    }

    var secondNavUsed = document.querySelector(".main.used");
    if(secondNavUsed !== null){
	    var secondNavUsedClass = secondNavUsed.className.split(" ")[1];
	    secondNavUsed.className = "main " + secondNavUsedClass;
    }
		
    document.querySelector('.main.'+secondNavToBeUsed).className="main " + secondNavToBeUsed + " used";
  }
  catch(e){
    console.log(e);
  }


  
document.querySelector('div.used .side').addEventListener('click',function(e){
  try{
    var thirdNavToBeUsed = e.target.id;
    if(thirdNavToBeUsed === ""){
      throw "nothing";
    }
    var thirdNavUsed = document.querySelector(".content.used");
    if(thirdNavUsed !== null){
	    var thirdNavUsedClass = thirdNavUsed.className.split(" ")[1];
	    thirdNavUsed.className = "content " + thirdNavUsedClass;
    }
		
    document.querySelector('.content.'+thirdNavToBeUsed).className="content " + thirdNavToBeUsed + " used";
  }
  catch(e){
  }



document.querySelector('.content.used .contentMenu').addEventListener('click',function(e){
  try{
    var finalContent = e.target.id;
    if((finalContent.slice(0,2)) != "mp"){
     throw "nothing";
    }
    var finalContentUsed = document.querySelector(".contentMenu .used");
    if(finalContentUsed !== null){
	    var finalContentUsedClass = finalContentUsed.className.split(" ")[1];
	    finalContentUsed.className = "mp " + finalContentUsedClass;
    }
		
  document.querySelector('.mp.'+finalContent).className="mp " + finalContent + " used";
  }
  catch(e){
  }

}); 


});
    


});




document.querySelector('div.used .side').addEventListener('click',function(e){
  try{
    var thirdNavToBeUsed = e.target.id;
    if(thirdNavToBeUsed === ""){
      throw "nothing";
    }
    var thirdNavUsed = document.querySelector(".content.used");
    if(thirdNavUsed !== null){
	    var thirdNavUsedClass = thirdNavUsed.className.split(" ")[1];
	    thirdNavUsed.className = "content " + thirdNavUsedClass;
    }
		
    document.querySelector('.content.'+thirdNavToBeUsed).className="content " + thirdNavToBeUsed + " used";
  }
  catch(e){
  }


    var contentMenuUsed = document.querySelectorAll(".contentMenu .used");
    for(var contentMenu of contentMenuUsed){
      var name = contentMenu.className.split(" ")[1];
      contentMenu.className = "mp " + name;
    }


document.querySelector('.content.used .contentMenu').addEventListener('click',function(e){
  try{
    var finalContent = e.target.id;
    if((finalContent.slice(0,2)) != "mp"){
     throw "nothing";
    }
    var finalContentUsed = document.querySelector(".contentMenu .used");
    if(finalContentUsed !== null){
	    var finalContentUsedClass = finalContentUsed.className.split(" ")[1];
	    finalContentUsed.className = "mp " + finalContentUsedClass;
    }
		
  document.querySelector('.mp.'+finalContent).className="mp " + finalContent + " used";
  }
  catch(e){
  }

}); 


});


document.querySelector('.content.used .contentMenu').addEventListener('click',function(e){
  try{
    var finalContent = e.target.id;
    if((finalContent.slice(0,2)) != "mp"){
     throw "nothing";
    }
    var finalContentUsed = document.querySelector(".contentMenu .used");
    if(finalContentUsed !== null){
	    var finalContentUsedClass = finalContentUsed.className.split(" ")[1];
	    finalContentUsed.className = "mp " + finalContentUsedClass;
    }
		
  document.querySelector('.mp.'+finalContent).className="mp " + finalContent + " used";
  }
  catch(e){
  }

}); 




