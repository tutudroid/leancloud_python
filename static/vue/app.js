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
//stock
//searchMarketCategory
import searchMarketCategory from './backend/market/searchMarketCategory/searchMarketCategory.vue'
//stock
//editMarketCategory
import editMarketCategory from './backend/market/editMarketCategory/editMarketCategory.vue'
//stock
//selfHouse
import selling from './backend/allproduct/selfHouse/selling.vue'
//stock
//selfHouse
import house from './backend/allproduct/selfHouse/house.vue'
//stock
//selfHouse
import addProduct from './backend/allproduct/selfHouse/addProduct.vue'
//selfShop
//initial selfshop
import initialSelfShop from './backend/selfSetting/initialSetting.vue'
//selfShop
//selfShop information management
import selfShopInfoMana from './backend/selfSetting/selfShopInfoMana.vue'
//selfshop
//freight model
import freightModel from './backend/selfManage/freightModel.vue'
//selfshop
//activity management
import activityMana from './backend/selfManage/activityMana.vue'
//selfshop
//brandList
import selfBrandList from './backend/selfManage/brandList.vue'
//sellershop
//brandList
import sellerBrandList from './backend/sellerSetting/brandList.vue'
//business operation
//mpcategoryRecommendation
import homepageSetting from './backend/businessOperation/homepageSetting.vue'
//business operation
//mpcategoryRecommendation
import categoryRecommendation from './backend/businessOperation/categoryRecommendation.vue'
//business operation
//mpcategoryRecommendation
import serviceList from './backend/businessOperation/serviceList.vue'
//business operation
//mpcategoryRecommendation
import bussinessTeamAppUser from './backend/businessOperation/bussinessTeamAppUser.vue'
//business operation
//mpcategoryRecommendation
import bussinessTeamSeller from './backend/businessOperation/bussinessTeamSeller.vue'
//ORDER
//ALL
import mpselfOrderAll from './backend/order/mpselfOrderAll.vue'
//ORDER
//mpselfOrderWaitingMoney
import mpselfOrderWaitingMoney from './backend/order/mpselfOrderWaitingMoney.vue'
//ORDER
//mpselfOrderOnTheRoad
import mpselfOrderOnTheRoad from './backend/order/mpselfOrderOnTheRoad.vue'
//ORDER
//mpselfOrderMoneyBack
import mpselfOrderMoneyBack from './backend/order/mpselfOrderMoneyBack.vue'
//ORDER
//mpselfOrderCustomerWaiting
import mpselfOrderCustomerWaiting from './backend/order/mpselfOrderCustomerWaiting.vue'
//ORDER
//mpselfOrderWaitingComment
import mpselfOrderWaitingComment from './backend/order/mpselfOrderWaitingComment.vue'
//ORDER
//mpselfOrderFinish
import mpselfOrderFinish from './backend/order/mpselfOrderFinish.vue'
//ORDER
//mpselfOrderCancel
import mpselfOrderCancel from './backend/order/mpselfOrderCancel.vue'
//order
//sellerOrder
import mpsellerOrder from './backend/order/mpsellerOrder.vue'
//order
//ordersearch
import orderSearch from './backend/order/orderSearch.vue'
//afterservice
//selfshop
import selfAfterService from './backend/afterService/selfAfterService.vue'
//afterservice
//sellershop
import sellerAfterService from './backend/afterService/sellerAfterService.vue'
//selfInfoCenter
//info
import selfCenter from './backend/selfCenter/selfCenter.vue'
//selfInfoCenter
//changePwd
import selfCenterChangePwd from './backend/selfCenter/selfCenterChangePwd.vue'

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
    allPersonShops:[],
    allCompanyShops:[],
    allAuditShops:[],
    allForbiddenShops:[],
    allStockCategorys:[],
    allMarketCategorys:[],
    allSelfSellingProducts:[],
    allSelfHouseProducts:[],
    selfShopInfoMana:{},
    selfShopFreightModels:[],
    allActivityModels:[],
    allSelfShopBrandLists:[],
    allShops:[],
    serviceList:[],
    selfOrderAll:[],
    selfOrderWaitingMoney:[],
    selfOrderOnTheRoad:[],
    selfOrderMoneyBack:[],
    selfOrderCustomerWaiting:[],
    selfOrderWaitingComment:[],
    selfOrderFinish:[],
    selfOrderCancel:[],
    orderSearch:[],
    selfAfterService:[],
    sellerAfterService:[],
    selfCenter:{},
    selfShopId:"1",
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
      "searchmarketcategory":searchMarketCategory,
      "editmarketcategory":editMarketCategory,
	    "registerform":registerForm,
	    "forgetpwdform":forgetPwdForm,
      "selfselling":selling,
      "selfhouse":house,
      "selfaddproduct":addProduct,
      "initialselfshop":initialSelfShop,
      "selfshopinfomana":selfShopInfoMana,
      "freightmodel":freightModel,
      "activitymana":activityMana,
      "selfbrandlist":selfBrandList,
      "sellerbrandlist":sellerBrandList,
      "homepagesetting":homepageSetting,
      "categoryrecommendation":categoryRecommendation,
      "servicelist":serviceList,
      "bussinessteamappuser":bussinessTeamAppUser,
      "bussinessteamseller":bussinessTeamSeller,
      "mpselforderall":mpselfOrderAll,
      "mpselforderwaitingmoney":mpselfOrderWaitingMoney,
      "mpselforderontheroad":mpselfOrderOnTheRoad,
      "mpselfordermoneyback":mpselfOrderMoneyBack,
      "mpselfordercustomerwaiting":mpselfOrderCustomerWaiting,
      "mpselforderwaitingcomment":mpselfOrderWaitingComment,
      "mpselforderfinish":mpselfOrderFinish,
      "mpselfordercancel":mpselfOrderCancel,
      "mpsellerorder":mpsellerOrder,
      "ordersearch":orderSearch,
      "selfafterservice":selfAfterService,
      "sellerafterservice":sellerAfterService,
      "selfcenter":selfCenter,
      "selfcenterchangepwd":selfCenterChangePwd,
	},
  created:function(){
      $.ajax({
          type: 'GET',
          url: '/Shop/DirectShop/',
          data: {
              
          },
          success: function (data) {
            let rdata = JSON.parse(data);
            _this.selfShopId = rdata.objectId;
          },
         error: function(XMLHttpRequest, textStatus, errorThrown) {
           swal('抓取不到数据')
          },
      });
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
       swal({
        title: "加载中",
        text:"你这么可爱，就等待一下呗",
        timer: 2000,
        showConfirmButton: false
      });
  	},
    //抓取所有的客户端配置
    getAllClientConfigs(){
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
       swal({
        title: "加载中",
        text:"你这么可爱，就等待一下呗",
        timer: 2000,
        showConfirmButton: false
      });
    },
    //抓取所有的个体商户
    getAllPersonShops(){
      let _this = this;
       $.ajax({
          type: 'get',
          url: '/Shop/AllSettleIn/',
          data: {
             state:2,
             page: 1,
             type: 0 
          },
          success: function (data) {
            let dataJson = JSON.parse(data);
            _this.allPersonShops = dataJson.SettleInApplication;
            
          },
         error: function(XMLHttpRequest, textStatus, errorThrown) {
           swal('抓取不到数据')
          },
      });
       swal({
        title: "加载中",
        text:"你这么可爱，就等待一下呗",
        timer: 2000,
        showConfirmButton: false
      });
    },
    //抓取所有的企业商户
    getAllCompanyShops(){
      let _this = this;
       $.ajax({
          type: 'get',
          url: '/Shop/AllSettleIn/',
          data: {
             state:2,
             page: 1,
             type: 1 
          },
          success: function (data) {
            let dataJson = JSON.parse(data);
            _this.allCompanyShops = dataJson.SettleInApplication;
            
          },
         error: function(XMLHttpRequest, textStatus, errorThrown) {
           swal('抓取不到数据')
          },
      });
       swal({
        title: "加载中",
        text:"你这么可爱，就等待一下呗",
        timer: 2000,
        showConfirmButton: false
      });
    },
    //抓取所有的待审核商户
    getAllAuditShops(){
      let _this = this;
       $.ajax({
          type: 'get',
          url: '/Shop/AllSettleIn/',
          data: {
             state:0,
             page: 1,
             type: 0 
          },
          success: function (data) {
            let dataJson = JSON.parse(data);
            _this.allAuditShops = dataJson.SettleInApplication;
            
          },
         error: function(XMLHttpRequest, textStatus, errorThrown) {
           swal('抓取不到数据')
          },
      });
       swal({
        title: "加载中",
        text:"你这么可爱，就等待一下呗",
        timer: 2000,
        showConfirmButton: false
      });
    },
    //抓取所有的禁用商户
    getAllForbiddenShops(){
      let _this = this;
       $.ajax({
          type: 'get',
          url: '/Shop/AllForbiddenShop/',
          data: {
             page: 1,
          },
          success: function (data) {
            let dataJson = JSON.parse(data);
            _this.allForbiddenShops = dataJson.Shop;
            
          },
         error: function(XMLHttpRequest, textStatus, errorThrown) {
           swal('抓取不到数据')
          },
      });
       swal({
        title: "加载中",
        text:"你这么可爱，就等待一下呗",
        timer: 2000,
        showConfirmButton: false
      });
    },
    //抓取所有的库存分类
    getAllStockCategorys(){
      let _this = this;
       $.ajax({
          type: 'get',
          url: '/Product/ShowStoreCategory/',
          data: {
             page: 1,
          },
          success: function (data) {
            let dataJson = JSON.parse(data);
            _this.allStockCategorys = dataJson.StoreCategory;           
          },
          error: function(XMLHttpRequest, textStatus, errorThrown) {
            swal('抓取不到数据')
          },
      });
       swal({
        title: "加载中",
        text:"你这么可爱，就等待一下呗",
        timer: 4000,
        showConfirmButton: false
      });
    },
    //抓取所有的销售分类
    getAllMarketCategorys(){
      let _this = this;
       $.ajax({
          type: 'get',
          url: '/Product/ShowSaleCategory/',
          data: {
             page: 1,
          },
          success: function (data) {
            let dataJson = JSON.parse(data);
            _this.allMarketCategorys = dataJson.SaleCategory;           
          },
          error: function(XMLHttpRequest, textStatus, errorThrown) {
            swal('抓取不到数据')
          },
      });
       swal({
        title: "加载中",
        text:"你这么可爱，就等待一下呗",
        timer: 4000,
        showConfirmButton: false
      });
    },
    //抓取所有的自营正在销售商品
    getAllSelfSellingnProducts(){
      let _this = this;
       $.ajax({
          type: 'get',
          url: '/xx/xx/',
          data: {
             page: 1,
          },
          success: function (data) {
            let dataJson = JSON.parse(data);
            _this.allSelfSellingnProducts = dataJson.xx;           
          },
          error: function(XMLHttpRequest, textStatus, errorThrown) {
            swal('抓取不到数据')
          },
      });
       swal({
        title: "加载中",
        text:"你这么可爱，就等待一下呗",
        timer: 2000,
        showConfirmButton: false
      });
    },
    //抓取所有的自营正在仓库商品
    getAllSelfHouseProducts(){
      let _this = this;
       $.ajax({
          type: 'get',
          url: '/xx/xx/',
          data: {
             page: 1,
          },
          success: function (data) {
            let dataJson = JSON.parse(data);
            _this.allMarketCategorys = dataJson.xx;           
          },
          error: function(XMLHttpRequest, textStatus, errorThrown) {
            swal('抓取不到数据')
          },
      });
       swal({
        title: "加载中",
        text:"你这么可爱，就等待一下呗",
        timer: 2000,
        showConfirmButton: false
      });
    },
    //抓取自营店信息
    getSelfShopInfoMana(){
      let _this = this;
       $.ajax({
          type: 'get',
          url: '/Shop/DirectShop/',
          data: {
      
          },
          success: function (data) {
            let dataJson = JSON.parse(data);
            _this.selfShopInfoMana = dataJson.xx;           
          },
          error: function(XMLHttpRequest, textStatus, errorThrown) {
            swal('抓取不到数据')
          },
      });
        swal({
        title: "加载中",
        text:"你这么可爱，就等待一下呗",
        timer: 2000,
        showConfirmButton: false
      });
    },
    //抓取运费模版信息
    getSelfShopFreightModels(){
      let _this = this;
       $.ajax({
          type: 'get',
          url: '/Shop/AllFreightModel/',
          data: {
            objectId:_this.selfshopid,
          },
          success: function (data) {
            let dataJson = JSON.parse(data);
            _this.SelfShopFreightModels = dataJson.xx;           
          },
          error: function(XMLHttpRequest, textStatus, errorThrown) {
            swal('抓取不到数据')
          },
      });
        swal({
        title: "加载中",
        text:"你这么可爱，就等待一下呗",
        timer: 2000,
        showConfirmButton: false
      });
    },
    getAllActivityModels(){
      let _this = this;
       $.ajax({
          type: 'get',
          url: '/Shop/xx/',
          data: {
      
          },
          success: function (data) {
            let dataJson = JSON.parse(data);
            _this.SelfShopFreightModels = dataJson;           
          },
          error: function(XMLHttpRequest, textStatus, errorThrown) {
            swal('抓取不到数据')
          },
      });
        swal({
        title: "加载中",
        text:"你这么可爱，就等待一下呗",
        timer: 2000,
        showConfirmButton: false
      });
    },
    getAllSelfShopBrandLists(){
       let _this = this;
       $.ajax({
          type: 'get',
          url: '/Shop/AllBrand/',
          data: {
             objectId:_this.selfShopId,
          },
          success: function (data) {
            let dataJson = JSON.parse(data);
            _this.allSelfShopBrandLists = dataJson.xx;           
          },
          error: function(XMLHttpRequest, textStatus, errorThrown) {
            swal('抓取不到数据')
          },
      });
        swal({
        title: "加载中",
        text:"你这么可爱，就等待一下呗",
        timer: 2000,
        showConfirmButton: false
      });
    },
    getAllShops(){
      let _this = this;
       $.ajax({
          type: 'get',
          url: '/Shop/AllSettleIn/',
          data: {
            state:2,
            type:1,
          },
          success: function (data) {
            let dataJson = JSON.parse(data);
            _this.allShops = dataJson.SettleInApplication;           
          },
          error: function(XMLHttpRequest, textStatus, errorThrown) {
            swal('抓取不到数据')
          },
      });
        swal({
        title: "加载中",
        text:"你这么可爱，就等待一下呗",
        timer: 2000,
        showConfirmButton: false
      });
    },
    getServiceList(){
      let _this = this;
       $.ajax({
          type: 'get',
          url: '/Product/AllProductService/',
          data: {
      
          },
          success: function (data) {
            let dataJson = JSON.parse(data);
            _this.serviceList = dataJson.ProductService;           
          },
          error: function(XMLHttpRequest, textStatus, errorThrown) {
            swal('抓取不到数据')
          },
      });
        swal({
        title: "加载中",
        text:"你这么可爱，就等待一下呗",
        timer: 2000,
        showConfirmButton: false
      });
    },
    getSelfOrderAll(){
      let _this = this;
       $.ajax({
          type: 'get',
          url: '/Order/AllOrder/',
          data: {
            objectId:_this.selfShopId, 
            state:-1,
          },
          success: function (data) {
            let dataJson = JSON.parse(data);
            _this.selfOrderAll = dataJson.Order;           
          },
          error: function(XMLHttpRequest, textStatus, errorThrown) {
            swal('抓取不到数据')
          },
      });
        swal({
        title: "加载中",
        text:"你这么可爱，就等待一下呗",
        timer: 2000,
        showConfirmButton: false
      });
    },
    getSelfOrderWaitingMoney(){
      let _this = this;
       $.ajax({
          type: 'get',
          url: '/Order/AllOrder/',
          data: {
            objectId:_this.selfShopId, 
            state:0
          },
          success: function (data) {
            let dataJson = JSON.parse(data);
            _this.selfOrderWaitingMoney = dataJson.Order;           
          },
          error: function(XMLHttpRequest, textStatus, errorThrown) {
            swal('抓取不到数据')
          },
      });
        swal({
        title: "加载中",
        text:"你这么可爱，就等待一下呗",
        timer: 2000,
        showConfirmButton: false
      });
    },
    getSelfOrderOnTheRoad(){
      let _this = this;
       $.ajax({
          type: 'get',
          url: '/Order/AllOrder/',
          data: {
            objectId:this.selfShopId, 
            state:2
          },
          success: function (data) {
            let dataJson = JSON.parse(data);
            _this.selfOrderOnTheRoad = dataJson.Order;           
          },
          error: function(XMLHttpRequest, textStatus, errorThrown) {
            swal('抓取不到数据')
          },
      });
        swal({
        title: "加载中",
        text:"你这么可爱，就等待一下呗",
        timer: 2000,
        showConfirmButton: false
      });
    },
    getSelfOrderMoneyBack(){
      let _this = this;
       $.ajax({
          type: 'get',
          url: '/Order/AllOrder/',
          data: {
            objectId:_this.selfShopId,
            state:6
          },
          success: function (data) {
            let dataJson = JSON.parse(data);
            _this.selfOrderMoneyBack = dataJson.Order;           
          },
          error: function(XMLHttpRequest, textStatus, errorThrown) {
            swal('抓取不到数据')
          },
      });
        swal({
        title: "加载中",
        text:"你这么可爱，就等待一下呗",
        timer: 2000,
        showConfirmButton: false
      });
    },
    getSelfOrderCustomerWaiting(){
      let _this = this;
       $.ajax({
          type: 'get',
          url: '/Order/AllOrder/',
          data: {
            objectId:_this.selfShopId,
            state:1
          },
          success: function (data) {
            let dataJson = JSON.parse(data);
            _this.selfOrderCustomerWaiting = dataJson.Order;           
          },
          error: function(XMLHttpRequest, textStatus, errorThrown) {
            swal('抓取不到数据')
          },
      });
        swal({
        title: "加载中",
        text:"你这么可爱，就等待一下呗",
        timer: 2000,
        showConfirmButton: false
      });
    },
    getSelfOrderWaitingComment(){
      let _this = this;
       $.ajax({
          type: 'get',
          url: '/Order/AllOrder/',
          data: {
            objectId:this.selfShopId,
            state:4
          },
          success: function (data) {
            let dataJson = JSON.parse(data);
            _this.selfOrderWaitingComment = dataJson.Order;           
          },
          error: function(XMLHttpRequest, textStatus, errorThrown) {
            swal('抓取不到数据')
          },
      });
        swal({
        title: "加载中",
        text:"你这么可爱，就等待一下呗",
        timer: 2000,
        showConfirmButton: false
      });
    },
    getSelfOrderFinish(){
      let _this = this;
       $.ajax({
          type: 'get',
          url: '/Order/AllOrder/',
          data: {
            objectId:this.selfShopId,
            state:3
          },
          success: function (data) {
            let dataJson = JSON.parse(data);
            _this.selfOrderFinish = dataJson.Order;           
          },
          error: function(XMLHttpRequest, textStatus, errorThrown) {
            swal('抓取不到数据')
          },
      });
        swal({
        title: "加载中",
        text:"你这么可爱，就等待一下呗",
        timer: 2000,
        showConfirmButton: false
      });
    },
    getSelfOrderCancel(){
      let _this = this;
       $.ajax({
          type: 'get',
          url: '/Order/AllOrder/',
          data: {
            objectId:this.selfShopId,
            state:5
          },
          success: function (data) {
            let dataJson = JSON.parse(data);
            _this.selfOrderCancel = dataJson.Order;           
          },
          error: function(XMLHttpRequest, textStatus, errorThrown) {
            swal('抓取不到数据')
          },
      });
        swal({
        title: "加载中",
        text:"你这么可爱，就等待一下呗",
        timer: 2000,
        showConfirmButton: false
      });
    },
    getOrderSearch(){
      let _this = this;
       $.ajax({
          type: 'get',
          url: '/xx/xx/',
          data: {
      
          },
          success: function (data) {
            let dataJson = JSON.parse(data);
            _this.orderSearch = dataJson.xx;           
          },
          error: function(XMLHttpRequest, textStatus, errorThrown) {
            swal('抓取不到数据')
          },
      });
        swal({
        title: "加载中",
        text:"你这么可爱，就等待一下呗",
        timer: 2000,
        showConfirmButton: false
      });
    },
    getSelfAfterService(){
      let _this = this;
       $.ajax({
          type: 'get',
          url: '/Shop/DirectShop/',
          data: {
           
          },
          success: function (data) {
            let dataJson = JSON.parse(data);
            _this.selfAfterService = dataJson.Order;           
          },
          error: function(XMLHttpRequest, textStatus, errorThrown) {
            swal('抓取不到数据')
          },
      });
        swal({
        title: "加载中",
        text:"你这么可爱，就等待一下呗",
        timer: 2000,
        showConfirmButton: false
      });
    },
    getSellerAfterService(){
      let _this = this;
       $.ajax({
          type: 'get',
          url: '/Shop/AllSettleIn/',
          data: {
            state:2,
            type:0,
          },
          success: function (data) {
            let dataJson = JSON.parse(data);
            _this.sellerAfterService = dataJson;           
          },
          error: function(XMLHttpRequest, textStatus, errorThrown) {
            swal('抓取不到数据')
          },
      });
        swal({
        title: "加载中",
        text:"你这么可爱，就等待一下呗",
        timer: 2000,
        showConfirmButton: false
      });
    },
    getSelf(){
      let _this = this;
       $.ajax({
          type: 'get',
          url: '/xx/xx/',
          data: {
      
          },
          success: function (data) {
            let dataJson = JSON.parse(data);
            _this.selfCenter = dataJson.xx;           
          },
          error: function(XMLHttpRequest, textStatus, errorThrown) {
            swal('抓取不到数据')
          },
      });
        swal({
        title: "加载中",
        text:"你这么可爱，就等待一下呗",
        timer: 2000,
        showConfirmButton: false
      });
    },
    //
  },

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
