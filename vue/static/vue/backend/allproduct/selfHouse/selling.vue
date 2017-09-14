<template>
	<div class="selfSellingVue">
		<table class="table table-striped shown" v-if="allselfselligproducts.length > 0">
		  <thead>
		  	<th>商品名</th>
		  	<th>编号</th>
		  	<th>价格</th>
		  	<th>库存</th>
		  	<th>销量</th>
		  	<th>创建时间</th>
		  	<th>商家</th>
		  	<th>状态</th>
		  	<th>操作</th>
		  </thead>
		  <tbody>
		  	<tr v-for="product in allselfselligproducts" @click="showDetail(product.objectId,product.uniqueId,product.propertyOption,product.name,product.productService,product.ip,product.brand,product.saleCategory,product.storeCategory,product.mainImage,product.imageList,product.collectionUser,product.comment,product.briefDescription,product.detailDescription,product.shop,product.saleCount,product.price,product.spec,product.freightModel,product.state)"> 
		  		<td>{{product.name}}</td>
		  		<td>{{product.uniqueId}}</td>
		  		<td>{{product.price}}</td>
		  		<td>{{product.stockCount}}</td>
		  		<td>{{product.saleCount}}</td>
		  		<td>{{product.created_at}}</td>
		  		<td>{{product.shop}}</td>
		  		<td>{{product.state}}<span class="link" @click="getItDown($event,product.uniqueId)"><span class="on default">下架</span><span class="off">已下架</span></span></td>
		  		<td><span class="link" @click="editDetail(product.objectId,product.uniqueId,product.propertyOption,product.name,product.productService,product.ip,product.brand,product.saleCategory,product.storeCategory,product.mainImage,product.imageList,product.collectionUser,product.comment,product.briefDescription,product.detailDescription,product.shop,product.saleCount,product.price,product.spec,product.freightModel,product.state)">编辑</span><span class="link" @click="deleteProduct($event,product.uniqueId)">删除</span></td>
		  	</tr>
		  </tbody>
		</table>

		<div class="productDetail hide">
			<span class="link" @click="toggleShow()">返回</span>
			<h2>商品详情</h2>
			<h3>商品名：{{this.name}}</h3>
			<h3>商品简介：{{this.description}}</h3>
			<div class="mainImages">
				<img class="image" v-for="image in this.imageList"></img>
			</div>
			<div class="propertyOption">
				<table>
					<thead>
						<th v-for="option in this.propertyOption">{{option}}</th>
						<th>价格</th>
						<th>数量</th>
						<th>销量</th>
					</thead>
						<th>图片</th>
					<tbody>
						<tr v-for="option in this.propertyOption">
							<td>option.name</td>
							<td>
								<table>
									<tr v-for="soption in option.soption">
										<td>{{soption.name}}</td>
										<td>{{soption.price}}</td>
										<td>{{soption.quantity}}</td>
										<td>{{soption.saleCount}}</td>
										<td>{{soption.image}}</td>
									</tr>
								</table>
							</td>
						</tr>
					</tbody>
				</table>
			</div>
			<div class="comment">
				<h2 data-toggle="modal" data-target=".commentContent">用户评价（{{commentCount}}）</h2>
				<div class="commentContent modal fade" v-for="comment in comment">
					<div class="media modal-dialog">
						<div class="modal-content">
							<div class="modal-body">
								<div class="media-left media-middle"> 
									<a href="#"> 
									<img alt="64x64" class="media-object" data-src="holder.js/64x64" :src="comment.userAvatar" data-holder-rendered="true" style="width: 64px; height: 64px;"> </a> 
								</div>
								<div class="media-body"> 
									<h4 class="media-heading">{{comment.created_at}}</h4> 
									<p>{{comment.content}}</p> 
									<p v-for="image in comment.imageList">
										<img src="image">
									</p> 
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
			<h3>运费:{{this.freightModel}}</h3>
			<h3>总销量:{{this.saleCount}}</h3>
			<h3>收藏:{{this.collection}}</h3>
			<h3>创建时间:{{this.created_at}}</h3>
			<h3>库存分类:{{this.storeCategory}}</h3>
			<h3>销售分类:{{this.saleCategory}}</h3>
			<h3>商家:{{this.shop}}</h3>
			<div class="service">
				<div class="serviceHeadline">
					商品服务：
				</div>
				<div class="content">
					<div v-for="service in this.productService">
						{{service}}
					</div>
				</div> 
			</div>
			<div class="spec">
				<table>
					<thead>
						<th>规格项</th>
						<th>内容</th>
					</thead>
					<tbody>
						<tr v-for="spec in this.spec">
							<td>{{spec.name}}</td>
							<td>{{spec.content}}</td>
						</tr>
					</tbody>
				</table>
			</div>
			<div class="mainImage">
				<h2>商品详情:</h2>
				<img :src="this.mainImage">
			</div>

		</div>

		<div class="editDetail hide">
			<span class="link" @click="toggleEdit()">返回</span>
			<div class="storeCateogry">
				<h2>库存分类:</h2>
				<div class="content">
					<select model="storeCategoryFirst" @click="clickFirst()" id="first" @change="changeSecond()" v-model="firstCate">
						<option>{{storeCategory.firstname}}</option>
					</select>
					<select model="storeCategorySecond" id="second" @change="changeThird()" v-model="secondCate">
						<option v-for="(cate,index) in storeCategorySecond" :value="index">{{cate.secondname}}</option>
					</select>
					<select model="storeCategoryThird" id="third" v-model="thirdCate">
						<option v-for="cate in storeCategorySecond[secondCate].storeCategoryThird">{{cate.thirdname}}</option>
					</select>
				</div>
			</div>
			<div class="saleCateogry">
				<h2>销售分类:</h2>
				<div class="content">
					<select model="saleCategoryFirst">
						<option>{{saleCategory.firstname}}</option>
					</select>
					<select model="saleCategorySecond">
						<option>{{saleCategory.secondname}}</option>
					</select>
				</div>
			</div>		
			<h3>品牌名：<input type="text" :value="brand" model="brand"></h3>
			<h3>商品名：<input type="text" :value="name" model="name"></h3>
			<h3>商品简介：<input type="text" :value="description" model="description"></h3>
			<div class="mainImages">
				<div class="image" v-for="image in this.imageList"><img :src="image" /><span class="ope


				rate" @click="deleteImage(image.objectId)">删除</span></div>
				<div class="imageList" v-for="n in 5-this.imageList.length"><label @click="addImage()">新增图片</label><input class="file" :id="'file'+n" type='file' /><div :id="'prev_file'+n"></div><br/></div>
			</div>
			<!--<div class="propertyOption">
				<table>
					<thead>
						<th v-for="option in this.propertyOption">{{option}}</th>
						<th>价格</th>
						<th>数量</th>
						<th>销量</th>
					</thead>
						<th>图片</th>
					<tbody>
						<tr v-for="option in this.propertyOption">
							<td>option.name</td>
							<td>
								<table>
									<tr v-for="soption in option.soption">
										<td>{{soption.name}}</td>
										<td>{{soption.price}}</td>
										<td>{{soption.quantity}}</td>
										<td>{{soption.saleCount}}</td>
										<td>{{soption.image}}</td>
									</tr>
								</table>
							</td>
						</tr>
					</tbody>
				</table>
			</div>-->
			<div class="service">
				<div class="serviceHeadline">
					商品服务：
				</div>
				<div class="content">
					<div v-if="this.productService.find(function(item){return item.name == '24小时内发货'})">
						<input type="checkbox" id="send" value="24小时内发货" v-model="checkedProductNames" checked="">
			  			<label for="send">24小时内发货</label>
					</div>
					<div v-else>
						<input type="checkbox" id="send" value="24小时内发货" v-model="checkedProductNames">
			  			<label for="send">24小时内发货</label>
					</div>
					<div v-if="productService.find(function(item){return item.name == '7天无理由退货'})">
						<input type="checkbox" id="rejected" value="7天无理由退货" v-model="checkedProductNames" checked="">
			  			<label for="rejected">7天无理由退货</label>
					</div>
					<div v-else>
						<input type="checkbox" id="rejected" value="7天无理由退货" v-model="checkedProductNames">
			  			<label for="rejected">7天无理由退货</label>
					</div>
					<div v-if="productService.find(function(item){return item.name == '正品保证'})">
						<input type="checkbox" id="promised" value="正品保证" v-model="checkedProductNames" checked="">
			  			<label for="promised">正品保证</label>
					</div>
					<div v-else>
						<input type="checkbox" id="promised" value="正品保证" v-model="checkedProductNames">
			  			<label for="promised">正品保证</label>
					</div>
					<div v-if="productService.find(function(item){return item.name == '包邮'})">
						<input type="checkbox" id="logisticFree" value="包邮" v-model="checkedProductNames" checked="">
			  			<label for="logisticFree">包邮</label>
					</div>
					<div v-else>
						<input type="checkbox" id="logisticFree" value="包邮" v-model="checkedProductNames">
			  			<label for="logisticFree">包邮</label>
					</div>
				</div> 
			</div>
			<div class="freightModel">
				<h2>运费：</h2>
				<div class="content">
					<select model="freightModel">
						<option>
							{{this.freightModel}}
						</option>
					</select>
					<span class="link" data-toggle="collapse" data-target="#newFreightModel">新建模版</span>
				</div>
				<div class="collapse" id="newFreightModel">
				  <div class="well">
				  	  <div class="form-group">
					    <label for="freightModelName">模版名称</label>
					    <input type="text" class="form-control" v-model="freightModelName">
					  </div>
					  <div class="form-group">
					    <input type="radio" v-model="freightModelOption">
					    <label for="freightModelOption">包邮</label>
					    <input type="radio" id="freightModelOption" v-model="freightModelOption">
					    <label for="freightModelOption">设置运费</label><span><input type="text" v-model="freightModelOptionFee">元</span>
					  </div>
					  <span class="btn btn-default">确认</span>
				  </div>
				</div>
			</div>
			<div class="spec">
				<h2>商品规格：</h2>
				<div v-for="(spec,index) in this.spec" class="specDetail">
					<input type="text" :value="spec.name" ><input type="text" :value="spec.content">
				</div>
				<div class="specDetail">
					<input type="text"  placeholder="规格（选填，最多四个字）"><input type="text" placeholder="规格介绍（选填，最多50个字）">
				</div>
				<div class="specDetail">
					<input type="text"  placeholder="规格（选填，最多四个字）"><input type="text" placeholder="规格介绍（选填，最多50个字）">
				</div>
				<div class="specDetail">
					<input type="text"  placeholder="规格（选填，最多四个字）"><input type="text" placeholder="规格介绍（选填，最多50个字）">
				</div>
				<div class="specDetail">
					<input type="text"  placeholder="规格（选填，最多四个字）"><input type="text" placeholder="规格介绍（选填，最多50个字）">
				</div>
				<div class="specDetail">
					<input type="text"  placeholder="规格（选填，最多四个字）"><input type="text" placeholder="规格介绍（选填，最多50个字）">
				</div>
				<div class="specDetail">
					<input type="text"  placeholder="规格（选填，最多四个字）"><input type="text" placeholder="规格介绍（选填，最多50个字）">
				</div>
				<div class="specDetail">
					<input type="text"  placeholder="规格（选填，最多四个字）"><input type="text" placeholder="规格介绍（选填，最多50个字）">
				</div>
				<div class="specDetail">
					<input type="text"  placeholder="规格（选填，最多四个字）"><input type="text" placeholder="规格介绍（选填，最多50个字）">
				</div>
				<div class="specDetail">
					<input type="text"  placeholder="规格（选填，最多四个字）"><input type="text" placeholder="规格介绍（选填，最多50个字）">
				</div>
				<div class="specDetail">
					<input type="text"  placeholder="规格（选填，最多四个字）"><input type="text" placeholder="规格介绍（选填，最多50个字）">
				</div>
				<div class="specDetail">
					<input type="text"  placeholder="规格（选填，最多四个字）"><input type="text" placeholder="规格介绍（选填，最多50个字）">
				</div>
				<div class="specDetail">
					<input type="text"  placeholder="规格（选填，最多四个字）"><input type="text" placeholder="规格介绍（选填，最多50个字）">
				</div>
			</div>
			<div class="mainImage">
				<h2>商品详情:</h2>
				<div class="mainImageContent">
					<div class="mainOnlyImage" v-for="image in this.mainImage">
						<img :src="this.mainImage">
						<span class="mainOnlyImageDelete">删除</span>
					</div>				
					<label for="file1" class="myBtn">新增图片</label>
					<input class="file" id="file1" type='file' style="display:none">
    				<div id="prev_file1"></div><br/>
				</div>
				
			</div>

		</div>

	</div>
</template>
<script>
	export default{
		data:function(){
			return {
				objectId:"",
				uniqueId:"",
				shop:{},
				propertyOption:[],
				name:"",
				product:[],
				saleCategory:{},
				storeCategory:{},
				brand:"",
				freightModel:{},
				productService:[],
				mainImage:"",
				imageList:[],
				briefDescription:"",
				detailDescription:"",
				price:"",
				spec:[],
				state:"",
				//
				storeCategoryFirst:"",
				storeCategorySecond:"",
				storeCategoryThird:"",
				saleCategoryFirst:"",
				saleCategorySecond:"",
				checkedProductNames:[],
				//
				allStockCategorys:[],
				allStockCategorysSecond:[],
				first:[],
				second:[],
				third:[],
			}
		},
		props:["allselfselligproducts"],
		methods:{
			showDetail(objectId,uniqueId,propertyOption,name,productService,ip,brand,saleCategory,storeCategory,mainImage,imageList,collectionUser,comment,briefDescription,detailDescription,shop,saleCount,price,spec,freightModel,state){
				this.objectId=objectId;
				this.uniqueId=uniqueId;
				this.propertyOption=propertyOption;
				this.name=name;
				this.Service=service;
				this.ip=ip;
				this.brand=brand;
				this.saleCategory=saleCategory;
				this.storeCategory=storeCategory;
				this.mainImage=mainImage;
				this.imageList=imageList;
				this.collectionUser=collectionUser;
				this.comment=comment;
				this.briefDescription=briefDescription;
				this.detailDescription=detailDescription;
				this.shop=shop;
				this.saleCount=saleCount;
				this.price=price;
				this.spec=spec;
				this.freightModel=freightModel;
				this.state=state;
				toggleShow();				
			},
			toggleShow(){
				let shown = $('.shown');
				let productDetail = $('.productDetail.hide ');
 				if(shown.hasClass('shown')){
 					shown.removeClass('shown');
 					shown.addClass('hide');
 				}
 				if(productDetail.hasClass('hide')){
 					productDetail.removeClass('hide');
 					productDetail.addClass('shown');
 				}
			},
			editDetail(objectId,uniqueId,propertyOption,name,productService,ip,brand,saleCategory,storeCategory,mainImage,imageList,collectionUser,comment,briefDescription,detailDescription,shop,saleCount,price,spec,freightModel,state){
				let _this = this;
				this.objectId=objectId;
				this.uniqueId=uniqueId;
				this.propertyOption=propertyOption;
				this.name=name;
				this.Service=service;
				this.ip=ip;
				this.brand=brand;
				this.saleCategory=saleCategory;
				this.storeCategory=storeCategory;
				this.mainImage=mainImage;
				this.imageList=imageList;
				this.collectionUser=collectionUser;
				this.comment=comment;
				this.briefDescription=briefDescription;
				this.detailDescription=detailDescription;
				this.shop=shop;
				this.saleCount=saleCount;
				this.price=price;
				this.spec=spec;
				this.freightModel=freightModel;
				this.state=state;
				toggleEdit();
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
		      	toggleEdit();
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
		      	toggleEdit();
				$.ajax({
		          type: 'get',
		          url: '/Product/ShowStoreSecondCategory/',
		          data: {
		             page: 1,
		          },
		          success: function (data) {
		            let dataJson = JSON.parse(data);
		            _this.allStockCategorysSecond = dataJson.StoreCategorySeocnd;           
		          },
		          error: function(XMLHttpRequest, textStatus, errorThrown) {
		            swal('抓取不到数据')
		          },
		      	});
			},
			toggleEdit(){
				let shown = $('.shown');
				let editDetail = $('.editDetail.hide ');
 				if(shown.hasClass('shown')){
 					shown.removeClass('shown');
 					shown.addClass('hide');
 				}
 				if(editDetail.hasClass('hide')){
 					editDetail.removeClass('hide');
 					editDetail.addClass('shown');
 				}
			},
			deleteProduct(e,id){
				swal({
		            title: "你确定吗?",
		            text: "删除之后将无法恢复",
		            type: "warning",
		            showCancelButton: true,
		            confirmButtonColor: "#DD6B55",
		            confirmButtonText: "是的,我要删除它!",
		            closeOnConfirm: false
	          	},
				function(){
					$.ajax({
					    type: 'get',
					    url: '/xx/xx/',
					    data: {
					       objectId: id,
					    },
					    success: function (data) {
					      swal("成功删除");
					      $(e).parent('td').parent('tr').remove();               
					    },
					   error: function(XMLHttpRequest, textStatus, errorThrown) {
					     swal("无法删除");
					    },
					});
				});
			},
			getItDown(e,id){
				swal({
		            title: "你确定吗?",
		            text: "下架之后该商品将不会被顾客看到",
		            type: "warning",
		            showCancelButton: true,
		            confirmButtonColor: "#DD6B55",
		            confirmButtonText: "是的,我要下架它!",
		            closeOnConfirm: false
	          	},
				function(){
					$.ajax({
					    type: 'get',
					    url: '/xx/xx/',
					    data: {
					       objectId: id,
					    },
					    success: function (data) {
					      swal("成功下架");
					      let off = $(e).parent('td').children('.on.default');
					      off.removeClass('default');
					      let on =  $(e).parent('td').children('.off');
					      on.addClass('default');             
					    },
					   error: function(XMLHttpRequest, textStatus, errorThrown) {
					     swal("无法下架");
					    },
					});
				});
			},
			clickFirst(){	
			  let firstName = [];
			  let _this = this;
			  let addedFirst = "";
			  let addedStuff = $('.addedFirst');
		      if(addedStuff.hasClass('addedFirst')){

			  }else{
				  if(this.allStockCategorys != null){
					  this.allStockCategorys.forEach(
					    function(item,index){
					      firstName[index] = item.name;
					      let secondName = [];
					      let secondCategory = item.storeCategorySecond;
					      if(secondCategory != null){
						      secondCategory.forEach(
						        function(item,index){
							  	secondName[index] = item;
							  });
					     	 _this.second[index] = secondName;	
					      }      
					      addedFirst += "<option class='addedFirst' value='"+index+"'>"+item.name+"</option>"		    
					  });
					  this.first = firstName;
				  }else{
				  	this.first = [];
				  }
				  $(addedFirst).appendTo('#first');
			  } 
			},
			changeSecond(){
		      let secondCate = this.firstCate;
			  this.storeCategorySecond = this.second[secondCate];		
			  if(this.secondCate != ""){
			    this.changeThird();
			  }	  
	        },
	        changeThird(){
		      let secondCate = this.firstCate;
			  if(this.secondCate != "" && secondCate != ""){
				  let thirdCate = this.secondCate;
				  let first = this.second[secondCate];
				  let second = first[thirdCate];
			      this.storeCategoryThird = second.storeCategoryThird;
			  }else{
			  	  this.storeCategoryThird = this.storeCategorySecond[this.secondCate];
			  }         
	        },    

		},
	}
</script>
<style lang="scss">
	.selfSellingVue{
		.on,.off{
			display:none;
		}
		.on.default{
			display:initial;
		}
	}
</style>