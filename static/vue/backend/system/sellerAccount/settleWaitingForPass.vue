<template>
  <div class="container settleWaitingForPassVue">
    <div class="t one shown" v-if="auditshops.length > 0">
 
        <div class="row"><div class="col-md-4">账号名</div><div class="col-md-4">手机号</div><div class="col-md-4">入驻类型</div></div>

        <div v-for="shop in shops()">
          <div v-if="shop.flag==0" class="tr personRow pointer row" @click='fillOutPersonMaterial(shop.objectId,shop.flag,shop.realName,shop.phoneNumber,shop.email,shop.idCard,shop.idCardExpireTimeStart,shop.idCardExpireTimeEnd,shop.frontIdCard,shop.backIdCard,shop.handIdCard,shop.alipay,shop.shopName,shop.brandName,shop.brandLogo,shop.brandDescription)'><div class="col-md-4">{{shop.realName}}</div><div class="col-md-4">{{shop.phoneNumber}}</div><div class="col-md-4">个人</div></div>
          <div v-if="shop.flag==1" class="tr personRow pointer row" @click='fillOutCompanyMaterial(shop.objectId,shop.flag,shop.uniformSocialCreditCode,shop.bussinessLicense,shop.legalPersonName,shop.legalPersonPhoneNumber,shop.legalPersonEmail,shop.legalPersonIdCard,shop.legalPersonExpireTimeStart,shop.legalPersonExpireTimeEnd,shop.legalPersonFrontIdCard,shop.legalPersonBackIdCard,shop.alipay,shop.managerRealName,shop.managerEmail,shop.managerPhoneNumber,shop.shopName,shop.brandName,shop.brandLogo,shop.brandDescription)'><div class="col-md-4">{{shop.managerRealName}}</div><div class="col-md-4">{{shop.managerPhoneNumber}}</div><div class="col-md-4">企业</div></div>
        </div>

    </div>


  <div class="checkPersonMaterial hide">
    <h2>入驻资料</h2>
    <hr>

    <div class="name">
    入驻真实姓名: <span class="answer">{{realName}}</span>
    </div>
    <div class="phoneNumber">
    手机号: <span class="answer">{{phoneNumber}}</span>
    </div>
    <div class="email">
    电子邮箱: <span class="answer">{{email}}</span>
    </div>
    <div class="IdCard">
    身份证号: <span class="answer">{{idCard}}</span>
    </div>
    <div class="idCardTime">
    身份证有效期: <span class="answer">{{idCardExpireTimeStart}}至{{idCardExpireTimeEnd}}}</span>
    </div>
    <div class="frontIdCard">
    身份证正面: <img class="answer pointer" :src="frontIdCard" width="100px" height="100px">
    </div>
    <div class="backIdCard">
    身份证反面: <img class="answer pointer" :src="backIdCard" width="100px" height="100px">
    </div>
    <div class="handIdCard">
    手持身份证照片: <img class="answer pointer" :src="handIdCard" width="100px" height="100px">
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

    <hr>

    <div>
      <span class="audit" @click="pass(id,1)">通过</span><span class="audit" @click="pass(id,0)">拒绝</span>
    </div>

    <hr>

    <div class="link" @click="toggleShow(id,type)">
      返回
    </div>

    

  </div>

  

  
  <div class="checkCompanyMaterial hide">
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

    <hr>

    <div>
      <span class="audit" @click="pass(id,1)">通过</span><span class="audit" @click="pass(id,0)">拒绝</span>
    </div>

    <hr>

    <div class="link" @click="toggleShow(id,type)">
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
      	personMaterial:"",
      	companyMaterial:"",
      	realName:"",
      	phoneNumber:"",
      	email:"",
      	idCard:"",
      	idCardExpireTimeStart:"",
      	idCardExpireTimeEnd:"",
      	frontIdCard:"",
      	backIdCard:"",
      	handIdCard:"",
      	alipay:"",
      	shopName:"",
      	brandName:"",
      	brandLogo:"",
      	brandDescription:"",
        uniformSocialCreditCode:"",
      	bussinessLicense:"",
      	legalPersonName:"",
      	legalPersonPhoneNumber:"",
      	legalPersonEmail:"",
      	legalPersonIdCard:"",
      	legalPersonExpireTimeStart:"",
      	legalPersonExpireTimeEnd:"",
      	legalPersonFrontIdCard:"",
      	legalPersonBackIdCard:"",
        managerRealName:"",
      	managerEmail:"",
      	managerPhoneNumber:"",
      	shopName:"",
      	id:"",
      	type:"",
      }
    },
    props:["auditshops"],
    methods: {
     toggleShow(id,type){
       var show = $(".settleWaitingForPassVue .shown");
       var mainHide = $(".t.hide");
       if(mainHide.hasClass('hide')){
         mainHide.removeClass('hide').addClass('shown');
       }
       if(type == 0){
       
       var hide = $(".checkPersonMaterial.hide");
       
       }
       if(type == 1){
       
       var hide = $(".checkCompanyMaterial.hide");
       }
       if(show != null){
         show.removeClass("shown").addClass("hide");
       }
       if(hide != null){
         hide.removeClass("hide").addClass("shown");
       }
     },
     fillOutPersonMaterial(id,type,name,phoneNumber,email,IdCard,idCardExpireTimeStart,idCardExpireTimeEnd,frontIdCard,backIdCard,handIdCard,alipay,shop_name,brandName,brandLogo,brandDescription){
       this.id = id;
       this.realName = name;
       this.type = type;
       this.phoneNumber = phoneNumber;
       this.email = email;
       this.idCard = IdCard;
       this.idCardExpireTimeStart = idCardExpireTimeStart;
       this.idCardExpireTimeEnd = idCardExpireTimeEnd;
       this.frontIdCard = frontIdCard;
       this.backIdCard = backIdCard;
       this.handIdCard = handIdCard;
       this.alipay = alipay;
       this.shopName = shop_name;
       this.brandName = brandName;
       this.brandLogo = brandLogo;
       this.brandDescription = brandDescription;
       this.toggleShow(id,type);
      
     },
     fillOutCompanyMaterial(id,type,uniformSocialCreditCode,bussinessLicense,legalPersonName,legalPersonPhoneNumber,legalPersonEmail,legalPersonIdCard,legalPersonExpireTimeStart,legalPersonExpireTimeEnd,legalPersonFrontIdCard,legalPersonBackIdCard,alipay,managerRealName,managerEmail,managerPhoneNumber,shopName,brandName,brandLogo,brandDescription){
       this.id = id;
       this.type = type;
       this.uniformSocialCreditCode = uniformSocialCreditCode;
       this.bussinessLicense = bussinessLicense;
       this.legalPersonName = legalPersonName;
       this.legalPersonPhoneNumber = legalPersonPhoneNumber;
       this.legalPersonEmail = legalPersonEmail;
       this.legalPersonIdCard = legalPersonIdCard;
       this.legalPersonExpireTimeStart = legalPersonExpireTimeStart;
       this.legalPersonExpireTimeEnd = legalPersonExpireTimeEnd;
       this.legalPersonFrontIdCard = legalPersonFrontIdCard;
       this.legalPersonBackIdCard = legalPersonBackIdCard;
       this.alipay = alipay;
       this.managerRealName = managerRealName;
       this.managerEmail = managerEmail;
       this.managerPhoneNumber = managerPhoneNumber;
       this.shopName = shopName;
       this.brandName = brandName;
       this.brandLogo = brandLogo;
       this.brandDescription = brandDescription;
       this.toggleShow(id,type);
     
     },
     pass(id,state){
       let _this = this;
       if(state == 1){
    	 swal(
      	   {
      	     title:"你确定通过它吗？",
      	     text:"通过之后此商家将成为入驻商家",
      	     type:"warning",
      	     showCancelButton:true,
      	     closeOnConfirm:false,
      	     confirmButtonText:"是的，我要让它入驻",
      	     confirmButtonColor:"ec6c62",
      	   },function(){
              $.ajax({
                type: 'get',
                url: '/Shop/ReviewSettleIn/',
                data: {
                   'objectId': _this.id,
                   'state': 2,
                },
                success: function (data) {
                  swal("此商家成功入驻");
                  
                },
               error: function(XMLHttpRequest, textStatus, errorThrown) {
                 swal("无法入驻此商家...");
                },
            });
      	   });
      }else{
    	 swal(
      	   {
      	     title:"你确定拒绝它吗？",
      	     text:"拒绝之后此商家将无法成为入驻商家",
      	     type:"warning",
      	     showCancelButton:true,
      	     closeOnConfirm:false,
      	     confirmButtonText:"是的，我要拒绝它入驻",
      	     confirmButtonColor:"ec6c62",
      	   },function(){
          		$.ajax({
                    type: 'get',
                    url: '/Shop/ReviewSettleIn/',
                    data: {
                       'objectId': _this.id,
                       'state': 1,
                    },
                    success: function (data) {
                      swal("已成功拒绝此商家入驻");
                      
                    },
                   error: function(XMLHttpRequest, textStatus, errorThrown) {
                     swal("无法拒绝此商家入驻");
                    },
              });
          });
  }
  },
  shops(){
      let i = this.auditshops;
      let shops = i.map(function(item){
        if(item.type == 1){
          item.infoCompany.flag = 1;
          return item.infoCompany;
        }else{
          item.infoPersonal.flag = 0;
          return item.infoPersonal;
        }        
      });
      return shops;
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
  .audit{
    border: 2px solid;
    background-color: cyan;
    padding: 10px;
    margin: 10px;
    cursor:pointer;
    
  }
  .personRow{
    position: relative;
    top: 20px;
    border-top:1px solid #c5c1c1;
  }
  .frontIdCard,.handIdCard,.backIdCard{
      height: 100px;
      margin: 100px 0;
  }
</style>
