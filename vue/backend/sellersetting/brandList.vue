<template>
	<div class="sellerBrandListsVue">
		<div class="t one shown">
	 
	        <div class="row"><div class="col-md-4">商家名</div><div class="col-md-4">品牌号</div><div class="col-md-4">品牌LOGO</div></div>

	        <div  class="link" @click="hideFirst($event)" v-for="shop in allshops"><div class="col-md-4">{{shop.realName}}</div><div class="col-md-4">{{shop.brand}}</div><div class="col-md-4">{{shop.brandLogo}}</div></div>

	    </div>

	    <div class="hide">
	    	<span class="link" @click="showFirst($event)">返回商家列表</span>
	    	<div>
	    		<span class="freightModelsVue link" @click="getSelfShopFreightModels($event)">运费模版</span>
	    		<span class="selfShopManaVue link" @click="getAllActivityModels($event)">自营店信息</span>
	    		<span class="selfBrandListVue link" @click="getAllSelfShopBrandLists($event)">品牌列表</span>
	    	</div>
			<div class="freightModelsVue hidesecond">
				<span class="link" @click="hideFreightModelsVue($event)">返回选项</span>
				<div class="one shown">
					<h2>运费模版</h2>
					<hr>
					<span class="link" @click="toggleAddNew()">新增运费模版</span>
					<div v-for="model in freightmodels">
						<span class="content">model.name</span>\
						<span class="content" v-if="model.isFreightFree">包邮</span><span class="content" v-else>model.freight</span>
						<span class="content link" @click="reviseModel(model.name,model.isFreightFree,model.freight)">修改</span><span class="delemeter">/</span><span class="content link" @click="deleteModel($event,model.objectId)">删除</span>
					</div>
				</div>
				<div class="revise hide">
					<h2>编辑运费模版</h2>
					<hr>
					<span class="link" @click="toggle()">返回</span>
					<label for="modelName">模版名称</label>
					<input id="modelName" type="text" v-model="modelName"></input>
					<input type="radio" v-model="modelFee" v-if="isFreightFree" checked="" :value="true" name="modelFee" ><input type="radio" v-model="modelFee" v-else name="modelFee" :value="true"><label>包邮</label>
					<input type="radio" v-model="modelFee" v-if="!isFreightFree" checked="" name="modelFee" :value="false"><input type="radio" v-model="modelFee" v-else name="modelFee" :value="false"><input type="text" v-model="fee" v-if="!isFreightFree" :value="freight"><input type="text" v-model="fee" v-else ><label>设置运费</label>
					<span @click="saveRevise()">保存</span>
				</div>		
				<div class="addNew hide">
					<h2>新增运费模版</h2>
					<hr>
					<span class="link" @click="toggle()">返回</span>
					<label for="modelName">模版名称</label>
					<input id="modelName" type="text" v-model="modelName"></input>
					<input type="radio" v-model="modelFee" name="modelFee" :value="true"><label>包邮</label>
					<input type="radio" v-model="modelFee" name="modelFee" :value="false"><label>设置运费</label><input type="text" v-model="fee">元
					<span class="link" @click="saveAddNew()" >保存</span>
				</div>
			</div>

			<div class="selfShopManaVue hidesecond">
				<span class="link" @click="hideSelfShopManaVue($event)">返回选项</span>
				<div class="info shown">
					<h2>自营店信息</h2>
					<hr>
					<span class="link" @click="hideInfo()">编辑</span>
					<h3>自营店店名:</h3>
					<div class="content">{{selfshop.name}}</div>
					<h3>管理员手机号</h3>
					<div class="content">{{selfshop.phone}}</div>
				</div>

				<div class="edit hide">
					<h2>修改自营店信息</h2>
					<hr>
					<span class="link" @click="showInfo()">返回</span>
					<label for="selfShopName">自营店名</label>
					<input type="text" v-model="selfShopName" id="selfShopName" class="contentInput" :value="selfshop.name">
					<label for="managerPhone">管理员手机号</label>
					<input type="text" v-model="managerPhone" id="managerPhone" class="contentInput" :value="selfshop.phone">
					<span class="save link" @click="save()">保存</span>
				</div>
			</div>

			<div class="selfBrandListVue hidesecond">
				<span class="link" @click="hideSelfBrandListVue($event)">返回选项</span>
				<div class="shown">
					<span class="link" @click="toggleB('.add')">添加品牌</span>
					<table class="table table-striped">
					<thead>
					<th>品牌名</th><th>品牌Logo</th><th>简介</th><th>编辑</th>
					</thead>
					<tbody>
					<tr v-for="brand in brandlists"><td>brand.name</td><td><img src="brand.imageFile"></td><td>brand.breifDescription</td><td @click="toggleB('.revise',brand.objectId,brand.name,brand.imageFile,brand.breifDescription)">修改</td></tr>
					</tbody>
					</table>
				</div>
				<div class="add hide">
						<h2>添加品牌</h2>
						<hr>
						<span class="link" @click="toggleB('.add')">返回</span>
						<div class="form-group">
						<label for="brandName">品牌名称</label>
						<input type="text" class="form-control" id="brandName" v-model="brandName">
						</div>
						<div class="form-group">
						<label for="file1">添加品牌Logo</label>
						<input class="file" id="file1" type='file' style="display:none;">
						<div id="prev_file1">
						<div class="prev_thumb" style="background-image:url('default.jpg');"></div>
						</div><br/>
						</div>
						<div class="form-group">
						<label for="brandDesc">品牌简介</label>
						<input type="text" class="form-control" id="brandDesc" v-model="brandDesc">
						</div>
						<span class="btn btn-default" @click="addBrand()">确定</span>
				</div>
				<div class="revise hide">
						<h2>修改品牌信息</h2>
						<hr>
						<span class="link" @click="toggleB('.add')">返回</span>
						<div class="form-group">
						<label for="brandName">品牌名称</label>
						<input type="text" class="form-control" id="brandName" v-model="brandName" >
						</div>
						<div class="form-group">
						<label for="file1">添加品牌Logo</label>
						<input class="file" id="file1" type='file' style="display:none;">
						<div id="prev_file1">
						<div class="prev_thumb" :style="'background-image:url('+imageFile+');'"></div>
						</div><br/>
						</div>
						<div class="form-group">
						<label for="brandDesc">品牌简介</label>
						<input type="text" class="form-control" id="brandDesc" v-model="brandDesc">
						</div>
						<span class="btn btn-default" @click="addBrand()">确定</span>
				</div>
			</div>	
		</div>

	</div>
</template>
<script>
	export default{
		data:function(){
			return {
				personMaterial:"",
		        companyMaterial:"",
		        realName:"",
		        //////////////////////
		        modelName:"",
				modelFee:"",
				fee:"",
				/////////////////////
				selfShopName:"",
				managerPhone:"",
				////////////////////
				brandName:"",
				brandDesc:"",
				objectId:"",
				imageFile:"",
				/////////////////////
				freightmodels:[],
				selfshop:{},
				brandlists:[],
			}
		},
		props:["allshops","selfshopid"],
		methods:{
			hideFirst(e){
				let firstHide = $(e.currentTarget).parent();
				firstHide.addClass('hide');
				firstHide.next().removeClass('hide');
			},
			showFirst(e){
				let firstShown = $(e.currentTarget).parent();
				firstShown.addClass('hide');
				firstShown.prev().removeClass('hide');
			},

	  	 /////////////////////////////////////////
	  	 	reviseModel(name,isFreightFree,freight){
				this.modelName = name;
				this.modelFee = isFreightFree;
				this.fee = freight;
				this.toggleRevise();
			},
			saveRevise(){
				let _this = this;
				swal({
		          title: "你确定修改吗?",
		          text: "",
		          type: "warning",
		          showCancelButton: true,
		          confirmButtonColor: "#DD6B55",
		          confirmButtonText: "是的,我确定!",
		          closeOnConfirm: false
		        },
		        function(){
		          $.ajax({
		            type: 'get',
		            url: '/Shop/EditFreightModel/',
		            headers: {
		              'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').prop('value')
		            },
		            contentType: "application/json; charset=utf-8",
		            dataType: "json",
		            data: {		      
		            	name:_this.modelName,
		            	isFreightFree:_this.modelFee,
		            	freight:_this.fee,		
		            },
		            success: function (data) {
		              swal("运费模版已经修改");
		            },
		            error: function(XMLHttpRequest, textStatus, errorThrown) {
		              swal("运费模版修改失败");
		            },           
		          });
        		});
			},
			saveAddNew(){
				let _this = this;
				swal({
		          title: "你确定新增吗?",
		          text: "",
		          type: "warning",
		          showCancelButton: true,
		          confirmButtonColor: "#DD6B55",
		          confirmButtonText: "是的,我确定!",
		          closeOnConfirm: false
		        },
		        function(){
		          $.ajax({
		            type: 'get',
		            url: '/Shop/EditFreightModel/',
		            headers: {
		              'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').prop('value')
		            },
		            contentType: "application/json; charset=utf-8",
		            dataType: "json",
		            data: {
		            	objectId:_this.selfshopid,
		            	name:_this.modelName,
		            	isFreightFree:_this.modelFee,
		            	freight:_this.fee,		
		            },
		            success: function (data) {
		              swal("运费模版已经新增");
		            },
		            error: function(XMLHttpRequest, textStatus, errorThrown) {
		              swal("运费模版新增失败");
		            },           
		          });
        		});
			},
			deleteModel(e,id){
				let _this = this;
				let record = $(e.currentTarget).parent();
				swal({
		          title: "你确定删除这个运费模版吗?",
		          text: "删除模版之后将无法恢复",
		          type: "warning",
		          showCancelButton: true,
		          confirmButtonColor: "#DD6B55",
		          confirmButtonText: "是的,我确定删除!",
		          closeOnConfirm: false
		        },
		        function(){
		          $.ajax({
		            type: 'get',
		            url: '/Shop/DeleteFreightModel/',
		            headers: {
		              'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').prop('value')
		            },
		            contentType: "application/json; charset=utf-8",
		            dataType: "json",
		            data: {
		            	objectId:id,		           
		            },
		            success: function (data) {
		              swal("运费模版已经成功删除");
		              $(record).remove();
		            },
		            error: function(XMLHttpRequest, textStatus, errorThrown) {
		              swal("运费模版删除失败");
		            },           
		          });
        		});
			},
			///////////////////////////////////////////////////
			save(){
				let _this = this;
				swal({
		          title: "确定修改自营商铺信息吗?",
		          text: "",
		          type: "warning",
		          showCancelButton: true,
		          confirmButtonColor: "#DD6B55",
		          confirmButtonText: "是的,我确认!",
		          closeOnConfirm: false
		        },
		        function(){
		          $.ajax({
		            type: 'get',
		            url: '/Shop/EditDirectShop/',
		            headers: {
		              'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').prop('value')
		            },
		            contentType: "application/json; charset=utf-8",
		            dataType: "json",
		            data: {
		            	objectId:_this.selfshopid,
					    shopName: _this.selfShopName,
					    phoneNumber: _this.managerPhone,
		            },
		            success: function (data) {
		              swal("信息已经修改");
		            },
		            error: function(XMLHttpRequest, textStatus, errorThrown) {
		              swal("信息修改失败");
		            },           
		          });
        		});
			},
			//////////////////////////////////////////////////
			addBrand(){
				let _this = this;
				let image = $('.add prev_thumb').attr("src").slice(23);
				swal({
		          title: "你确定新增吗?",
		          text: "",
		          type: "warning",
		          showCancelButton: true,
		          confirmButtonColor: "#DD6B55",
		          confirmButtonText: "是的,我要增加!",
		          closeOnConfirm: false
		        },
		        function(){
		          $.ajax({
		            type: 'xx',
		            url: '/xx/xx/',
		            headers: {
		              'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').prop('value')
		            },
		            contentType: "application/json; charset=utf-8",
		            dataType: "json",
		            data: {
		            	brandDesc:_this.brandDesc,
		            	brandName:_this.brandName,
		            	imageFile:image,
		            },
		            success: function (data) {
		              swal("自营品牌新增成功");
		            },
		            error: function(XMLHttpRequest, textStatus, errorThrown) {
		              swal("自营品牌新增失败");
		            },           
		          });
        		});
			},
			revise(){
				let _this = this;
				let image = $('.revise prev_thumb').attr("src").slice(23);
				if(_this.brandDesc=="" || _this.brandName=="" || _this.objectId=="" || image==null){
					swal("存在空值");
				}else{
					swal({
			          title: "你确定修改吗?",
			          text: "",
			          type: "warning",
			          showCancelButton: true,
			          confirmButtonColor: "#DD6B55",
			          confirmButtonText: "是的,我要修改!",
			          closeOnConfirm: false
			        },
			        function(){
			          $.ajax({
			            type: 'xx',
			            url: '/xx/xx/',
			            headers: {
			              'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').prop('value')
			            },
			            contentType: "application/json; charset=utf-8",
			            dataType: "json",
			            data: {
			            	brandDesc:_this.brandDesc,
			            	brandName:_this.brandName,
			            	objectId:_this.objectId,
			            	imageFile:image,
			            },
			            success: function (data) {
			              swal("自营品牌修改成功");
			            },
			            error: function(XMLHttpRequest, textStatus, errorThrown) {
			              swal("自营品牌修改失败");
			            },           
			          });
	        		});
	        	}
			},
			///////////////////////////////////////////
			showFreightModelsVue(e){
				let shown = $(e.currentTarget).parent();
				shown.addClass('hidesecond');
				shown.next().removeClass('hidesecond')
			},
			hideFreightModelsVue(e){
				let hide =$(e.currentTarget).parent();
				hide.addClass('hidesecond');
				hide.prev().removeClass('hidesecond');
			},
			showSelfShopManaVue(e){
				let shown = $(e.currentTarget).parent();
				shown.addClass('hidesecond');
				shown.next().next().removeClass('hidesecond')
			},
			hideSelfShopManaVue(e){
				let hide =$(e.currentTarget).parent();
				hide.addClass('hidesecond');
				hide.prev().prev().removeClass('hidesecond');
			},
			showSelfBrandListVue(e){
				let shown = $(e.currentTarget).parent();
				shown.addClass('hidesecond');
				shown.next().next().next().removeClass('hidesecond')
			},
			hideSelfBrandListVue(e){
				let hide =$(e.currentTarget).parent();
				hide.addClass('hidesecond');
				hide.prev().prev().prev().removeClass('hidesecond');
			},
			toggle(){
				let hide = $('.freightModelsVue').children('.one');
				let hideAddNew = $('.freightModelsVue .addNew');
				let hideRevise = $('.freightModelsVue .revise');
				if(hideAddNew.hasClass('shown')){
					hideAddNew.removeClass('shown').addClass('hide');
					hide.removeClass('hide').addClass('shown');
				}
				if(hideRevise.hasClass('shown')){
					hideRevise.removeClass('shown').addClass('hide');
					hide.removeClass('hide').addClass('shown');
				}
			},
			toggleAddNew(){
				this.modelFee = "";
				this.modelName = "";
				this.fee = "";
				let shown = $('.freightModelsVue .one');
				let hideAddNew = $('.freightModelsVue .addNew');
				if(shown.hasClass('shown')){
					shown.removeClass('shown').addClass('hide');
				}
				if(hideAddNew.hasClass('hide')){
					hideAddNew.removeClass('hide').addClass('shown');
				}
				
			},
			toggleRevise(){
				let shown = $('.freightModelsVue .one');
				let hideRevise = $('.freightModelsVue .revise');
				if(shown.hasClass('shown')){
					shown.removeClass('shown').addClass('hide');
				}
				if(hideRevise.hasClass('hide')){
					hideRevise.removeClass('hide').addClass('shown');
				}

			},
			hideInfo(){
				let shown = $('.selfShopManaVue .info');
				let hide = $('.selfShopManaVue .edit');
				if(shown.hasClass('shown')){
					shown.removeClass('shown').addClass('hide');
				}
				if(hide.hasClass('hide')){
					hide.removeClass('hide').addClass('shown');
				}
			},
			showInfo(){
				let shown = $('.selfShopManaVue .info');
				let hide = $('.selfShopManaVue .edit');
				if(shown.hasClass('hide')){
					shown.removeClass('hide').addClass('shown');
				}
				if(hide.hasClass('shown')){
					hide.removeClass('shown').addClass('hide');
				}
			},
			toggleB(hideName="hide",id="",name="",imageFile="",desc=""){
				if(hideName = ".add"){
					this.brandDesc="";
					this.brandName="";
				}else{
					this.brandName = name;
					this.brandDesc = desc;
					this.objectId = id;
					this.imageFile = imageFile;
				}
				let shown = $('.selfBrandListVue .shown');
				let hide = $('.selfBrandListVue'+hideName);
				if(shown.hasClass('.shown')){
					shown.removeClass('shown').addClass('hide');
				}
				if(hide.hasClass('hide')){
					hide.removeClass('hide').addClass('shown');
				}
			},
			/////////////////////////////////////////////////////////////////
			 //抓取运费模版信息
		    getSelfShopFreightModels(e){
		      let _this = this;
		      let ok = 0;
		       $.ajax({
		          type: 'get',
		          url: '/Shop/AllFreightModel/',
		          data: {
		            objectId:_this.selfshopid,
		          },
		          success: function (data) {
		            let dataJson = JSON.parse(data);
		            _this.freightmodels = dataJson.xx;
		            ok = 1;           
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
		        	
		        this.showFreightModelsVue(e);
		        
		    },
		    getAllActivityModels(e){
		      let _this = this;
		      let ok = 0;
		       $.ajax({
		          type: 'get',
		          url: '/Shop/xx/',
		          data: {
		      
		          },
		          success: function (data) {
		            let dataJson = JSON.parse(data);
		            _this.brandlists = dataJson;   
		            ok = 1;        
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
		     
		        this.showSelfShopManaVue(e);
		        
		    },
		    getAllSelfShopBrandLists(){
		       let _this = this;
		       let ok = 0;
		       $.ajax({
		          type: 'get',
		          url: '/Shop/AllBrand/',
		          data: {
		             objectId:_this.selfShopId,
		          },
		          success: function (data) {
		            let dataJson = JSON.parse(data);
		            _this.selfshop = dataJson.xx;
		            ok = 1;           
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
		        
		        this.showSelfBrandListVue(e);
		        
		    },

  },
}
</script>
<style lang="scss">
	.sellerBrandListsVue{
		.hidesecond{
			display:none;
		}
	}
</style>