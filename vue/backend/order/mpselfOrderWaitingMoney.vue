<template>
	<div class="selfOrderWaitingMoneyVue">
		<div class="shown">
			<div class="title">
				<span class="th">商品</span>
				<span class="th">单价</span>
				<span class="th">数量</span>
				<span class="th">买家</span>
				<span class="th">交易状态</span>
				<span class="th">总价</span>
				<span class="th">操作</span>
			</div>
			<div class="content container result" v-for="o in selforderwaitingmoney">
				<div class="row head">
					<div class="col-md-3">订单号:{{o.uniqueId}}</div>		
					<div class="col-md-3">下单时间:{{o.created_at}}</div>		
				</div>
				<div class="row data" v-for="m in selforderwaitingmoney.orderProduct">
					<div class="col-md-2">{{m.productMainImage}}</div>		
					<div class="col-md-2">{{m.productPrice}}</div>
					<div class="col-md-2">{{m.productCount}}</div>		
					<div class="col-md-2">{{o.user.name}}</div>
					<div class="col-md-1">{{m.orderState}}</div>		
					<div class="col-md-1">{{m.productPrice*m.productCount}}</div>
					<div class="col-md-1 link" @click="toggle('detail',m.user,o.receiverName,o.receiverPhoneNumber,o.receiverAddress,o.orderProduct)">查看详情</div>		
				</div>
			</div>
		</div>
		<div class="hide">
			<h2>订单状态：{{orderState}}</h2>
			<hr>
			<div class="operate">
				待付款
			</div>
			<div class="customerInfo">
				<h3>买家信息</h3>
				<hr>
				<div>
					<h4>用户:{{user.name}}</h4>
					<h4>收件人:{{receiverName}}</h4>
					<h4>联系电话:{{receiverPhoneNumber}}</h4>
					<h4>收件地址:{{receiverAddress}}</h4>
				</div>
			</div>
			<div class="orderInfo">
				<h3>订单信息</h3>、
				<hr>
				<div>
					<h4>订单号:{{uniqueId}}</h4>
					<h4>创建时间:{{created_at}}</h4>
				</div>
			</div>
			<div class="orderProducts container">
				<div class="title">
					<span class="th">商品</span>
					<span class="th">属性</span>
					<span class="th">单价</span>
					<span class="th">数量</span>
					<span class="th">优惠</span>
					<span class="th">总价</span>
				</div>
				<div class="row data" v-for="(m,index) in orderProduct">
					<div class="col-md-2">{{m.productMainImage}}</div>		
					<div class="col-md-2">{{m.productStyle}}</div>		
					<div class="col-md-2">{{m.productPrice}}</div>
					<div class="col-md-1">{{m.productCount}}</div>		
					<div class="col-md-1"></div>
					<div class="col-md-1 link" v-if="index == m.length-1">{{totalPrice}}</div>		
				</div>
			</div>
		</div>
	</div>
</template>
<script>
	export default{
		data:function(){
			return {
				user:{},
				receiverName:"",
				receiverPhoneNumber:"",
				receiverAddress:"",
				orderProduct:[],
				totalPrice:0,
			}
		},
		props:["selforderwaitingmoney"],
		methods:{	
			toggle(detail="",user,receiverName,receiverPhoneNumber,receiverAddress,orderProduct){
				if(detail == "detail"){
					this.user = user;
					this.receiverName = receiverName;
					this.receiverPhoneNumber = receiverPhoneNumber;
					this.receiverAddress = receiverAddress;
					this.orderProduct = orderProduct;
					orderProduct.forEach(function(item){
						this.totalPrice += item.productPrice;
					});
				}
				let shown = $('.shown');
				let hide = $('.hide');
				if(shown.hasClass('shown')){
					shown.removeClass('shown').addClass('hide');
				}
				if(hide.hasClass('hide')){
					hide.removeClass('hide').addClass('shown');
				}
			},			
		},
	}
</script>