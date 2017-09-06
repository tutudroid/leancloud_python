const $ = require("jquery");
const swal = require("sweetalert");
const axios = require("axios");

//login
//login------login.html
import login from './login/login.vue'

//system
//accountlist-----check forbid delete changePwd account
import changePwd from './backend/system/accountList/changePwd.vue'
//system
//accountlist-----add new account
import addAccount from './backend/system/accountList/addAccount.vue'
//system
//sellerAccount-----personSettled
import personSettled from './backend/system/sellerAccount/personSettled.vue'
//system
//sellerAccount-----companySettled
import companySettled from './backend/system/sellerAccount/companySettled.vue'
//system
//sellerAccount-----settleWatingForPass
import settleWaitingForPass from './backend/system/sellerAccount/settleWaitingForPass.vue'
//system
//sellerAccount-----settleForbidden
import settleForbidden from './backend/system/sellerAccount/settleForbidden.vue'
//system
//appuser------searchappuser
import searchAppUser from './backend/system/appUser/searchAppUser.vue'
//system
//clientPageConfig
import clientPageConfig from './backend/system/clientPageConfig/clientPageConfig.vue'

//stock
//searchStockCategory
import searchStockCategory from './backend/stock/searchStockCategory/searchStockCategory.vue'
//stock
//editStockCategory
import editStockCategory from './backend/stock/editStockCategory/editStockCategory.vue'

//sellerBackend loginModule
//register
import registerForm from './sellerBackend/loginModule/registerForm.vue'
//sellerBackend loginModule
//forgetPwd
import forgetPwdForm from './sellerBackend/loginModule/forgetPwdForm.vue'

new Vue({
	el: '#app',
	data:{
	  allSysUsers:[],
    allClientConfigs:[],
	},
	components: {
	    "changepwd":changePwd,
	    "addaccount":addAccount,
	    "personsettled":personSettled,
	    "companysettled":companySettled,
            "settlewaitingforpass":settleWaitingForPass,
	    "settleforbidden":settleForbidden,
	    "searchappuser":searchAppUser,
	    "clientpageconfig":clientPageConfig,
	    "login":login,
	    "searchstockcategory":searchStockCategory,
	    "editstockcategory":editStockCategory,
	    "registerform":registerForm,
	    "forgetpwdform":forgetPwdForm,
	},
	methods: {
	  back(id){
	   var firstChild = $(id+" div.shown");
	   var secondChild = $(id+" div.shownSecond");
	   if(firstChild.hasClass('shown')){
	     firstChild.removeClass('shown').addClass('hide');
	     if(firstChild.hasClass('prev')){
	       firstChild.removeClass('prev');
	     }
	   }
	   var point = $(id+" .one");
	   if(point.hasClass('hide')){
	     point.removeClass('hide').removeClass('prev').addClass('shown');
	   }
	   if(secondChild.hasClass('shownSecond')){
	     secondChild.removeClass('shownSecond').addClass('hideSecond');
	   }
	
	  },

	  //抓取所有的系统用户
	  allSysuser(){
  		swal({
  		  title: "加载中",
  		  text:"你这么可爱，就等待一下呗",
  		  timer: 2000,
  		  showConfirmButton: false
  		});
		 let _this = this;
       $.ajax({
          type: 'GET',
          url: '/Admin/SysUser/',
          data: {
              'page':1,
          },
          success: function (data) {
            let rdata = JSON.parse(data);
            _this.allSysUsers = rdata.User;
          },
         error: function(XMLHttpRequest, textStatus, errorThrown) {
           swal('抓取不到数据')
          },
      });
  	},
    //抓取所有的客户端配置
    getAllClientConfigs(){
      swal({
        title: "加载中",
        text:"你这么可爱，就等待一下呗",
        timer: 2000,
        showConfirmButton: false
      });
     let _this = this;
       $.ajax({
          type: 'GET',
          url: '/Admin/WebPageConfigure/',
          data: {
             
          },
          success: function (data) {
            let dataJson = JSON.parse(data);
            _this.allClientConfigs = dataJson.WebPageConfigure;
            
          },
         error: function(XMLHttpRequest, textStatus, errorThrown) {
           swal('抓取不到数据')
          },
      });
    },
  }

});















//ashacus

if(document.querySelector('.navInMonitor') != null){



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



}
