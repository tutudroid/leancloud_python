<template>
  <div class="personSettledVue">
    <table class="table table-striped one shown">
      <thead>
        <tr><td>商家名</td><td>品牌名</td><td>品牌LOGO</td><td>入驻类型</td><td>状态</td></tr>
      </thead>

      <tbody>
        <tr class="personRow pointer" @click='settledPersonDetail(1,"asha","18816500304","ashaShop","ashaBrand","ashaLogo照片","asha shop is nice","person",0,"289574827@qq.com","330327199402112931","2008-08-05","2009-09-01","正面照片","反面照片","手持照片","18816500340")'><td>asha</td><td>ashaBrand</td><td>sunasha</td><td>person</td><td>normal</td></tr>
        <tr class="personRow pointer" @click='settledPersonDetail(2,"peter","11011911212","peterShop","peterBrand","peterLogo","peter shop is good","person",1,"peter@gmail.com","3234234257357","2009-09-09","2010-09-08","正面照片","反面照片","手持照片","13718787326")'><td>peter</td><td>peterBrand</td><td>sunpeter</td><td>person</td><td>forbidden</td></tr>
      </tbody>
    </table>

    <div class="settledPersonDetail hide">
      <div class="container">
        <div class="name">
          账号：{{name}} 
	</div>

	<div class="phoneNumber">
          手机号：{{phoneNumber}}<span class="modifyPhoneNum link margin-left " @click="modifyPhoneNum()">修改</span>
	</div>
	
	<hr>

	<div class="shop_name">
          店铺名：{{shop_name}}
	</div>

	<div class="brandName">
          品牌名：{{brandName}}
	</div>

	<div class="brandLogo">
          品牌Logo{{brandLogo}}
	</div>

	<div class="brandDescription">
          品牌简介：{{brandDescription}}
	</div>

	<hr>

	<div class="type">
          入驻类型：{{type}}<span class="checkSettledInfo link margin-left "  @click="checkSettledPersonMaterial()">查看入驻材料</span>
	</div>

	<div class="state">
          状态：<span :class='[state==0?"normal":"forbidden"]'>正常</span><span :class='[state==1?"normal":"forbidden"]'>禁用</span>
	</div>

	<div class="link" @click="toggleShow">
	  返回
	</div>
      </div>
    </div>

    <div class="modifyPhoneNumDetail hideSecond">
	 <form class="form-horizontal">
	  <div class="control-group">
	    <label class="control-label" for="newPhone">新的手机号</label>
	    <div class="controls">
	      <input type="text" id="newPhone" v-model="newPhoneNumber">
	    </div>
	  </div>
	  <div class="control-group">
	    <label class="control-label" for="confirmPhone">确认手机号</label>
	    <div class="controls">
	      <input type="input" id="confirmPhone" v-model="confirmPhoneNumber">
	    </div>
	  </div>
	  <div class="control-group">
	    <div class="controls">
	      <button class="btn myBtn" @click="modifyPhoneNumToDB">确认</button>
	      <button class="btn myBtn" @click="toggleSecond">取消</button>
	    </div>
	  </div>
	</form>     
  </div>

  <div class="checkSettledPersonMaterial hideSecond">
    <h2>入驻资料</h2>
    <hr>

    <div class="name">
    入驻真实姓名: <span class="answer">{{name}}</span>
    </div>
    <div class="phoneNumber">
    手机号: <span class="answer">{{phoneNumber}}</span>
    </div>
    <div class="email">
    电子邮箱: <span class="answer">{{email}}</span>
    </div>
    <div class="IdCard">
    身份证号: <span class="answer">{{IdCard}}</span>
    </div>
    <div class="idCardTime">
    身份证有效期: <span class="answer">{{idCardExpireTimeStart}}至{{idCardExpireTimeEnd}}</span>
    </div>
    <div class="frontIdCard">
    身份证正面: <span class="answer">{{frontIdCard}}</span>
    </div>
    <div class="backIdCard">
    身份证反面: <span class="answer">{{backIdCard}}</span>
    </div>
    <div class="handIdCard">
    手持身份证照片: <span class="answer">{{handIdCard}}</span>
    </div>
    <div class="alipay">
    支付宝账号: <span class="answer">{{alipay}}</span>
    </div>

    <hr>

    <div class="shop_name">
    店铺名称: <span class="answer">{{shop_name}}</span>
    </div>
    <div class="brandName">
    品牌名称: <span class="answer">{{brandName}}</span>
    </div>
    <div class="brandLogo">
    品牌Logo: <span class="answer">{{brandLogo}}</span>
    </div>
    <div class="brandDescription">
    品牌简介: <span class="answer">{{brandDescription}}</span>
    </div>

    <div class="link" @click="toggleSecond">
      返回
    </div>

    <hr>

  </div>

  </div>


</template>

<script>
  export default {
    data:function(){
      return {
        settledPersonId:-1,
	name:"",
	phoneNumber:"",
	shop_name:"",
	brandName:"",
	brandLogo:"",
	brandDescription:"",
	type:"",
	state:-1,
	newPhoneNumber:"",
	confirmPhoneNumber:"",
	email:"",
	IdCard:"",
	idCardExpireTimeStart:"",
	idCardExpireTimeEnd:"",
	frontIdCard:"",
	backIdCard:"",
	handIdCard:"",
	alipay:"",
      }
    },
    props:["listofsettledperson"],
    methods: {
      settledPersonDetail(settledPersonId,name,phoneNumber,shop_name,brandName,brandLogo,brandDescription,type,state,email,IdCard,idCardExpireTimeStart,idCardExpireTimeEnd,frontIdCard,backIdCard,handIdCard,alipay){
        this.settledPersonId = settledPersonId;
	this.name = name;
	this.phoneNumber = phoneNumber;
	this.shop_name = shop_name;
	this.brandName = brandName;
	this.brandLogo = brandLogo;
	this.brandDescription = brandDescription;
	this.type = type;
	this.state = state;
	this.email = email;
	this.IdCard = IdCard;
	this.idCardExpireTimeStart = idCardExpireTimeStart;
	this.idCardExpireTimeEnd = idCardExpireTimeEnd;
	this.frontIdCard = frontIdCard;
	this.backIdCard = backIdCard;
	this.handIdCard = handIdCard;
	this.alipay = alipay;
	this.toggleShow();

      },
     toggleShow(){
       var show = $(".personSettledVue .shown");
       var hide = $(".personSettledVue .hide");
       if(show != null){
         show.removeClass("shown").addClass("hide");
         if(hide != null){
           hide.removeClass("hide").addClass("shown");
         }
       }
     },
     modifyPhoneNum(){
       var show = $(".personSettledVue .shown");
       var hide = $(".personSettledVue .hide");
       var hideSecond = $(".personSettledVue .modifyPhoneNumDetail.hideSecond");
       if(show != null){
         show.addClass("prev");
	 if(hide != null){
	   hide.addClass("prev");
	 }
       }
       if(hideSecond != null){
         hideSecond.removeClass("hideSecond").addClass("shownSecond");
       }
     },
     checkSettledPersonMaterial(){
       var show = $(".personSettledVue .shown");
       var hide = $(".personSettledVue .hide");
       var hideSecond = $(".checkSettledPersonMaterial.hideSecond");
       if(show != null){
         show.addClass("prev");
	 if(hide != null){
	   hide.addClass("prev");
	 }
       }
       if(hideSecond != null){
         hideSecond.removeClass("hideSecond").addClass("shownSecond");
       }
     },
     toggleSecond(){
       var shownSecond = $('.personSettledVue .modifyPhoneNumDetail.shownSecond');
       var shownSecondMaterial = $('.checkSettledPersonMaterial.shownSecond');
       var hidePrev = $('.personSettledVue .hide.prev');
       var shownPrev = $('.personSettledVue .shown.prev');
       if(shownSecond != null){
         shownSecond.removeClass('shownSecond').addClass('hideSecond');
	 if(hidePrev != null){
	   hidePrev.removeClass('prev');

	 }
	 if(shownPrev != null){
	  shownPrev.removeClass('prev');
	 }
       }

       if(shownSecondMaterial != null){
         shownSecondMaterial.removeClass('shownSecond').addClass('hideSecond');
	 if(hidePrev != null){
	   hidePrev.removeClass('prev');

	 }
	 if(shownPrev != null){
	  shownPrev.removeClass('prev');
	 }
       }
     },
     modifyPhoneNumToDB(){
       alert(" id: "+this.settledPersonId+" newPhoneNumber: "+this.newPhoneNumber+" confirmPhoneNumber: "+this.confirmPhoneNumber);
     },


    }
  }
</script>

<style>
  .settledPersonDetail div{
    margin: 20px;
    font-size: 18px;
  }
  hr{
    border-top:3px solid #cabdbd;
  }
  .normal{
    border: 2px solid;
    background-color: cyan;
    padding: 2px;
    margin: 0 5px;
  }
  .prev{
    display:none;
  }
  .settledPersonDetail div{
    margin: 20px;
    font-size: 18px;
  }
  hr{
    border-top:3px solid #cabdbd;
  }
  .checkSettledPersonMaterial div{
    margin: 20px;
    font-size: 18px;
  }
  .answer{
    position: absolute;
    left: 450px;
  }
</style>
