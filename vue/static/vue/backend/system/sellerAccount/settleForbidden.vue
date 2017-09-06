<template>
  <div class="settleForbiddenVue">
    <table class="table table-striped one shown" v-if="forbiddenshops.length > 0">
      <thead>
        <tr><td>商家名字</td><td>品牌名</td><td>品牌Logo</td><td>入驻类型</td><td>状态</td></tr>
      </thead>

      <tbody>
        <tr v-for="shop in shops()" v-if="shop.type=0" class="personRow pointer" @click='fillOutPersonMaterial(shop.id,shop.type,shop.realName,shop.phoneNumber,shop.email,shop.IdCard,shop.idCardExpireTimeStart,shop.idCardExpireTimeEnd,shop.frontIdCard,shop.backIdCard,shop.handIdCard,shop.alipay,shop.shopName,shop.brandName,shop.brandLogo,shop.brandDescription)'><td>shop.realName</td><td>shop.phoneNumber</td><td>个人</td><td>禁用</td></tr>
        <tr v-for="shop in shops()" v-if="shop.type=1" class="personRow pointer" @click='fillOutCompanyMaterial(id,shop.type,shop.uniformSocialCreditCode,shop.bussinessLicense,shop.legalPersonName,shop.legalPersonPhoneNumber,shop.legalPersonEmail,shop.legalPersonIdCard,shop.legalPersonExpireTimeStart,shop.legalPersonExpireTimeEnd,shop.legalPersonFrontIdCard,shop.legalPersonBackIdCard,shop.alipay,shop.managerRealName,shop.managerEmail,shop.managerPhoneNumber,shop.shopName,shop.brandName,shop.brandLogo,shop.brandDescription)'><td>shop.managerRealName</td><td>shop.managerPhoneNumber</td><td>企业</td><td>禁用</td></tr>
      </tbody>
    </table>


  <div class="checkPersonMaterial hide">
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
    身份证有效期: <span class="answer">{{idCardExpireTimeStart}}至{{idCardExpireTimeEnd}}}</span>
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

    <div class="link" @click="toggleShow(id,type)">
      返回
    </div>

    <hr>

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
      	name:"",
      	phoneNumber:"",
      	email:"",
      	IdCard:"",
      	idCardExpireTimeStart:"",
      	idCardExpireTimeEnd:"",
      	frontIdCard:"",
      	backIdCard:"",
      	handIdCard:"",
      	alipay:"",
      	shop_name:"",
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
    props:["forbiddenshops"],
    methods: {
     toggleShow(id,type){
       var show = $(".settleForbiddenVue .shown");
       var mainHide = $(".table.hide");
       if(mainHide.hasClass('hide')){
         mainHide.removeClass('hide').addClass('shown');
       }
       if(type == "个人"){
       
       var hide = $(".checkPersonMaterial.hide");
       
       }
       if(type == "企业"){
       
       var hide = $(".checkCompanyMaterial.hide");
       }
       if(show != null){
         show.removeClass("shown").addClass("hide");
       }
       if(hide != null){
         hide.removeClass("hide").addClass("shown");
       }
     },
     fillOutPersonMaterial(id,type,name,phoneNumber,email,IdCard,idCardExpireTimeStart,idCardExpireTimeEnd,frontIdCard,backIdCard,handIdCard,alipay,shop_name,brandName,brandLogo,brandDescription,){
       this.id = id;
       this.name = name;
       this.type = type;
       this.phoneNumber = phoneNumber;
       this.email = email;
       this.IdCard = IdCard;
       this.idCardExpireTimeStart = idCardExpireTimeStart;
       this.idCardExpireTimeEnd = idCardExpireTimeEnd;
       this.frontIdCard = frontIdCard;
       this.backIdCard = backIdCard;
       this.handIdCard = handIdCard;
       this.alipay = alipay;
       this.shop_name = shop_name;
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
     shops(){
      let i = this.auditshops;
      let shops = i.map(function(item){
        return item.infoCompany;
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
</style>
