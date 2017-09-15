<template>
	<div class="categoryRecommendationVue">
		<div class="shown">
			<label>推荐分类</label>
			<select v-model="recommendation" @change="searchProduct()">
				<option disabled value="">请选择你要搜索的推荐分类</option>
				<option>精品推荐</option>
				<option>新品推荐</option>
				<option>新品上架</option>
				<option>热销</option>
			</select>
			<span class="link" @click="addProduct()">添加商品</span>
			<div class="result">
				<table class="table table-bordered">
				  <thead>
				  	<th>商品名</th><th>编号</th><th>价格</th><th>库存</th><th>销量</th><th>创建时间</th><th>商家</th><th>状态</th><th>操作</th>
				  </thead>
				  <tbody v-if="products.length>0">
				  	<tr v-for="p in products">
				  		<td>{{p.name}}</td>
				  		<td>{{p.uniqueId}}</td>
				  		<td>{{p.price}}</td>
				  		<td>{{p.product.stockCount}}</td>
				  		<td>{{p.saleCount}}</td>
				  		<td>{{p.created_at}}</td>
				  		<td>{{p.shop}}</td>
				  		<td>{{p.state}}</td>
				  		<td @click="move($event,p.objectId)">移除</td>
				  	</tr>
				  </tbody>
				</table>
			</div>		
		</div>
		<div class="addProduct add hide">
			<span class="link" @click="toggle()">返回</span>
				  <div class="form-group">
				    <label>商品编号</label>
				    <input class="form-control" v-model="uniqueId">					  
				  </div>
				  <div class="form-group">
				    <label>商品名</label>
				    <input class="form-control" v-model="name">					  
				  </div>
				  <div class="form-group">
				    <label>创建时间</label>
				    <input class="form-control" v-model="created_at_begin">	
				    至
				    <input class="form-control" v-model="created_at_end">				  
				  </div>
				  <div class="form-group">
				    <label>品牌</label>
				    <input class="form-control" v-model="brandname">					  
				  </div>
				  <div class="form-group">
				    <label>库存分类</label>
						<div class="form-group" >
							<select class="form-control" id="firstSt" v-model="firstCatestock"  @click="clickFirst()" @change="changeSecond()">
							    <option disabled value="">请选择一级分类</option>
								<option disabled value="">--------</option>
								<option disabled value="">--------</option>
							</select>
						</div>
						<div class="form-group">
						    <select class="form-control" id="secondSt" v-model="secondCatestock" @change="changeThird()">
						        <option disabled value="">必须先选择一级分类</option>
						    </select>
								<option value="">"不选"</option>
						</div>
						<div class="form-group">
							<select class="form-control" id="third" v-model="thirdCatestock">
							    <option disabled value="">必须先选择二级分类</option>
								<option value="">"不选"</option>
							</select>
						</div>					  
				  </div>
				  <div class="form-group">
				    <label>销量</label>
				    <input class="form-control" v-model="saleCount">		
				    至
				    <input class="form-control" v-model="saleCount_end">			  
				  </div>
				  <div class="form-group">
				    <label>状态</label>
				    <input class="form-control" v-model="state">					  
				  </div>
				  <div class="form-group">
				    <label>销售分类</label>
					    <div class="form-group" >
							<select class="form-control" id="firstSa" v-model="firstCate" @click="clickSaleFirst()" @change="changeSaleSecond()">
							    <option disabled value="">请选择一级分类</option>
								<option disabled value="">--------</option>
								<option disabled value="">--------</option>
							</select>
						</div>
						<div class="form-group">			
						    <select class="form-control" id="secondSa" v-model="secondCate">
						        <option disabled value="">必须先选择一级分类</option>
								<option value="">"不选"</option>
						    </select>
						</div>					  
				  </div>
				 
				  <span class="btn btn-default" @click="searchAdd()">搜索</span>

				  <div class="result">
					<table class="table table-bordered">
					  <thead>
					  	<th>商品名</th><th>编号</th><th>价格</th><th>库存</th><th>销量</th><th>创建时间</th><th>商家</th><th>状态</th><th>操作</th>
					  </thead>
					  <tbody v-if="searchAdds.length>0">
					  	<tr v-for="p in searchAdds">
					  		<td>{{p.name}}</td>
					  		<td>{{p.uniqueId}}</td>
					  		<td>{{p.price}}</td>
					  		<td>{{p.product.stockCount}}</td>
					  		<td>{{p.saleCount}}</td>
					  		<td>{{p.created_at}}</td>
					  		<td>{{p.shop}}</td>
					  		<td>{{p.state}}</td>
					  		<td @click="add($event,p.objectId)">添加</td>
					  	</tr>
					  </tbody>
					</table>
				  </div>		
		</div>
	</div>
</template>
<script>
	export default{
		data:function(){
			return {
				recommendation:"",
				products:[],
				//////////
				firststock:[],
				secondstock:[],
				first:[],
				second:[],
				firstCatestock:"",
				secondCatestock:"",
				thirdCatestock:"",
				storecategory:[],
				//////////
				marketcategorys:[],
				firstCate:"",
				secondCate:"",
				//////////
				uniqueId:"",
				name:"",
				created_at_begin:"",
				created_at_end:"",
				state:"",
				saleCount:"",
				saleCount_end:"",
				searchAdds:[],
				saleok:0,
				stockok:0,
				brandname:"",
			}
		},
		methods:{
			toggle(){
				let shown = $('.shown');
				let hide = $('.hide');
				if(shown.hasClass('shown')){
					shown.removeClass('shown').addClass('hide');
				}
				if(hide.hasClass('hide')){
					hide.removeClass('hide').addClass('shown');
				}
			},
			addProduct(){
				this.toggle();
			},
			searchProduct(){
			    let _this = this;
		        $.ajax({
		          type: 'get',
		          url: '/xx/xx/',
		          data: {
		             page: 1,
		          },
		          success: function (data) {
		            let dataJson = JSON.parse(data);
		            _this.products = dataJson.xx;
		            
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
			searchAdd(){
			    let _this = this;
		        $.ajax({
		          type: 'get',
		          url: '/xx/xx/',
		          data: {
		             page: 1,
		          },
		          success: function (data) {
		            let dataJson = JSON.parse(data);
		            _this.searchAdds = dataJson.xx;
		            
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
			move(e,id){
				let remove = $(e.currentTarget).parent();
				swal({
		          title: "你确定移除这一个产品吗?",
		          text: "",
		          type: "warning",
		          showCancelButton: true,
		          confirmButtonColor: "#DD6B55",
		          confirmButtonText: "是的,我要移除它!",
		          closeOnConfirm: false
		        },
		        function(){
		          $.ajax({
		            type: 'post',
		            url: '/Product/DelCategoryRecommend/',
		            headers: {
		              'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').prop('value')
		            },
		            contentType: "application/json; charset=utf-8",
		            dataType: "json",
		            data: {
		            	objectId:id,
		            },
		            success: function (data) {
		              swal("此商品被成功移除");
		              $(remove).remove();
		            },
		            error: function(XMLHttpRequest, textStatus, errorThrown) {
		              swal("此商品移除失败");
		            },           
		          });
		        });
			},
			add(e,id){
				let add = $(e.currentTarget);
				swal({
		          title: "你确定添加这一个产品至推荐码?",
		          text: "",
		          type: "warning",
		          showCancelButton: true,
		          confirmButtonColor: "#DD6B55",
		          confirmButtonText: "是的,我要添加它!",
		          closeOnConfirm: false
		        },
		        function(){
		          $.ajax({
		            type: 'get',
		            url: '/Product/SaleCategoryRecommend/',
		            headers: {
		              'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').prop('value')
		            },
		            contentType: "application/json; charset=utf-8",
		            dataType: "json",
		            data: {
		            	objectId:id,
		            },
		            success: function (data) {
		              swal("此商品已添加至分类");
		              $(remove).text("已添加");
		            },
		            error: function(XMLHttpRequest, textStatus, errorThrown) {
		              swal("此商品添加失败");
		            },           
		          });
		        });
			},
			//stockCate
				clickFirst(){	
				  let _this = this;				  
			       
				  let firstName = [];
				  let addedFirst = "";
				  let addedStuff = $('.addedFirst');
			      if(this.stockok == 1){

				  }else{
				  		$.ajax({
				          type: 'get',
				          url: '/Product/ShowStoreCategory/',
				          data: {
				             page: 1,
				          },
				          success: function (data) {
				            let dataJson = JSON.parse(data);
				            _this.storecategory = dataJson.StoreCategory;      
				            _this.stockok = 1;     
				            	if(_this.storecategory != null){
								  _this.storecategory.forEach(
								    function(item,index){
								      firstName[index] = item.name;
								      let secondName = [];
								      let secondCategory = item.storeCategorySecond;
								      if(secondCategory != null){
									      secondCategory.forEach(
									        function(item,index){
										  	secondName[index] = item;
										  });
								     	 _this.secondstock[index] = secondName;	
								      }      
								      addedFirst += "<option class='stockaddedFirst' value='"+index+"'>"+item.name+"</option>";	    
								  });
								  _this.firststock = firstName;
							  }else{
							  	_this.firststock = [];
							  }
							  if($('.stockaddedFirst').hasClass('stockaddClass')){

							  }else{
							  	$(addedFirst).appendTo('select#firstSt');
							  }
							  
				          },
				          error: function(XMLHttpRequest, textStatus, errorThrown) {
				            swal('抓取不到数据')
				          },
				      });		
				      swal({
				        title: "正在加载库存分类，仅加载一次",
				        text:"你这么可爱，就等待一下呗",
				        timer: 4000,
				        showConfirmButton: false
				      });						  
				  } 
				  
				},
				changeSecond(){
				  let addedStuff = $('.stockaddedSecond');
				  if(addedStuff.hasClass('stockaddedSecond')){
				    $( ".stockaddedSecond" ).remove();
				  }
			      let secondCate = this.firstCatestock;
				  let secondCates = this.secondstock[secondCate];
				  let addedSecond = "";
				  secondCates.forEach(
				    function(item,index){
				      addedSecond += "<option class='stockaddedSecond' value='"+index+"'>"+item.name+"</option>";
				  });
				  $(addedSecond).appendTo('#secondSt');
				  if(this.secondCatestock != ""){
				    this.changeThird();
				  }	        
		       },
		       changeThird(){
				  let addedStuff = $('.addedThird');
				  if(addedStuff.hasClass('addedThird')){
				    $( ".addedThird" ).remove();
				  }
			      let secondCate = this.firstCatestock;
				  if(this.secondCatestock != ""){
					  let thirdCatestock = this.secondCatestock;
					  let first = this.secondstock[secondCate];
					  let second = first[thirdCatestock];
				      let thirdCatestocks = second.storeCategoryThird;
					  let addedThird = "";
					  thirdCatestocks.forEach(
					    function(item){
					      addedThird += "<option class='addedThird' value='"+item.id+"'>"+item.name+"</option>";
					      console.log(addedThird);
					    }
					  );
					 $(addedThird).appendTo('select#third');
				  }        
		       },  
		    //stockCate

		    //saleCate
			    clickSaleFirst(){	
			      let _this = this;
			       
				  let firstName = [];
				  let addedFirst = "";
				  let addedStuff = $('.addedFirst');
			      if(this.saleok == 1){

				  }else{
					  	$.ajax({
				          type: 'get',
				          url: '/Product/ShowSaleCategory/',
				          data: {
				             page: 1,
				          },
				          success: function (data) {
				            let dataJson = JSON.parse(data);
				            _this.marketcategorys = dataJson.SaleCategory;      
				            _this.saleok = 1;   
				            if(_this.marketcategorys != null){
							  _this.marketcategorys.forEach(
							    function(item,index){
							      firstName[index] = item.name;
							      let secondName = [];
							      let secondCategory = item.saleCategorySecond;
							      if(secondCategory != null){
								      secondCategory.forEach(
								        function(item,index){
									  	secondName[index] = item;
									  });
							     	 _this.second[index] = secondName;	
							      }      
							      addedFirst += "<option class='saleaddedFirst' value='"+index+"'>"+item.name+"</option>"	
								});
								_this.first = firstName;
							}else{
								_this.first = [];
							}
						  	if($('.saleaddedFirst').hasClass('saleaddedFirst')){

						  	}else{
						  		$(addedFirst).appendTo('select#firstSa');
						  	}  
				          },
				          error: function(XMLHttpRequest, textStatus, errorThrown) {
				            swal('抓取不到数据')
				          },
				      });					  
					  swal({
				        title: "正在加载销售分类，仅加载一次",
				        text:"你这么可爱，就等待一下呗",
				        timer: 4000,
				        showConfirmButton: false
				      });
				  } 
				  
				},
				changeSaleSecond(){
				  let addedStuff = $('.saleaddedSecond');
				  if(addedStuff.hasClass('saleaddedSecond')){
				    $( ".saleaddedSecond" ).remove();
				  }
			      let secondCate = this.firstCate;
				  let secondCates = this.second[secondCate];
				  let addedSecond = "";
				  secondCates.forEach(
				    function(item,index){
				      addedSecond += "<option class='saleaddedSecond' value='"+index+"'>"+item.name+"</option>";
				  });
				  $(addedSecond).appendTo('select#secondSa');    
		       },
		    //saleCate
		},
	}
</script>