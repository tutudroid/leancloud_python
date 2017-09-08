<template>
  <div class="companySettledVue">
    <table class="table table-striped one shown" v-if="companyshops.length > 0">
      <thead>
        <tr><td>商家名</td><td>品牌名</td><td>品牌LOGO</td><td>入驻类型</td><td>状态</td></tr>
      </thead>

      <tbody>
        <tr v-for="shop in shops()" class="personRow pointer" @click='settledCompanyDetail(shop.objectId,shop.managerPhoneNumber,shop.managerRealName,shop.managerEmail,shop.alipay,shop.shopName,shop.brandName,shop.brandLogo,shop.brandDescription,shop.bussinessLicense,shop.uniformSocialCreditCode,shop.legalPersonName,shop.legalPersonPhoneNumber,shop.legalPersonIdCard,shop.legalPersonFrontIdCard,shop.legalPersonBackIdCard,shop.legalPersonExpireTimeStart,shop.legalPersonExpireTimeEnd,shop.legalPersonEmail,shop.state,shop.type)'><td>{{shop.legalPersonName}}</td><td>{{shop.brandName}}</td><td>{{shop.brandLogo}}</td><td>公司</td><td>{{shop.state}}</td></tr>
      </tbody>
    </table>

    <div class="settledPersonDetail hide">
      <div class="container">
        <div class="name">
          账号：{{managerRealName}} 
	</div>

	<div class="managePhoneNumber">
          手机号：{{managerPhoneNumber}}<span class="modifyPhoneNum link margin-left " @click="modifyPhoneNum()">修改</span>
	</div>
	
	<hr>

	<div class="shopName">
          店铺名：{{shopName}}
	</div>

	<div class="brandName">
          品牌名：{{brandName}}
	</div>

	<div class="brandLogo">
          品牌Logo：{{brandLogo}}
	</div>

	<div class="brandDescription">
          品牌简介：{{brandDescription}}
	</div>

	<hr>

	<div class="type">
          入驻类型：{{type}}<span class="checkSettledInfo link margin-left "  @click="checkSettledCompanyMaterial()">查看入驻材料</span>
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
	      <span class="btn myBtn" @click="modifyPhoneNumToDB">确认</span>
	      <span class="btn myBtn" @click="toggleSecond">取消</span>
	    </div>
	  </div>
	</form>     
  </div>

  <div class="checkSettledCompanyMaterial hideSecond">
    <h2>入驻资料</h2>
    <hr>

    <div class="uniformSocialCreditCode">
    统一社会信用代码: <span class="answer">{{uniformSocialCreditCode}}</span>
    </div>
    <div class="bussinessLicense">
    营业执照: <span class="answer">{{bussinessLicense}}</span>
    </div>
    <div class="legalPersonName">
    法人姓名: <span class="answer">{{legalPersonName}}</span>
    </div>
    <div class="legalPhoneNumber">
    法人手机号: <span class="answer">{{legalPersonPhoneNumber}}</span>
    </div>
    <div class="legalPersonEmail">
    法人邮箱: <span class="answer">{{legalPersonEmail}}</span>
    </div>
    <div class="legalPersonIdCard">
    法人身份证号: <span class="answer">{{legalPersonIdCard}}</span>
    </div>
    <div class="legalPersonidCardTime">
    法人身份证有效期: <span class="answer">{{legalPersonExpireTimeStart}}至{{legalPersonExpireTimeEnd}}</span>
    </div>
    <div class="legalPersonFrontIdCard">
    法人身份证正面: <span class="answer">{{legalPersonFrontIdCard}}</span>
    </div>
    <div class="legalPersonBackIdCard">
    法人身份证反面: <span class="answer">{{legalPersonBackIdCard}}</span>
    </div>
    <div class="alipay">
    支付宝账号: <span class="answer">{{alipay}}</span>
    </div>

    <hr>
    
    <div class="managerRealName">
    管理人真实姓名: <span class="answer">{{managerRealName}}</span>
    </div>
    <div class="managerEmail">
    管理人邮箱: <span class="answer">{{managerEmail}}</span>
    </div>
    <div class="managerPhoneNumber">
    管理人手机号: <span class="answer">{{managerPhoneNumber}}</span>
    </div>

    <hr>

    <div class="shopName">
    店铺名称: <span class="answer">{{shopName}}</span>
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
      	type:"",
      	managerPhoneNumber:"",
      	managerRealName:"",
      	managerEmail:"",
      	alipay:"",
      	shopName:"",
      	brandName:"",
      	brandLogo:"",
      	brandDescription:"",
      	bussinessLicense:"",
      	uniformSocialCreditCode:"",
      	legalPersonName:"",
      	legalPersonPhoneNumber:"",
      	legalPersonIdCard:"",
      	legalPersonFrontIdCard:"",
      	legalPersonBackIdCard:"",
      	legalPersonExpireTimeStart:"",
      	legalPersonExpireTimeEnd:"",
      	legalPersonEmail:"",
      	state:0,
      	newPhoneNumber:"",
      	confirmPhoneNumber:""
      }
    },
    props:["companyshops"],
    methods: {
      settledCompanyDetail(settledCompanyId,managerPhoneNumber,managerRealName,managerEmail,alipay,shopName,brandName,brandLogo,brandDescription,bussinessLicense,uniformSocialCreditCode,legalPersonName,legalPersonPhoneNumber,legalPersonIdCard,legalPersonFrontIdCard,legalPersonBackIdCard,legalPersonExpireTimeStart,legalPersonExpireTimeEnd,legalPersonEmail,state,type){
        this.settledCompanyId = settledCompanyId;
      	this.managerPhoneNumber = managerPhoneNumber;
      	this.managerRealName = managerRealName;
      	this.managerEmail = managerEmail;
      	this.alipay = alipay;
      	this.shopName = shopName;
      	this.brandName = brandName;
      	this.brandLogo = brandLogo;
      	this.brandDescription = brandDescription;
      	this.bussinessLicense = bussinessLicense;
      	this.uniformSocialCreditCode = uniformSocialCreditCode;
      	this.legalPersonName = legalPersonName;
      	this.legalPersonPhoneNumber = legalPersonPhoneNumber;
      	this.legalPersonIdCard = legalPersonIdCard;
      	this.legalPersonFrontIdCard = legalPersonFrontIdCard;
      	this.legalPersonBackIdCard = legalPersonBackIdCard;
      	this.legalPersonExpireTimeStart = legalPersonExpireTimeStart;
      	this.legalPersonExpireTimeEnd = legalPersonExpireTimeEnd;
      	this.legalPersonEmail = legalPersonEmail;
      	this.state = state;
      	this.type = type;
      	this.toggleShow();
      },
     toggleShow(){
       var show = $(".companySettledVue .shown");
       var hide = $(".companySettledVue .hide");
       if(show != null){
         show.removeClass("shown").addClass("hide");
         if(hide != null){
           hide.removeClass("hide").addClass("shown");
         }
       }
     },
     modifyPhoneNum(){
       var show = $(".companySettledVue .shown");
       var hide = $(".companySettledVue .hide");
       var hideSecond = $(".companySettledVue .modifyPhoneNumDetail.hideSecond");
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
     checkSettledCompanyMaterial(){
       var show = $(".companySettledVue .shown");
       var hide = $(".companySettledVue .hide");
       var hideSecond = $(".checkSettledCompanyMaterial.hideSecond");
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
       var shownSecond = $('.companySettledVue .modifyPhoneNumDetail.shownSecond');
       var shownSecondMaterial = $('.checkSettledCompanyMaterial.shownSecond');
       var hidePrev = $('.companySettledVue .hide.prev');
       var shownPrev = $('.companySettledVue .shown.prev');
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
       let _this = this;
       swal({
          title: "你确定修改手机号码吗?",
          text: "更新之后将无法恢复",
          type: "warning",
          showCancelButton: true,
          confirmButtonColor: "#DD6B55",
          confirmButtonText: "是的,我要更新它!",
          closeOnConfirm: false
        },
        function(){
          $.ajax({
            type: 'POST',
            url: '/Shop/SettleModifyPhoneNumber/',
            headers: {
              'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').prop('value')
            },
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            data: {
              objectId: _this.objectId,
              phoneNumber:_this.newPhoneNumber,
              phoneNumberNew: _this.confirmPhoneNumber
            },
            success: function (data) {
              swal("手机号码已经更新");
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
              swal("手机号码更新失败");
            },           
          });
        });
     },
    shops(){
      let i = this.companyshops;
      let shops = i.map(function(item){
        return item.infoCompany;
      });
      return shops;
    },

    }
  }
</script>

<style>
  .settledCompanyDetail div{
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
  .checkSettledCompanyMaterial div{
    margin: 20px;
    font-size: 18px;
  }
  .answer{
    position: absolute;
    left: 450px;
  }
</style>
