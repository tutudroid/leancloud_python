<template>
	<div class="selfSellingVue">
		<table class="table table-striped">
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
		  	<tr v-for="product in allselfselligproducts"> 
		  		<td>{{product.name}}</td>
		  		<td>{{product.uniqueId}}</td>
		  		<td>{{product.price}}</td>
		  		<td>{{product.stockCount}}</td>
		  		<td>{{product.saleCount}}</td>
		  		<td>{{product.created_at}}</td>
		  		<td>{{product.shop}}</td>
		  		<td>{{product.state}}<span class="link" @click="getItDown($event,product.uniqueId)"><span class="on default">下架</span><span class="off">已下架</span></span></td>
		  		<td><span class="link" @click="edit()">编辑</span><span class="link" @click="deleteProduct($event,product.uniqueId)">删除</span></td>
		  	</tr>
		  </tbody>
		</table>
	</div>
</template>
<script>
	export default{
		data:function(){
			return {

			}
		},
		props:["allselfselligproducts"],
		methods:{
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
			}
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