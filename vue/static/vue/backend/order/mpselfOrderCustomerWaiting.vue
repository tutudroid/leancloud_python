<template>
	<div class="selfOrderCustomerWaitingVue">
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
			<div class="content container result" v-for="o in selfordercustomerwaiting">
				<div class="row head">
					<div class="col-md-3">订单号:{{o.uniqueId}}</div>		
					<div class="col-md-3">下单时间:{{o.created_at}}</div>		
				</div>
				<div class="row data" v-for="m in selfordercustomerwaiting.orderProduct">
					<div class="col-md-2">{{m.productMainImage}}</div>		
					<div class="col-md-2">{{m.productPrice}}</div>
					<div class="col-md-2">{{m.productCount}}</div>		
					<div class="col-md-2">{{o.user.name}}</div>
					<div class="col-md-1">{{m.orderState}}</div>		
					<div class="col-md-1">{{m.productPrice*m.productCount}}</div>
					<div class="col-md-1 link" @click="toggle('detail',o.shop.uniqueId,m.user,o.receiverName,o.receiverPhoneNumber,o.receiverAddress,o.orderProduct)">查看详情</div>		
				</div>
			</div>
		</div>
		<div class="hide">
			<h2>订单状态：{{orderState}}</h2>
			<hr>
			<div class="operate">
				<span class="sendGood myBtn" data-toggle="modal" data-target="modal1">发货</span>
				<div class="modal1 fade" tabindex="-1" role="dialog">
					  <div class="modal-dialog" role="document">
					    <div class="modal-content">
					      <div class="modal-header">
					        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
					        <h4 class="modal-title">发货</h4>
					      </div>
					      <div class="modal-body">
					      	<label>配送公司</label>
					        <select v-model="sendCompany">
					        	<option>顺风</option>
					        	<option>EMS</option>
					        </select>
					        <label>配送单号</label>
					        <input type="text" v-model="sendNumber">
					      </div>
					      <div class="modal-footer">
					        <button type="button" class="btn btn-default" data-dismiss="modal">关闭</button>
					        <button type="button" class="btn btn-primary" @click="sendGood(uniqueId)">保存</button>
					      </div>
					    </div><!-- /.modal-content -->
					  </div><!-- /.modal-dialog -->
					</div><!-- /.modal -->
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
				user:"",
				objectId:"",
				receiverName:"",
				receiverPhoneNumber:"",
				receiverAddress:"",
				orderProduct:[],
				totalPrice:0,
				//
				sendNumber:"",
				sendCompany:"",
			}
		},
		props:["selfordercustomerwaiting"],
		methods:{
			toggle(detail="",id,user,receiverName,receiverPhoneNumber,receiverAddress,orderProduct){
				if(detail == "detail"){
					this.user = user;
					this.objectId = id;
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
			sendGood(id){
				swal({
		          title: "你确定发货吗?",
		          text: "",
		          type: "warning",
		          showCancelButton: true,
		          confirmButtonColor: "#DD6B55",
		          confirmButtonText: "是的,我要发货!",
		          closeOnConfirm: false
		        },
		        function(){
		          $.ajax({
		            type: 'post',
		            url: '/Order/DisplaceOrder/',
		            headers: {
		              'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').prop('value')
		            },
		            contentType: "application/json; charset=utf-8",
		            dataType: "json",
		            data: {
		            	objectId:id, 
		            	shipperCode:"xxxxxxx", 
		            	shipperName:_this.sendCompany, 
		            	logisticsCode:_this.sendNumber
		            },
		            success: function (data) {
		              swal("发货成功");
		            },
		            error: function(XMLHttpRequest, textStatus, errorThrown) {
		              swal("发货失败");
		            },           
		          });
		        });
			},
		},
	}
</script>