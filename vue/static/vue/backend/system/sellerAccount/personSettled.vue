<template>
  <div class="personSettledVue">
    <table class="table table-striped one shown" v-if="personshops.length > 0">
      <thead>
        <tr><td>商家名</td><td>品牌名</td><td>品牌LOGO</td><td>入驻类型</td><td>状态</td></tr>
      </thead>

      <tbody>
        <tr v-for="shop in shops()" class="personRow pointer" @click='settledPersonDetail(shop.objectId,shop.realName,shop.phoneNumber,shop.shopName,shop.brandName,shop.brandLogo,shop.brandDescription,"person",shop.state,shop.email,shop.idCard,shop.idCardExpireTimeEnd,shop.idCardExpireTimeStart,shop.frontIdCard,shop.backIdCard,shop.handIdCard,shop.alipay)'><td>{{shop.realName}}</td><td>{{shop.brandName}}</td><td>{{shop.brandLogo}}</td><td>person</td><td>{{shop.state}}</td></tr>
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
              店铺名：{{shopName}}
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
        objectId:-1,
      	name:"",
      	phoneNumber:"",
      	shopName:"",
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
        state:0,
      }
    },
    props:["personshops"],
    methods: {
      settledPersonDetail(settledPersonId,name,phoneNumber,shop_name,brandName,brandLogo,brandDescription,type,state,email,IdCard,idCardExpireTimeStart,idCardExpireTimeEnd,frontIdCard,backIdCard,handIdCard,alipay){
        this.objectId = settledPersonId;
      	this.name = name;
      	this.phoneNumber = phoneNumber;
      	this.shopName = shop_name;
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
        this.state = state;
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
       _this = this;
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
              'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').prop('value')
            },
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            data: {
              objectId: _this.objectId,
              phoneNumber: _this.newPhoneNumber,
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
      let i = this.personshops;
      let shops = i.map(function(item){
        return item.infoPersonal;
      });
      return shops;
    },
  },
  computed:{
    
  },
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
